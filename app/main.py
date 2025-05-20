from contextlib import asynccontextmanager
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from h_w.routes import router as hello_wordl_route
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import time


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan"""
    print("Application startup")
    yield
    print("Application shutdown")


tags_metadata = [
    {
        "name": "tasks",
        "description": "Operations related to task management",
        "externalDocs": {
            "description": "More about tasks",
            "url": "https://example.com/docs/tasks",
        },
    }
]

app = FastAPI(
    lifespan=lifespan,
    tags_metadata=tags_metadata,
    title="Hello World!",
    description="Simple 'Hello World' project to showcase API",
    summary="Say hello to world...",
    version="0.0.1",
    contact={
        "name": "Sepehr Maadani",
        "url": "https://github.com/sepehrmdn77/",
        "email": "sepehrmaadani98@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://choosealicense.com/",
    },
)

app.include_router(hello_wordl_route)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(exc):
    print(exc.__dict__)
    error_response = {
        "error": True,
        "status_code": exc.status_code,
        "detail": exc.detail,
    }
    return JSONResponse(status_code=exc.status_code, content=error_response)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def http_validation_handler(request, exc):
    print(exc.__dict__)
    error_response = {
        "error": True,
        "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
        "detail": exc.errors(),
    }
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error_response
    )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
