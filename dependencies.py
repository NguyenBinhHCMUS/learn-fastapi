from typing import Union, Annotated

from fastapi import Query, Header, HTTPException


async def common_parameters(
        skip: int = 0,
        limit: int = 100
):
    return {"skip": skip, "limit": limit}


class CommonQueryParams:
    def __init__(self, keyword: str = Query(None, min_length=0, max_length=256, title="Search by keyword"),
                 skip: int = 0, limit: int = 100):
        self.keyword = keyword
        self.skip = skip
        self.limit = limit


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key
