import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.route("/", methods=['GET'])
async def hello(request: fastapi.Request):
    return fastapi.Response("Hello world!")


@app.route("/bye")
async def bye(request: fastapi.Request):
    return fastapi.Response("Bye world!")


if __name__ == '__main__':
    uvicorn.run("main:app", port=18881, reload=True, debug=True)