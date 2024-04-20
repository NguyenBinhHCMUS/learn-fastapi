from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse, PlainTextResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)
