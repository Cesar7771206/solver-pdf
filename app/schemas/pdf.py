from pydantic import BaseModel

class MarkdownResponse(BaseModel):
    filename: str
    content: str
    size_bytes: int