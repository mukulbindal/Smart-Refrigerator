import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import *
import time
from .liveFoodDetection import LiveDetection, LiveDetectionv2
import timeit
import threading
import multiprocessing
from asgiref.sync import async_to_sync
import asyncio
url = '192.168.1.4'


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.stop = False
        self.accept()
        self.send(text_data=json.dumps("Creating Object"))
        self.liveDetectionModel = LiveDetectionv2()
        self.send(text_data=json.dumps("Object Created"))


    def disconnect(self, close_code=1000):
        print("Disconnect Called")
        self.close()
        self.stop = True
        print("Disconnect Over")

    def detect(self):
        print("Entered Aysnc detect fn")
        # try:
        while True:
            try:
                self.liveDetectionModel.detect(self.url, self)
            except Exception as e:
                self.send_status("CameraError")
                self.stop = True
            if self.stop:
                break
            time.sleep(2)
        # except Exception as e:
        #     print("Exception in detect",e)

    def receive(self, text_data=None, bytes_data=None):
        print("Received message from client!")
        self.url = json.loads(text_data)['CamIP']
        self.thread = threading.Thread(target=self.detect)
        self.thread.start()
        print("Thread started")

    def send_status(self, data):
        self.send(text_data=json.dumps(data))
