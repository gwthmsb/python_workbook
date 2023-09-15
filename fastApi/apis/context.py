from typing import Any
from uuid import uuid4
from contextvars import ContextVar

class Context:
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            ctx_v = ContextVar(k)
            t = ctx_v.set(v)
            self.contextVars = {
                "id": k, "token": t
            }

    async def add_request_id(self):
        request_uid = uuid4()
        con_req_id = ContextVar("request_id")
        token = con_req_id.set(request_uid)
        self.contextVars["request_id"] = {
            "id": con_req_id, "token": token
        }
            
    def get_request_id(self):
        return req.get("id").get() if(req:= self.contextVars.get("request_id", None)) else None
    
    async def del_requet_id(self):
        await self.del_context_var("request_id")

    async def del_context_var(self, variable):
        con_var.get("id").reset(con_var.get("token")) if(con_var:= self.contextVars.get(variable, None)) else None
    