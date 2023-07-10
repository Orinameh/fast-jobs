from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import root_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values and "slug" not in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()

        return values

    # @validator('slug', pre=True)
    # def generate_slug(cls, slug, values):
    #     title = values.get("title")
    #     slug = None
    #     if title:
    #         slug = title.replace(' ', '-').lower()
    #     return slug


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: date

    class Config:
        orm_mode = True
