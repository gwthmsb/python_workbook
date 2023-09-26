from fastapi import FastAPI

from config import get_config, configure_logger
from loguru import logger
from scratch import print_log

config = get_config()
ctx = config.context

configure_logger()

#logger.remove(0)
#logger.add(sink=stdout, level="INFO", format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {extra[request_id]} | {message}", serialize=False, backtrace=True)

app = FastAPI()


@app.middleware("http")
async def app_setup(request, call_next):
    await ctx.add_request_id()
    with logger.contextualize(**config.config_to_add_logs()):
        response = await call_next(request)
    await ctx.del_requet_id()
    return response

@app.get("/info")
def getAppInfo():
    logger.info("Inside the GetAppInfo")
    return {"config": get_config()}

@app.get("/")
def get():
    logger.info("Logging with request ID")
    print_log()
    return {"request_id": ctx.get_request_id()}

    