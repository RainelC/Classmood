from db import *
from models import *
from face import *
import pymongo

#-------Students-------#

def new_student(student: Student):
    b64_img = student.img.replace('data:image/png;base64,', '')
    img = process_picture(b64_img)

    if (img):
        fileid = fs.put(img, filename = "Student picture")
        db.students.insert_one({
            "_id": student.student_id,
            "name": student.name,
            "lastname": student.lastname,
            "image": {
                "fileid": fileid,
                "alt": "student face"
            }
        })
        return True
    else:
        return  False

def update_stud(student: Student):
    if (student.img != None): 
        b64_img = student.img.replace('data:image/png;base64,', '')
        img = process_picture(b64_img)
        if (img):
            fileid = fs.put(img, filename = "Student picture")
            image = {
                "fileid": fileid,
                "alt": "student face"
            }
        else:
            return False

    else:
        student_db = db.students.find({"_id": student.student_id})
        for i in student_db:
            image = i['image']

    try:
        collection.update_one(
            {"_id": student.student_id},
            {"$set": {
                    "name": student.name,
                    "lastname": student.lastname,
                    "image": image
                }
            }) 
        return True
    except:
        return False

def delete_stud(id: str):
    result = db.students.delete_one({"_id": id})
    print(result.deleted_count)
    if (result.deleted_count != 0):
        return True
    else:
        return False

#-------Teachers-------#

def new_teacher(teacher: Teachers):
    name = teacher.name
    lastname = teacher.lastname
    email = teacher.email
    password = teacher.password

    try:
        db.teachers.insert_one({
            "name": name,
            "lastname": lastname,
            "email": email,
            "password": password, 
        })
        return True
    except:
        return False

def update_teach(teacher: Teachers):
    id = teacher.teacher_id
    name = teacher.name
    lastname = teacher.lastname
    email = teacher.email
    password = teacher.password

    try:
        collection.update_one(
            {"_id": id},
            {"$set": {
                "name": name,
                "lastname": lastname,
                "email": email,
                "password": password, 
                }          
            }
        )
        return True
    except:
        return False

def delete_teach(id: str):
    result = db.teachers.delete_one({"_id": id})
    if (result.deleted_count != 0):
        return True
    else:
        return False

#-------Subjects-------#

def new_subject(subject: Subject):

    id = subject.teacher_id
    name = subject.name_subject

    if id != '' and name != '':
        try:
            collection.update_one(
                {"_id": id},
                {"$set": {
                        "name_subject": name
                    }
                }
            )
            return True
        except:
            return False
    else:
        return False

def update_subject(subject: Subject):

    id = subject.subject_id
    name = subject.name_subject

    try:
        collection.update_one(
            {"_id": id},
            {"$set": {
                "name": name
                }          
            }
        )
        return True
    except:
        return False

def delete_subject(id: str):
    result = db.subject.delete_one({"_id": id})
    if (result.deleted_count != 0):
        return True
    else:
        return False

#/-------Schedules-------#

def new_schedule(schedule: Schedule, classroom_id: int):
    try:
        db.classrooms.update_one(
            {"_id": classroom_id},
            {"$push": {
                "schedule": {
                    "day": schedule.day,
                    "start_time": schedule.start_time,
                    "end_time": schedule.end_time
                }
            }}
        )
        return True
    except pymongo.errors.PyMongoError:
        return False

def update_schedul(schedule: Schedule, classroom_id: int):
    try:
        db.classrooms.update_one(
            {"_id": classroom_id},
            {"$set": {
                "schedule.day": schedule.day,
                "schedule.$.start_time": schedule.start_time,
                "schedule.$.end_time": schedule.end_time
            }}
        )
        return True
    except pymongo.errors.PyMongoError:
        return False

def delete_schedul(day: str, classroom_id: int):
    try:
        db.classrooms.update_one(
            {"_id": classroom_id},
            {"$pull": {"schedule": {"day": day}}}
        )
        return True
    except pymongo.errors.PyMongoError:
        return False

#-------Classrooms-------#

def new_classroom(classroom: Classrooms):
    try:
        db.classrooms.insert_one({
            "_id": classroom.classroom_id,
            "teacher_id": classroom.teacher_id,
            "classroom_name": classroom.classroom_name,
            "description": classroom.description
        })
        return True
    except pymongo.errors.PyMongoError:
        return False

def update_classroom(classroom: Classrooms):
    try:
        db.classrooms.update_one(
            {"_id": classroom.classroom_id},
            {"$set": {
                "teacher_id": classroom.teacher_id,
                "classroom_name": classroom.classroom_name,
                "description": classroom.description
            }}
        )
        return True
    except pymongo.errors.PyMongoError:
        return False

def delete_classroom(classroom_id: int):
    result = db.classrooms.delete_one({"_id": classroom_id})
    return result.deleted_count != 0

#/-------Login-------#

def ValidUser(credentials: Credentials):
    email = credentials.email
    password = credentials.password

    teacher = db.teachers.find_one({"email": email})
    if teacher:
        if teacher.get('password') == password:
            return True, "Ok", teacher
        else:
            return False, "Unauthorized", teacher
    return False, "NotFound", {}

db, fs, collection = conexion_db()