from dotenv import dotenv_values
from fastapi import FastAPI, Request
from pymongo import MongoClient
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Routers
from routes.users import router as UserRouter
from routes.uploads import router as UploadRouter
from routes.profiles import router as ProfileRouter
from routes.products import router as ProductRouter

config = dotenv_values(".env")

app = FastAPI()


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UploadRouter, tags=["Uploads"], prefix="/uploads")
app.include_router(UserRouter, tags=["Users"], prefix="/users")
app.include_router(ProfileRouter, tags=["Profiles"], prefix="/profiles")
app.include_router(ProductRouter, tags=["Products"], prefix="/products")
