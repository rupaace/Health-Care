# views.py

from rest_framework import generics
from .models import Patient, Doctor, Appointment, Prescription, MedicalRecord
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, PrescriptionSerializer, MedicalRecordSerializer
from sklearn.linear_model import LinearRegression
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PatientList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PrescriptionList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class MedicalRecordList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class MedicalRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class PatientOutcomePrediction(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        # Load data from database
        patients = Patient.objects.all()
        patient_data = []

        for patient in patients:
            data = [patient.age, patient.weight, patient.height, patient.blood_pressure]
            patient_data.append(data)

        labels = []
        for patient in patients:
            labels.append(patient.mortality)

        model = LinearRegression()
        model.fit(patient_data, labels)

        new_patient_data = [[45, 75, 170, '120/80']]
        prediction = model.predict(new_patient_data)

        response_data = {'prediction': prediction}
        return Response(response_data)
