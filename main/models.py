from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField()


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    medicine = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    notes = models.TextField()


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.CharField(max_length=100)
    notes = models.TextField()


class Insurance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance_company_name = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    group_number = models.CharField(max_length=50, blank=True)
    policy_holder_name = models.CharField(max_length=100, blank=True)
    policy_holder_relationship = models.CharField(max_length=50, blank=True)


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)


class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ordering_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result = models.TextField()
    notes = models.TextField(blank=True)


class Referral(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referring_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    referred_doctor = models.CharField(max_length=100)
    notes = models.TextField(blank=True)


class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergen = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)


class Immunization(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine_type = models.CharField(max_length=100)
    date_administered = models.DateField()
    notes = models.TextField(blank=True)


class FamilyHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    relative = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    notes = models.TextField(blank=True)


class EmergencyContact(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)


