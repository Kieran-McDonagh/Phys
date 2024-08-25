from pydantic import BaseModel


class NewWorkout(BaseModel):
    type: str
    body: dict
    notes: str
