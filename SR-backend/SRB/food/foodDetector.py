from imageai.Detection import ObjectDetection
from pathlib import Path


class ModelOfHell:
    def __init__(self):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath("./food/yolo/yolo.h5")
        self.detector.loadModel("fastest")

    def detect(self, image):
        return self.detector.detectObjectsFromImage(input_type="array", input_image=image, output_image_path="./cap.jpg")


