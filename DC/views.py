from django.shortcuts import render
from .models import Doctor
from .serializer import DoctorSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class DoctorListPagination(PageNumberPagination):
    page_size = 2

class DoctorListByClinicIdView(generics.ListAPIView):
    pagination_class = DoctorListPagination
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_queryset(self):
        clinic_id = self.kwargs['clinic_id']
        return self.queryset.filter(clinic_id=clinic_id)

class DoctorListByClinicIdAndSpecialityView(generics.ListAPIView):
    pagination_class = DoctorListPagination
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_queryset(self):
        clinic_id = self.kwargs['clinic_id']
        speciality = self.kwargs['speciality']
        return self.queryset.filter(clinic_id=clinic_id, speciality=speciality)

class DoctorListByClinicIdAndSpecialityAndTimingView(generics.ListAPIView):
    pagination_class = DoctorListPagination
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_queryset(self):
        clinic_id = self.kwargs['clinic_id']
        speciality = self.kwargs['speciality']
        return self.queryset.filter(
            clinic_id=clinic_id,
            speciality=speciality,
            starttime__lte='20:00:00',
            endtime__gte='16:00:00'
        )