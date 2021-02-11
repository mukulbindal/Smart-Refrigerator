from imageai.Detection import VideoObjectDetection, ObjectDetection
import cv2
import numpy as np
import os
import requests
from collections import Counter
import pyautogui as pg

labels = {'bottle': True,
          'bowl': True,
          'banana': True,
          'apple': True,
          'sandwich': True,
          'orange': True,
          'broccoli': True,
          'hot_dog': True,
          'carrot': True,
          'pizza': True,
          'donut': True,
          'cake': True}


class LiveDetectionv2():
    def __init__(self):
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(os.path.join(self.execution_path, 'food\\yolo\\resnet50_coco_best_v2.1.0.h5'))
        self.detector.loadModel("fastest")
        self.list_of_items = []
        self.first_time = True

    def __del__(self):
        del self.detector

    def detect(self, streamURL, socket):
        print("Starting to detect...")
        self.socket = socket
        img_res = requests.get(f"http://{streamURL}:8080/shot.jpg")
        img_arr = np.array(bytearray(img_res.content), dtype=np.uint8)
        ##Added Code:
        # img_arr = np.asarray(pg.screenshot())

        ##
        img_arr = cv2.imdecode(img_arr, -1)
        # print(img_arr)
        print(type(img_arr))
        print("Camera Connected...")
        arr, predictions = self.detector.detectObjectsFromImage(input_image=img_arr,
                                                                input_type="array",
                                                                output_type="array",
                                                                minimum_percentage_probability=50
                                                                )
        self.per_second_stream(predictions)
        if self.first_time and len(self.list_of_items) == 0:
            self.socket.send_status("empty")
            self.first_time = False

    def per_second_stream(self, detected_items):
        print("Detected Something..")
        detected_items = Counter([x['name'] for x in detected_items])
        proper_list = []
        for key, value in detected_items.items():
            if key in labels.keys():
                proper_list.append({'name': key, 'quantity': value})
        if sorted(self.list_of_items, key=lambda x: (x['name'], x['quantity'])) != \
                sorted(proper_list, key=lambda x: (x['name'], x['quantity'])):
            self.list_of_items = proper_list
            self.socket.send_status(proper_list)
        if len(self.list_of_items) == 0:
            self.socket.send_status("empty")
        print("Finished sending data")


class LiveDetection():
    def __init__(self):
        self.execution_path = os.getcwd()
        self.detector = VideoObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(os.path.join(self.execution_path, 'food\\yolo\\yolo.h5'))
        self.detector.loadModel("fastest")
        self.list_of_items = []

    def __del__(self):
        del self.detector

    def detect(self, streamURL, socket):
        print("Starting to detect...")
        self.socket = socket
        self.camera = cv2.VideoCapture('http://' + streamURL + ':8080/video')
        print("Camera Connected...")
        self.video_path = self.detector.detectObjectsFromVideo(camera_input=self.camera,
                                                               save_detected_video=False,
                                                               per_second_function=self.per_second_stream,
                                                               frames_per_second=60,
                                                               log_progress=False,
                                                               minimum_percentage_probability=30,
                                                               frame_detection_interval=60,
                                                               video_complete_function=self.finished
                                                               )

    def per_second_stream(self, second_number, output_arrays, count_arrays, average_output_count):
        self.socket.send_status("alive")
        # A dictionary
        detected_items = count_arrays[len(count_arrays) - 1]
        if not len(detected_items):
            self.socket.send_status([])
            return
        proper_list = []
        for key, value in detected_items.items():
            if key in labels.keys():
                proper_list.append({'name': key, 'quantity': value})
        if sorted(self.list_of_items, key=lambda x: (x['name'], x['quantity'])) != sorted(proper_list,
                                                                                          key=lambda x: (x['name'],
                                                                                                         x[
                                                                                                             'quantity'])):
            self.list_of_items = proper_list
            self.socket.send_status(proper_list)

    def finished(self):
        print("Finished the stream")
