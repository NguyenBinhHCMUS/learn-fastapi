## 1. Introduce

Cài đặt FastAPI và các thư viện cần thiết trong môi trường ảo

Set up env

```commandline
python -m venv env

pip install -r requirements.txt
```

Cài đặt thư viện chính:

```commandline
pip install fastapi
```

Cài đặt máy chủ ASGI uvicorn để run code:

```commandline
pip install uvicorn
```

Khởi động server với uvicorn và hot reload, port mặc định sẽ là 8000

```commandline
uvicorn main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc

Python cũng có một tính năng cho phép đặt metadata bổ sung trong những gợi ý kiểu dữ liệu này bằng cách sử dụng
Annotated.

## 12. Cookie and Header Parameters¶

You can define Cookie parameters the same way you define Query and Path parameters.

## 14. Extra Models

About ```**user_in.dict()```

### Pydantic's ```.dict()```

```user_in``` is a Pydantic model of class ```UserIn.```

Pydantic models have a .dict() method that returns a dict with the model's data.

So, if we create a Pydantic object user_in like:

```python
user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
```

and then we call:

user_dict = user_in.dict()
we now have a dict with the data in the variable user_dict (it's a dict instead of a Pydantic model object).

And if we call:

```python
print(user_dict)
```

we would get a Python dict with:

```doctest
{
    'username': 'john',
    'password': 'secret',
    'email': 'john.doe@example.com',
    'full_name': None,
}
```

### Unwrapping a dict

If we take a dict like ```user_dict``` and pass it to a function (or class) with ```**user_dict```, Python will "unwrap"
it.
It will pass the keys and values of the user_dict directly as key-value arguments.

So, continuing with the user_dict from above, writing:

```
UserInDB(**user_dict)
```

Would result in something equivalent to:

```doctest
UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)
```

Or more exactly, using user_dict directly, with whatever contents it might have in the future:

```doctest
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)
```

## 19. Handling Errors

There are many situations in which you need to notify an error to a client that is using your API.

This client could be a browser with a frontend, a code from someone else, an IoT device, etc.

You could need to tell the client that:

- The client doesn't have enough privileges for that operation.
- The client doesn't have access to that resource.
- The item the client was trying to access doesn't exist.
- etc.

In these cases, you would normally return an HTTP status code in the range of 400 (from 400 to 499).

This is similar to the 200 HTTP status codes (from 200 to 299). Those "200" status codes mean that somehow there was a "
success" in the request.

The status codes in the 400 range mean that there was an error from the client.
