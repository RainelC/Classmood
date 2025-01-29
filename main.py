from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from logic import *

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

# @app.get("/students")
# def index():    
#     return {"response": "Hello world"}


#-------Students-------#

@app.post("/student/create")
def create_student(student: Student):
    if (new_student(student)):
        return student
    else:
        return status.HTTP_400_BAD_REQUEST

@app.put("/student/update")
def update_student(student: Student, response: Response):
    if update_stud(student):
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.delete("/student/delete")
def delete_student(id: str, response: Response):
    if delete_stud(id):
       response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


#-------Teachers-------#

@app.post("/teacher/create")
def create_teacher(teacher: Teachers, response: Response):
    if new_teacher(teacher):
        response.status_code = status.HTTP_201_CREATED
        return teacher
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Failed to create teacher"}
    
@app.put("/teacher/update")
def update_teacher(teacher: Teachers, response: Response):
    if update_teach(teacher):
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.delete("/teacher/delete")
def delete_teacher(id: str, response: Response):
    if delete_teach(id):
       response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

#-------Subjects-------#

@app.post("/subjects/create")
def create_subject(subject: Subject, response: Response):
    if new_subject(subject):
        response.status_code = status.HTTP_201_CREATED
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.put("/subjects/update")
def update_subject(subject: Subject, response: Response):
    if update_subject(subject):
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.delete("/subjects/delete")
def delete_subject(id: str, response: Response):
    if delete_subject(id):
       response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

#-------Schedules-------#

@app.post("/schedule/create")
def create_schedule(schedule: Schedule, response: Response):
    if new_schedule(schedule):
        response.status_code = status.HTTP_201_CREATED
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.put("/schedule/update")
def update_schedule(schedule: Schedule, response: Response):
    if update_schedul(schedule):
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.delete("/schedule/delete")
def delete_schedule(id: str, response: Response):
    if delete_schedul(id):
       response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

#-------Classrooms-------#

@app.post("/classroom/create")
def create_classroom(classroom: Classrooms, response: Response):
    if new_classroom(classroom):
        response.status_code = status.HTTP_201_CREATED
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.put("/classroom/update")
def update_classroom(classroom: Classrooms, response: Response):
    if update_classroom(classroom):
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.delete("/classroom/delete")
def delete_classroom(id: int, response: Response):
    if delete_classroom(id):
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_404_NOT_FOUND




@app.post("/attendance")
def attendance_post(data: Attendance_data, response: Response):
    if attendance(data.img, data.teacher_id):     
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)



@app.post("/login")
def login_user(credentials: Credentials, response: Response):
    Success, message, user = ValidUser(credentials)

    if Success:
        response.status_code = status.HTTP_201_CREATED
        return user
    else:
        if (message == "Unauthorized"):
            response.status_code = status.HTTP_401_UNAUTHORIZED
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
    
