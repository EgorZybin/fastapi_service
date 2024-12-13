from pydantic import BaseModel


class RequestBody(BaseModel):
    url: str
