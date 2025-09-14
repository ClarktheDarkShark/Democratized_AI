package platform.policy

default allow = false

allow {
  input.subject.role == "admin"
}

allow {
  input.subject.role == "operator"
  input.action == "tools.execute"
  input.resource.tool in input.context.allow_tools
}
