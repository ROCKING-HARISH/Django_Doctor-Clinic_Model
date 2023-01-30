# Django_Doctor-Clinic_Model

Hello Everyone,

I have created an user_account as harish.

Admin login credential:

user name: harish
password : HARISH

Have created 2 module class called Doctor and Clinic with one to many relationship with a ForeignKey in Doctor using Clinic as (Clinic, on_delete=models.CASCADE)


Have populated the database with 3 Clinic and 15 Doctor random data with 5 Doctors in each Clinic. 

Doctor specialities used :      Neurologist
                                Cardiologist
                                Gynaecologist

PageNumberPagination:
    page_size = 2
    
Have used ModelSerializer for the field in Doctor class in serializer.DoctorSerializer
    
    
Created 3 api endpoints to get following details using Filtering queryset: 


1) fetch all doctors working for given clinic by clinic id, use pagination
send 2 doctors data in each query.


2) fetch all doctors for given clinic by clinic id and by their speciality, use
pagination send 2 doctors data in each query.


3) fetch all doctors for given clinic by clinic id and their speciality who
are attending patients between 4PM to 8PM


    
You can use the following dynamic URLs(used Kwargs):

doctors/clinic/<int:clinic_id>/

doctors/clinic/<int:clinic_id>/speciality/<str:speciality>/

doctors/clinic/<int:clinic_id>/speciality/<str:speciality>/timing/
