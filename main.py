import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)

# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# def get_food(food_name: FoodEnum):
#     return {"food_name": food_name}
#
#
# @app.put("/items/{item_id}")
# async def read_items(
#         item_id: UUID,
#         start_datetime: Annotated[Union[datetime, None], Body()] = None,
#         end_datetime: Annotated[Union[datetime, None], Body()] = None,
#         repeat_at: Annotated[Union[time, None], Body()] = None,
#         process_after: Annotated[Union[timedelta, None], Body()] = None):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }
#
#
# @app.get("/items")
# async def read_items_with_cookie(cookie_id: Annotated[Union[str, None], Cookie()] = None,
#                                  accept_encoding: Annotated[Union[str, None], Header()] = None,
#                                  sec_ch_ua: Annotated[Union[str, None], Header()] = None,
#                                  user_agent: Annotated[Union[str, None], Header()] = None):
#     return {"Cookie": cookie_id, "Accept-Encoding": accept_encoding, "Sec-Ch-Ua": sec_ch_ua,
#             "User-Agent": user_agent}
#
#
# @app.get("/keyword-weights/", response_model=dict[str, float])
# async def read_keyword_weights():
#     return {"foo": 2.3, "bar": 3.4}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}
#
#
# @app.get("/items-header/{item_id}", description="Add custom headers")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
#         )
#     return {"item": items[item_id]}


# @app.get("/unicorns/{name}", description="Custom exception handlers")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     if name == "override":
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"unicorn_name": name}
