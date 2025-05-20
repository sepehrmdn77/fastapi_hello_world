from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session  # for creating session
from h_w.schemas import HwResponseSchema, HelloCreateSchema
from core.database import get_db
from h_w.models import HelloModel

router = APIRouter(tags=["Hello_world"])


@router.get("/")
async def main_page():
    return "Go to: url/hello_world"


@router.get(
        "/hello_world",
        response_model=
            None #  It can be HwResponseSchema if there is a valid response model
        )
async def hello_world(
    db: Session = Depends(get_db),
):
    query = db.query(HelloModel).filter_by(id=1)
    return query.first()


@router.post("/hello_world", response_model=HwResponseSchema)
async def create_hello(
    request: HelloCreateSchema,
    db: Session = Depends(get_db),
):
    data = request.model_dump()
    task_obj = HelloModel(**data)
    db.add(task_obj)
    db.commit()
    db.refresh(task_obj)
    return task_obj

