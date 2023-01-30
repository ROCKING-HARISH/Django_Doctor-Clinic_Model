# Django_Doctor-Clinic_Model

hello evryone

I have created an user_account as harish.

Admin login credential:

user name: harish
password : HARISH

Have populated the database with 3 Clinic and 15 Doctor random data with 5 Doctors in each Clinic. 

Doctor specialities used :      Neurologist
                                Cardiologist
                                Gynaecologist

PageNumberPagination:
    page_size = 2
    
    
You can use the following dynamic URLs:

doctors/clinic/<int:clinic_id>/

doctors/clinic/<int:clinic_id>/speciality/<str:speciality>/

doctors/clinic/<int:clinic_id>/speciality/<str:speciality>/timing/
