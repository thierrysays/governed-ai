# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Thierry Sayegh-Sauvage
package governedai.routing_test

import rego.v1

import data.governedai.routing

models := [
	{"id": "m-ok", "status": "approved", "allowed_data_classes": ["public", "internal"]},
	{"id": "m-cand", "status": "candidate", "allowed_data_classes": ["public"]},
	{"id": "m-other", "status": "approved", "allowed_data_classes": ["public"]},
]

systems := [
	{"id": "s-ok", "status": "approved", "models": ["m-ok", "m-cand"], "allowed_data_classes": ["public", "internal"]},
	{"id": "s-cand", "status": "candidate", "models": ["m-ok"], "allowed_data_classes": ["public"]},
	{"id": "s-narrow", "status": "approved", "models": ["m-ok"], "allowed_data_classes": ["public"]},
]

allowed(req) if {
	routing.allow with data.models as models with data.systems as systems with input as req
}

reasons(req) := r if {
	r := routing.deny_reasons with data.models as models with data.systems as systems with input as req
}

test_allow_approved_system_model_and_class if {
	allowed({"system": "s-ok", "model": "m-ok", "data_class": "internal"})
}

test_deny_unknown_system if {
	req := {"system": "ghost", "model": "m-ok", "data_class": "public"}
	not allowed(req)
	"system_not_in_registry" in reasons(req)
}

test_deny_candidate_system if {
	req := {"system": "s-cand", "model": "m-ok", "data_class": "public"}
	not allowed(req)
	"system_not_approved" in reasons(req)
}

test_deny_model_not_declared_by_system if {
	req := {"system": "s-ok", "model": "m-other", "data_class": "public"}
	not allowed(req)
	"model_not_authorised_for_system" in reasons(req)
}

test_deny_class_above_system_ceiling_even_if_model_allows if {
	req := {"system": "s-narrow", "model": "m-ok", "data_class": "internal"}
	not allowed(req)
	"data_class_not_allowed_for_system" in reasons(req)
}

test_deny_unknown_model if {
	req := {"system": "s-ok", "model": "ghost", "data_class": "public"}
	not allowed(req)
	"model_not_in_registry" in reasons(req)
}

test_deny_candidate_model if {
	req := {"system": "s-ok", "model": "m-cand", "data_class": "public"}
	not allowed(req)
	"model_not_approved" in reasons(req)
}

test_deny_class_above_model_clearance_even_if_system_allows if {
	req := {"system": "s-ok", "model": "m-other", "data_class": "internal"}
	not allowed(req)
	"data_class_not_allowed" in reasons({"system": "s-ok", "model": "m-other", "data_class": "internal"})
}
