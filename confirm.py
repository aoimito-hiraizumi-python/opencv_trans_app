import cv2
import face_recognition

original_face_img = "images/man.png"

face_img = face_recognition.load_image_file(original_face_img)
face_landmarks_list = face_recognition.face_landmarks(face_img)

# print(face_landmarks_list)

face_img = cv2.imread(original_face_img)
print(face_landmarks_list[0]["chin"])
for chin_coordinate in face_landmarks_list[0]["right_eye"]:
    cv2.drawMarker(
        face_img, 
        chin_coordinate,
        color=(255, 0, 0),
        markerType=cv2.MARKER_CROSS,
        thickness=1,
    )

cv2.imshow("Image", face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
