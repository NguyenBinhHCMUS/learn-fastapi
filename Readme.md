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
