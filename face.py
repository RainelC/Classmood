from retinaface import RetinaFace
from deepface import DeepFace
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image
import base64
import cv2
import numpy as np
import os
from io import BytesIO
from db import conexion_db


def process_picture(encoded_string):
    try:
        img_data = base64.b64decode(encoded_string)
        nparr = np.frombuffer(img_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        faces =  RetinaFace.extract_faces(img_np)
        ima_IO = BytesIO()
        for face in faces:
            plt.figure(figsize=(face.shape[1] / 100, face.shape[0] / 100), dpi=100)
            plt.imshow(face)
            plt.axis('off')
            plt.savefig(ima_IO, format='jpg')
            plt.savefig('face.jpg', bbox_inches='tight', pad_inches=0)
            ima_IO.seek(0)
            process_enconded_string = base64.b64encode(ima_IO.read())
            return process_enconded_string
    except:
        return False



def attendance(img,teacher_id):
    b64_img = img.replace('data:image/png;base64,', '')
    img_v = process_picture(b64_img)

    if (img_v):
        img_data = base64.b64decode(img_v)
        nparr = np.frombuffer(img_data, np.uint8)
        img_np_rec = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        db, fs, _ = conexion_db()
        student_ids = []
        classrooms = db.classrooms.find({"teacher_id": teacher_id})
        for classroom in classrooms:
            idClass = classroom['_id']
            student_ids.extend(classroom["students_ids"])

        students = db.students.find({"_id": {"$in": student_ids}})
        for student in students:
            fid = student['image']['fileid']
            img_64 = fs.get(fid).read()

            img_data = base64.b64decode(img_64)
            nparr = np.frombuffer(img_data, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            try:
                obj = DeepFace.verify(img_np, img_np_rec
                , model_name = 'ArcFace', detector_backend = 'retinaface')
                print(obj['verified'])
                if obj['verified']:
                    try:
                        
                        objs = DeepFace.analyze(
                            img_path = "face.jpg", 
                            actions = ['emotion'],
                        )
                    
                        print(objs)
                        sentiment = objs[0]['dominant_emotion']
                        # sentiment_confidence = obj[0]['face_confidence']

                        date = datetime.now()
                        status = "present"
                        db.classrooms.update_one(
                            {"_id": idClass},
                            {"$push": {
                                "session": {
                                    "student_id": student["_id"],
                                    "date": date,
                                    "attendance_status": status,
                                    "sentiment": sentiment,
                                    # "sentiment_confidence": sentiment_confidence
                                }
                            }}
                            )
                        return True, {"status": "Ok"}
                    except Exception as e:
                        print(f"Error during emotion analysis: {e}")
                        return False, {"error": f"Error during emotion analysis: {e}"}

            except Exception as e:
                print(f"Error during face verification: {e}")
                return False, {"error": f"Error during face verification: {e}"}
    else: 
        print("image error")
        return False, {"error": f"Image error"}