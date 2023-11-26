from pydantic import BaseModel

# Define a Pydantic model called Post
class Post(BaseModel):
    title: str
    short_desc: str
    description: str
    tags: list[str]
