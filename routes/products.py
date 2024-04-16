from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies import common_parameters

router = APIRouter()


@router.get("")
async def get_products(commons: Annotated[dict, Depends((common_parameters))]):
    return commons
