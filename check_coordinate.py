import cv2

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN: #発生したイベントマウスを移動して左クリックした時の座標の取得
        print(x, y)
    return x, y
# 座標を表示

img = cv2.imread("images/man.png")

cv2.imshow("Face", img)
cv2.setMouseCallback("Face", onMouse)
cv2.waitKey() # ()が空欄の時、ずっと表示、何かクリックしたら画像が消える
