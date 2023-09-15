from fastapi import FastAPI

from config import get_config
from context import Context

config = get_config()
ctx = config.context

app = FastAPI()


@app.middleware("http")
async def app_setup(request, call_next):
    await ctx.add_request_id()
    response = await call_next(request)

    await ctx.del_requet_id()
    return response

@app.get("/info")
def getAppInfo():
    return {"config": get_config()}

@app.get("/")
def get():
    return {"request_id": ctx.get_request_id()}

    