from typing import Union, Annotated

from fastapi import APIRouter, status, Query, Path, Body, Depends
from fastapi.encoders import jsonable_encoder
from typing_extensions import Any

from dependencies import common_parameters, CommonQueryParams, verify_key, verify_token
from models import User, RoleEnum, StatusEnum
from models.profile import Profile
from schemas import UserIn, UserOut
from utils.helpers import fake_save_user

router = APIRouter()


@router.get("",
            response_model=list[User],
            response_model_exclude={"password"},
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(verify_token), Depends(verify_key)])
async def get_users(
        commons: Annotated[CommonQueryParams, Depends()],
        sort: Union[str, None] = None
) -> Any:
    """
    Get all users
    - keyword: text to search
    - skip:
    - limit:
    - sort:
    - return: [Users]
    """
    return [{
        "user_name": "binhbong",
        "password": "hashpassword",
        "first_name": "Binh",
        "last_name": "Bong",
        "phone_number": "012345678",
        "roles": [RoleEnum.shop],
        "status": StatusEnum.active
    }]


@router.get("me", response_model=User, response_model_exclude={"password"})
async def get_current_user() -> Any:
    return {
        "id": 1,
        "user_name": "binhbong",
        "password": "hashpassword",
        "first_name": "Binh",
        "last_name": "Bong",
        "phone_number": "012345678",
        "roles": [RoleEnum.shop],
        "status": StatusEnum.active
    }


@router.get("{id}")
async def get_user(id: int = Path(..., title="The ID of the user to get", ge=1, le=100)):
    return {"message": "Hello world" + " "}


@router.post("", response_model=UserOut, status_code=201)
def create_user(user: UserIn = Body(...,
                                    openapi_examples={
                                        "shop": {
                                            "user_name": "binhbong",
                                            "password": "hashpassword",
                                            "first_name": "Binh",
                                            "last_name": "Bong",
                                            "phone_number": "012345678",
                                            "roles": [RoleEnum.shop],
                                            "status": StatusEnum.active
                                        },
                                        "client": {
                                            "user_name": "binhbong",
                                            "password": "hashpassword",
                                            "first_name": "Binh",
                                            "last_name": "Bong",
                                            "phone_number": "012345678",
                                            "roles": [RoleEnum.client],
                                            "status": StatusEnum.active
                                        },
                                        "admin": {
                                            "user_name": "binhbong",
                                            "password": "hashpassword",
                                            "first_name": "Binh",
                                            "last_name": "Bong",
                                            "phone_number": "012345678",
                                            "roles": [RoleEnum.admin],
                                            "status": StatusEnum.active
                                        }
                                    })) -> Any:
    # user_dict = user.dict()
    # if user.phone_number:
    #     phone_number_with_prefix = "(+84)" + user.phone_number[1:]
    #     user_dict.update({"phone_number_with_prefix": phone_number_with_prefix})

    user_saved = fake_save_user(user)
    return user_saved


@router.put("{id}")
async def update_user(*, id: int = Path(..., title="The ID the user to update"), user: User = Body(..., embed=True),
                      profile: Profile = Body(..., embed=True)):
    json_compatible_item_data = jsonable_encoder(user)
    # users[id] = json_compatible_item_data
    print(json_compatible_item_data)
    return {"id": id, "user": {"first_name": user.first_name, **user.dict()}, "message": "Hello world"}
