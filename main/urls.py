from django.urls import path
from .views import *

app_name = 'healthcare'

urlpatterns = [
    # Patient URLs
    path('patients/', PatientListCreateView.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient_retrieve_update_destroy'),
    
    # Doctor URLs
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor_retrieve_update_destroy'),
    
    # Appointment URLs
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment_list_create'),
    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment_retrieve_update_destroy'),
    
    # Prescription URLs
    path('prescriptions/', PrescriptionListCreateView.as_view(), name='prescription_list_create'),
    path('prescriptions/<int:pk>/', PrescriptionRetrieveUpdateDestroyView.as_view(), name='prescription_retrieve_update_destroy'),
    
    # Medical Record URLs
    path('medical-records/', MedicalRecordListCreateView.as_view(), name='medical_record_list_create'),
    path('medical-records/<int:pk>/', MedicalRecordRetrieveUpdateDestroyView.as_view(), name='medical_record_retrieve_update_destroy'),
    
    # Insurance URLs
    path('insurance/', InsuranceListCreateView.as_view(), name='insurance_list_create'),
    path('insurance/<int:pk>/', InsuranceRetrieveUpdateDestroyView.as_view(), name='insurance_retrieve_update_destroy'),
    
    # Payment URLs
    path('payments/', PaymentListCreateView.as_view(), name='payment_list_create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment_retrieve_update_destroy'),
    
    # Test Result URLs
    path('test-results/', TestResultListCreateView.as_view(), name='test_result_list_create'),
    path('test-results/<int:pk>/', TestResultRetrieveUpdateDestroyView.as_view(), name='test_result_retrieve_update_destroy'),
    
    # Referral URLs
    path('referrals/', ReferralListCreateView.as_view(), name='referral_list_create'),
    path('referrals/<int:pk>/', ReferralRetrieveUpdateDestroyView.as_view(), name='referral_retrieve_update_destroy'),
    
    # Allergy URLs
    path('allergies/', AllergyListCreateView.as_view(), name='allergy_list_create'),
    path('allergies/<int:pk>/', AllergyRetrieveUpdateDestroyView.as_view(), name='allergy_retrieve_update_destroy'),
]
