from rest_framework import serializers
from .models import Symptom, UserProfile, Hospital, Doctor
import base64  

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['symptom_id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'name', 'email', 'age', 'gender']

class HospitalSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ['facility_id', 'name', 'type', 'latitude', 'longitude', 'address', 'photo_url']

    def get_photo_url(self, obj):
        if obj.photo:
            return base64.b64encode(obj.photo).decode('utf-8')
        return None 

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'name', 'specialization', 'hospital_id']