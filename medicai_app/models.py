from django.db import models
from django.contrib.postgres.fields import ArrayField

class Symptom(models.Model):
    symptom_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'symptoms'

class UserProfile(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)  # UID dari Firebase
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])  # Tanggal lahir
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

class Hospital(models.Model):
    facility_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.TextField()
    photo = models.BinaryField(null=True, blank=True) 

    class Meta:
        db_table = 'healthcarefacilities'

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    precautions = models.TextField()

    class Meta:
        db_table = 'diseases'

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    hospital_id = models.IntegerField()
    contact_info = models.CharField(max_length=255)
    photo = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'doctors'

class DoctorSpeciality(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    class Meta:
        db_table = 'doctor_specialization'

class DiagnosisHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255)  # Matches 'character varying'
    diagnosis = models.CharField(max_length=255)  # Matches 'character varying'
    doctor_notes = models.TextField(null=True, blank=True)  # Matches 'text'
    created_at = models.DateTimeField(auto_now_add=True)  # Matches 'timestamp'
    symptoms = ArrayField(models.TextField(), blank=True, default=list)

    class Meta:
        db_table = 'medicalhistory'

class Consultation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='consultation')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='consultation')

    class Meta:
        db_table = 'consultation_chat'

class Message(models.Model):
    consultation = models.ForeignKey(Consultation,  on_delete=models.CASCADE, related_name='message')
    sender = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'
