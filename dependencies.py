async def common_parameters(
        skip: int = 0,
        limit: int = 100
):
    return {"skip": skip, "limit": limit}
