from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="Hello world api")
async def root():
    return {"message": "Hello world"}

@app.post("/")
def post():
    return {"message": "Post api" }
