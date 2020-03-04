import face_recognition
import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders





def write_file(l1):
  f1=open("sample.txt","w")
  for i in range(len(l1)):
      str1=l1[i]+'\n'
      f1.write(str1)
  f1.close()    
  print("written")
  mail_txt()
  
def mail_txt():
    fromaddr = "asd052165@gmail.com"
    toaddr = "youraddress.email"
 
    msg = MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE EMAIL"
 
    body = "text"
 
    msg.attach(MIMEText(body, 'plain'))
 
    filename = "sample.txt"
    attachment = open("sample.txt", "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'mnbv!0192')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
video_capture = cv2.VideoCapture(0)


rak_image = face_recognition.load_image_file(path to image)
rak_face_encoding = face_recognition.face_encodings(rak_image)[0]
rohit_image=face_recognition.load_image_file(path to image2)
rohit_face_encoding=face_recognition.face_encodings(rohit_image)[0]






known_face_encodings = [
    rak_face_encoding,
    rohit_face_encoding
   ]
known_face_names = [
    "Rakesh",
    "Rohit"]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
l1=[]
while True:
    
    ret, frame = video_capture.read()

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    
    rgb_small_frame = small_frame[:, :, ::-1]

    
    if process_this_frame:
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
           
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
             
            if name not in l1:
                    l1.append(name)
            face_names.append(name)

    process_this_frame = not process_this_frame


   
    for (top, right, bottom, left), name in zip(face_locations, face_names):
       
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

       
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

       
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    
    cv2.imshow('Video', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break


video_capture.release()
cv2.destroyAllWindows()
print(l1)
write_file(l1) 