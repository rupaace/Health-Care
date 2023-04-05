from django.urls import path
from .views import *

app_name = 'healthcare'

urlpatterns = [
    # Patient URLs
    path('patients/', PatientListCreateView.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientRetrieveView.as_view(), name='patient_retrieve'),
    
    # Doctor URLs
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorRetrieveView.as_view(), name='doctor_retrieve'),
    
    # Appointment URLs
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment_list_create'),
    path('appointments/<int:pk>/', AppointmentRetrieveView.as_view(), name='appointment_retrieve'),
    
    # Prescription URLs
    path('prescriptions/', PrescriptionListCreateView.as_view(), name='prescription_list_create'),
    path('prescriptions/<int:pk>/', PrescriptionRetrieveView.as_view(), name='prescription_retrieve'),
    
    # Medical Record URLs
    path('medical-records/', MedicalRecordListCreateView.as_view(), name='medical_record_list_create'),
    path('medical-records/<int:pk>/', MedicalRecordRetrieveView.as_view(), name='medical_record_retrieve'),
    
    # Insurance URLs
    path('insurance/', InsuranceListCreateView.as_view(), name='insurance_list_create'),
    path('insurance/<int:pk>/', InsuranceRetrieveView.as_view(), name='insurance_retrieve'),
    
    # Payment URLs
    path('payments/', PaymentListCreateView.as_view(), name='payment_list_create'),
    path('payments/<int:pk>/', PaymentRetrieveView.as_view(), name='payment_retrieve'),
    
    # Test Result URLs
    path('test-results/', TestResultListCreateView.as_view(), name='test_result_list_create'),
    path('test-results/<int:pk>/', TestResultRetrieveView.as_view(), name='test_result_retrieve'),
    
    # Referral URLs
    path('referrals/', ReferralListCreateView.as_view(), name='referral_list_create'),
    path('referrals/<int:pk>/', ReferralRetrieveView.as_view(), name='referral_retrieve'),
    
    # Allergy URLs
    path('allergies/', AllergyListCreateView.as_view(), name='allergy_list_create'),
    path('allergies/<int:pk>/', AllergyRetrieveView.as_view(), name='allergy_retrieve'),
]
