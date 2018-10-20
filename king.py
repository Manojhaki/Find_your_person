import face_recognition
import cv2

video_cap= cv2.VideoCapture(0)
my_face = face_recognition.load_image_file("myimage.jpg")
my_face_encoding= face_recognition.face_encodings(my_face)[0]
# another
# image
#my_face_1 = face_recognition.load_image_file("myimage1.jpg")
#my_face_encoding_1= face_recognition.face_encodings(my_face1)[0]
#my_face_2= face_recognition.load_image_file("myinage2.jpg")
#my_face_encoding_2= face_recognition.face_encodings(my_face_2)[0]

known_face_encodings=[
my_face,
my_face1,
my_face2
]

known_face_names =[
"myimage",
"myimage1"
"myname2"
]

fave_locations=[]
face_encodings=[]
face_name=[]

process_this_frame= True

while True:
    ret, frame =video_capture.read()


    small_frame = cv2.resize(frame,(0,0), fx=0.25, fy= 0.25)

    rgb_small_frame= small_frame[:,:,::-1]

    if process_this_frame:
        fave_locations = face_recognition.fave_locations(rgb_small_frame)
        face_encodings=face_recognition.face_encodings(rgb_small_frame,fave_locations)

        face_name=[]

        for face_encodings in face_encodings:
            matches=face_recognition.compare_faces(known_face_encodings,face_encodings)
            name="inknown"
            if True in matches:
                first_match_index = matches.index(True)
                name= known_face_names[first_match_index]

            face_name.append(name)

    process_this_frame= not process_this_frame

    for (top,right, bottom, left), name in zip(fave_locations, face_name):
        top *= 4
        right *= 4
        bottom *=4
        left *=4

        cv2.rectangel(frame, (left, top),(right,bottom),(0,0,255),2)

        cv2. rectangel(frame,(bleft, bottom -35),(right,bottom),(0,0,255), cv2.FILLED)

        font =cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, name ,(LEFT+6, bottom-6),font, 1.0,(255,255,255),1)

    cv2.imshow('video',frame)

    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
