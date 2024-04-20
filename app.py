from dotenv import dotenv_values
from fastapi import FastAPI, Request
from pymongo import MongoClient
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from helpers.exception_handler import UnicornException, unicorn_exception_handler, http_exception_handler, \
    validation_exception_handler
from middlewares import add_process_time_header, ProcessTimeMiddleware
# Routers
from routes.users import router as UserRouter
from routes.uploads import router as UploadRouter
from routes.profiles import router as ProfileRouter
from routes.products import router as ProductRouter

config = dotenv_values(".env")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.add_exception_handler(UnicornException, http_exception_handler)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )
app.add_middleware(ProcessTimeMiddleware, some_attribute="some_attribute_here_if_needed")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UploadRouter, tags=["Uploads"], prefix="/uploads")
app.include_router(UserRouter, tags=["Users"], prefix="/users")
app.include_router(ProfileRouter, tags=["Profiles"], prefix="/profiles")
app.include_router(ProductRouter, tags=["Products"], prefix="/products")
