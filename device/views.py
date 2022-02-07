from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import StreamingHttpResponse, response
from django.views.generic import ListView, DetailView
from .serializer import CamSerializer
from .models import Cam
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import cv2
import threading

class CamAllViewApi(APIView):
    
    def get(self, request):
        all_fans = Cam.objects.all()
        data = CamSerializer(all_fans, many=True).data
        return Response(data)

class CamSingleViewApi(APIView):
    def get(self, request, slug):
        single = get_object_or_404(Cam, slug=slug)
        data = CamSerializer(single).data
        return Response(data)


class CamAllView(LoginRequiredMixin, ListView):
    model = Cam
    context_object_name = "all"
    template_name = 'device/all.html'

class CamSingleView(LoginRequiredMixin, DetailView):
    model = Cam
    context_object_name = "one"
    template_name = "device/single.html"

@login_required
def VideoView(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass

    return render(request, 'devices/video_cap.html', context={'cam': cam})

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.grabbed, self.frame = self.video.read()
        threading.Thread(target=self.update, args=()).start()
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            self.grabbed, self.frame = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')