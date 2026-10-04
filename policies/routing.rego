# Model routing: a request may reach a model only if the model is approved
# and cleared for the request's data class. Default deny.
package governedai.routing

import rego.v1

default allow := false

model_for(id) := m if {
	some m in data.models
	m.id == id
}

allow if {
	m := model_for(input.model)
	m.status == "approved"
	input.data_class in m.allowed_data_classes
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
