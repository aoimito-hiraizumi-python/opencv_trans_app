import cv2

original_hitoshi_img = "images/hitoshi.jpg"
original_face_img = "images/man.png"
original_mask_img = "images/otahuku.png"


def find_face():
    # 顔検出の分類機を用意 白黒の方が精度が上がる
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    img = cv2.imread(original_face_img)

    face_list = cascade.detectMultiScale(img)
    # [[261  71 107 107]]

    return face_list


def paste_img(face_list):
    x = face_list[0][0]
    y = face_list[0][1]
    w = face_list[0][2]
    h = face_list[0][3]
    face_img = cv2.imread(original_face_img)
    mask_img = cv2.imread(original_mask_img)
    resized_mask_img = cv2.resize(mask_img, dsize=(w, h))

    cv2.imwrite("images/resize_otahuku.png", resized_mask_img)

    face_img[y : y + h, x : x + w] = cv2.imread("images/resize_otahuku.png")
    cv2.imwrite("images/hensin.png", face_img)


face_list = find_face()
paste_img(face_list)
