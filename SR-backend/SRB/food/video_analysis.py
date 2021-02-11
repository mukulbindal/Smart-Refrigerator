from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()

camera = cv2.VideoCapture(0)


def per_second(second_number, output_arrays, count_arrays, average_output_count):
    # print("SECOND : ", second_number)
    # print("Array for the outputs of each frame ", output_arrays)
    # print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count) if average_output_count else None
    # print("------------END OF A SECOND --------------")


detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo/yolo.h5"))
detector.loadModel()
video_path = detector.detectObjectsFromVideo(camera_input=camera, save_detected_video=False, per_second_function=per_second,
     frames_per_second=1, log_progress=True, minimum_percentage_probability=30, frame_detection_interval=3)

print(video_path)