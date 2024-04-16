from fastapi import Path, Body, status
from fastapi.routing import APIRouter

from models import Profile

router = APIRouter()


@router.patch("{profile_id}", response_model=Profile, status_code=status.HTTP_201_CREATED)
async def update_profile(profile_id: int = Path(..., title="The ID the profile to update"),
                         profile: Profile = Body(...)):
    stored_profile_data = await Profile.find_one({"_id": profile_id})
    stored_profile_model = Profile(**stored_profile_data)
    update_data = profile.dict(exclude_unset=True)
    update_profile = stored_profile_model.copy(update=update_data)
    await Profile.update_one({"_id": id}, {"$set": update_profile})
    return update_profile
