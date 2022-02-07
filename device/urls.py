from django.urls import path
from .views import CamAllViewApi, CamSingleViewApi, VideoView, CamAllView, CamSingleView

urlpatterns = [
    path('api/v1/all', CamAllViewApi.as_view(), name="all_api"),
    path('api/v1/<slug:slug>', CamSingleViewApi.as_view(), name="single_api"),
    path('', CamAllView.as_view(), name="all_camera"),
    path('camera/<slug:slug>', CamSingleView.as_view(), name="this_camera"),
    path('live_stream', VideoView, name="video_cap"),
]