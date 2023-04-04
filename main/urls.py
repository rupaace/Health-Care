from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
PatientList,
PatientDetail,
DoctorList,
DoctorDetail,
AppointmentList,
AppointmentDetail,
PrescriptionList,
PrescriptionDetail,
MedicalRecordList,
MedicalRecordDetail,
PatientOutcomePrediction,

)

urlpatterns = [
path('patients/', PatientList.as_view(), name='patient-list'),
path('patients/int:pk/', PatientDetail.as_view(), name='patient-detail'),
path('doctors/', DoctorList.as_view(), name='doctor-list'),
path('doctors/int:pk/', DoctorDetail.as_view(), name='doctor-detail'),
path('appointments/', AppointmentList.as_view(), name='appointment-list'),
path('appointments/int:pk/', AppointmentDetail.as_view(), name='appointment-detail'),
path('prescriptions/', PrescriptionList.as_view(), name='prescription-list'),
path('prescriptions/int:pk/', PrescriptionDetail.as_view(), name='prescription-detail'),
path('medical/', MedicalRecordList.as_view(), name='medical-list'),
path('medical/int:pk/', MedicalRecordDetail.as_view(), name='medical-detail'),
path('api/patients/predict-outcome/', PatientOutcomePrediction.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)