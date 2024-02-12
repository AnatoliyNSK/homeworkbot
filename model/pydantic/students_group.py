from pydantic import BaseModel


class StudentGroup(BaseModel):
    group_name: str
    disciplines_short_name: list[str]
    students: list[str]
