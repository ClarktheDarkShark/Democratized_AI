from .base import BaseTool

class IacEmitterTool(BaseTool):
    name = "iac_emitter"

    def execute(self, args):
        kind = args.get("kind", "terraform")
        if kind == "ansible":
            return {"artifact": "---\n- hosts: all\n  tasks: []"}
        return {"artifact": "terraform {}"}
