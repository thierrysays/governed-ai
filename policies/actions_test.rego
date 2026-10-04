package governedai.actions_test

import rego.v1

import data.governedai.actions

tools := [
	{"id": "read", "status": "approved", "irreversible": false},
	{"id": "write", "status": "approved", "irreversible": true},
	{"id": "draft", "status": "candidate", "irreversible": false},
]

test_allow_reversible_approved_tool if {
	actions.allow with data.tools as tools with input as {"tool": "read"}
}

test_deny_irreversible_without_human_approval if {
	not actions.allow with data.tools as tools with input as {"tool": "write"}
	"human_approval_required" in actions.deny_reasons with data.tools as tools with input as {"tool": "write"}
}

test_deny_irreversible_with_refused_approval if {
	not actions.allow with data.tools as tools with input as {"tool": "write", "human_approval": {"approved": false, "approver": "a"}}
}

test_allow_irreversible_with_human_approval if {
	actions.allow with data.tools as tools with input as {"tool": "write", "human_approval": {"approved": true, "approver": "a"}}
}

test_deny_candidate_tool if {
	not actions.allow with data.tools as tools with input as {"tool": "draft"}
	"tool_not_approved" in actions.deny_reasons with data.tools as tools with input as {"tool": "draft"}
}

test_deny_unknown_tool if {
	not actions.allow with data.tools as tools with input as {"tool": "ghost"}
	"tool_not_in_registry" in actions.deny_reasons with data.tools as tools with input as {"tool": "ghost"}
}
