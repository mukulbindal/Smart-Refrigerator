from django.shortcuts import render
from django.http import JsonResponse
from .imageCapture import putimage
from .foodDetector import ModelOfHell
import timeit
from .liveFoodDetection import LiveDetection

# Create your views here.
# model_of_hell = ModelOfHell()



def detect_items(request):
    if request.method == 'GET':
        IP = "192.168.1.2"
        image_arr = putimage(IP)
        print(image_arr.size)
        start_time = timeit.default_timer()
        # res = model_of_hell.detect(image_arr)
        stop_time = timeit.default_timer()
        print('Elapsed:', stop_time - start_time)
        # print(res)
        return JsonResponse({'result': "res"})
