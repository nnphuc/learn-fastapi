import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def home():
    return "hello"
