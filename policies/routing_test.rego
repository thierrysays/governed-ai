package governedai.routing_test

import rego.v1

import data.governedai.routing

models := [
	{"id": "m-ok", "status": "approved", "allowed_data_classes": ["public", "internal"]},
	{"id": "m-cand", "status": "candidate", "allowed_data_classes": ["public"]},
]

test_allow_approved_model_and_permitted_class if {
	routing.allow with data.models as models with input as {"model": "m-ok", "data_class": "internal"}
}

test_deny_unknown_model if {
	not routing.allow with data.models as models with input as {"model": "ghost", "data_class": "public"}
	"model_not_in_registry" in routing.deny_reasons with data.models as models with input as {"model": "ghost", "data_class": "public"}
}

test_deny_candidate_model if {
	not routing.allow with data.models as models with input as {"model": "m-cand", "data_class": "public"}
	"model_not_approved" in routing.deny_reasons with data.models as models with input as {"model": "m-cand", "data_class": "public"}
}

test_deny_data_class_not_cleared if {
	not routing.allow with data.models as models with input as {"model": "m-ok", "data_class": "restricted"}
	"data_class_not_allowed" in routing.deny_reasons with data.models as models with input as {"model": "m-ok", "data_class": "restricted"}
}
