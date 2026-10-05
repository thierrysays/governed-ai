# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Thierry Sayegh-Sauvage
# Model routing: a request reaches a model only if the system is approved and
# uses that model, and the data class is cleared by BOTH the system and the model.
# Default deny.
package governedai.routing

import rego.v1

default allow := false

system_for(id) := s if {
	some s in data.systems
	s.id == id
}

model_for(id) := m if {
	some m in data.models
	m.id == id
}

allow if {
	s := system_for(input.system)
	s.status == "approved"
	input.model in s.models
	input.data_class in s.allowed_data_classes
	m := model_for(input.model)
	m.status == "approved"
	input.data_class in m.allowed_data_classes
}

deny_reasons contains "system_not_in_registry" if {
	not system_for(input.system)
}

deny_reasons contains "system_not_approved" if {
	s := system_for(input.system)
	s.status != "approved"
}

deny_reasons contains "model_not_authorised_for_system" if {
	s := system_for(input.system)
	not input.model in s.models
}

deny_reasons contains "data_class_not_allowed_for_system" if {
	s := system_for(input.system)
	not input.data_class in s.allowed_data_classes
}

deny_reasons contains "model_not_in_registry" if {
	not model_for(input.model)
}

deny_reasons contains "model_not_approved" if {
	m := model_for(input.model)
	m.status != "approved"
}

deny_reasons contains "data_class_not_allowed" if {
	m := model_for(input.model)
	not input.data_class in m.allowed_data_classes
}
