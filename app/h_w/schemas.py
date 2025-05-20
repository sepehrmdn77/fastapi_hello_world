from pydantic import BaseModel, Field

class HwResponseSchema(BaseModel):
    text : str = Field(..., description="This is a simple API.")

class HelloCreateSchema(HwResponseSchema):
    pass
