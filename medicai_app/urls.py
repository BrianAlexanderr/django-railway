from django.urls import path
from .views import predict_disease, get_symptoms, register_user, get_hospitals, get_photo, get_symptom_names

urlpatterns = [
    path("predict_disease/", predict_disease, name="predict_disease"),
    path('symptoms/', get_symptoms, name='get_symptoms'),
    path('register_user/', register_user, name='register_user'),
    path('facilities/', get_hospitals, name='get_facilities'),
    path('facilities/photo/<int:facility_id>/', get_photo, name='get_facility_photo'),
    path('get_symptom_names/', get_symptom_names, name="get_symptom_names"),
]
