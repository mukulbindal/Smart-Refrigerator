import cv2
import numpy as np
import requests


def putimage(IP):
    img_res = requests.get(f"http://{IP}:8080/shot.jpg")
    img_arr = np.array(bytearray(img_res.content), dtype=np.uint8)
    # img_arr.resize((1024,))
    print('shape is ', img_arr.shape)
    img_arr = cv2.imdecode(img_arr, -1)

    return img_arr
