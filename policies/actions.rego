# Agent tool calls: the tool must be approved; irreversible tools additionally
# require an explicit human approval recorded in the request. Default deny.
package governedai.actions

import rego.v1

default allow := false

tool_for(id) := t if {
	some t in data.tools
	t.id == id
}

allow if {
	t := tool_for(input.tool)
	t.status == "approved"
	t.irreversible == false
}

allow if {
	t := tool_for(input.tool)
	t.status == "approved"
	t.irreversible == true
	input.human_approval.approved == true
	count(input.human_approval.approver) > 0
}

deny_reasons contains "tool_not_in_registry" if {
	not tool_for(input.tool)
}

deny_reasons contains "tool_not_approved" if {
	t := tool_for(input.tool)
	t.status != "approved"
}

deny_reasons contains "human_approval_required" if {
	t := tool_for(input.tool)
	t.irreversible == true
	not allow
}
