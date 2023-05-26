from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        username = validated_data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'A user with that username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Patient.objects.get(pk=self.kwargs['pk'], user=self.request.user)
        except Patient.DoesNotExist:
            raise NotFound()

class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoctorRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Doctor.objects.get(pk=self.kwargs['pk'], user=self.request.user)
        except Doctor.DoesNotExist:
            raise NotFound()

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.all()

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class AppointmentRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Appointment.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Appointment.DoesNotExist:
            raise NotFound()

class PrescriptionListCreateView(generics.ListCreateAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prescription.objects.all()

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class PrescriptionRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Prescription.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Prescription.DoesNotExist:
            raise NotFound()

class MedicalRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicalRecord.objects.all()

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class MedicalRecordRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return MedicalRecord.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except MedicalRecord.DoesNotExist:
            raise NotFound()

class InsuranceListCreateView(generics.ListCreateAPIView):
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Insurance.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class InsuranceRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Insurance.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Insurance.DoesNotExist:
            raise NotFound()

class PaymentListCreateView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class PaymentRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Payment.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Payment.DoesNotExist:
            raise NotFound()
        
class TestResultListCreateView(generics.ListCreateAPIView):
    serializer_class = TestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TestResult.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class TestResultRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return TestResult.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except TestResult.DoesNotExist:
            raise NotFound()

class ReferralListCreateView(generics.ListCreateAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Referral.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class ReferralRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Referral.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Referral.DoesNotExist:
            raise NotFound()

class AllergyListCreateView(generics.ListCreateAPIView):
    serializer_class = AllergySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Allergy.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class AllergyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AllergySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Allergy.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Allergy.DoesNotExist:
            raise NotFound()

class ImmunizationListCreateView(generics.ListCreateAPIView):
    serializer_class = ImmunizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Immunization.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class ImmunizationRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImmunizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Immunization.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except Immunization.DoesNotExist:
            raise NotFound()

class FamilyHistoryListCreateView(generics.ListCreateAPIView):
    serializer_class = FamilyHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FamilyHistory.objects.filter(patient__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient__user=self.request.user)

class FamilyHistoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FamilyHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return FamilyHistory.objects.get(pk=self.kwargs['pk'], patient__user=self.request.user)
        except FamilyHistory.DoesNotExist:
            raise NotFound()
        
