from pydantic import BaseModel

class Resume(BaseModel):
    raw_text: str 