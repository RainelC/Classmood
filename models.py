from pydantic import BaseModel
from typing import List
from typing import Optional
from datetime import time, date


class Attendance_data(BaseModel):
    teacher_id: str
    img: str

class Credentials(BaseModel):
    email: str
    password: str


class Student(BaseModel):
    student_id: str
    name: str
    lastname: str
    img: Optional[str]


class Subject(BaseModel):
    teacher_id: str
    name_subject: str


class Schedule(BaseModel):
    day: str
    start_time: time
    end_time: time

class Classrooms(BaseModel):
    classroom_id: int
    teacher_id: str
    classroom_name: str
    description: str 
    students_ids: List[str]
    schedule: List[Schedule]


class Teachers(BaseModel):
    teacher_id: str
    name: str
    lastname: str
    email: str
    password: str
    subject: Optional[List[str]]
    classrooms: Optional[List[Classrooms]]

class Session(BaseModel):
    student_id: int
    attendance_status: str
    sentiment: Optional[str]
    sentiment_confidence: Optional[str]

class Classes(BaseModel):
    class_id: int
    classroom_id: int
    date: date
    session: List[Session]