# thirdparty
import uvicorn

# project
from logger import initialize_logger
from src import config
from src.app_initializer import get_fastapi_application


initialize_logger()
app = get_fastapi_application()


@app.get("/")
async def root() -> dict:
    return {"Status": "Application in progress"}


if __name__ == "__main__":
    uvicorn.run(app, host=config.app_config.host, port=config.app_config.port)
