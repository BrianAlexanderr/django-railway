from django.urls import path
from .views import predict_disease, get_symptoms, register_user, get_hospitals, get_photo, get_symptom_names, get_recommended_doctors, get_precautions, save_diagnosis, get_medical_history

urlpatterns = [
    path("predict_disease/", predict_disease, name="predict_disease"),
    path('symptoms/', get_symptoms, name='get_symptoms'),
    path('register_user/', register_user, name='register_user'),
    path('facilities/', get_hospitals, name='get_facilities'),
    path('facilities/photo/<int:facility_id>/', get_photo, name='get_facility_photo'),
    path('get_symptom_names/', get_symptom_names, name="get_symptom_names"),
    path('doctors/<int:disease_id>/', get_recommended_doctors, name='get_recommended_doctors'),
    path('get_precautions/', get_precautions, name='get_precautions'),
    path('save_diagnosis/', save_diagnosis, name='save_diagnosis'),
    path('api/medical_history/<str:user_id>/', get_medical_history, name='get_medical_history'),
]
