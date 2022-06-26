import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.route("/", methods=['GET'])
async def hello(request: fastapi.Request):
    return fastapi.Response("Hello world!")


@app.route("/bye")
async def bye(request: fastapi.Request):
    return fastapi.Response("Bye world!")
