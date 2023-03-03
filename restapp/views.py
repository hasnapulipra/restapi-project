from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

@api_view(['POST'])
def add_staff(request):
    params=request.data
    statusCode=0

    name = params['name'] 
    username = params['username'] 
    password = params['password'] 
    dob = params['dob'] 
    email = params['email']

    try:
        exist = Staff.objects.filter(email = email).exists()

        if not exist :


            staff = StaffSerializer(data = params)

            if staff.is_valid():

                staff.save()

                statusCode= 200
        else : 
            statusCode = 409

    except Exception as e:
        print(e)

        statusCode=401  
    
    return Response({'statusCode':statusCode})


@api_view(['GET'])
def load_staff(request):
    
    staff=Staff.objects.all()
    ser=StaffSerializer(staff,many=True)
    return Response(ser.data)


@api_view(['POST'])
def add_doctor(request):
    params = request.data
    statusCode = 0

    name = params['name']
    username = params['username']
    password = params['password']
    age = params['age']
    gender = params['gender']
    specialization = params['specialization']
    experience = params['experience']
    language = params['language']
    contact = params['contact']
    email = params['email']
    schedule = params['schedule']
    

    try:
        exist = Doctor.objects.filter(email=email).exists()

        if not exist:
            doctor = DoctorSerializer(data=params)
            if doctor.is_valid():
                doctor.save()
                statusCode = 200

        else:
            statusCode = 409
        
    except Exception as e:
        print(e)
        statusCode = 401

    return Response({'statusCode':statusCode})


@api_view(['GET'])
def load_doctor(request):
    doctor = Doctor.objects.all()
    ser = DoctorSerializer(doctor,many=True)
    return Response(ser.data)


@api_view(['POST'])
def add_patient(request):
    params = request.data
    statusCode = 0

    fullname = params['fullname']
    username = params['username']
    password = params['password']
    email = params['email']
    contact = params['contact']
    address = params['address']
    dob = params['dob']
    age = params['age']
    bgroup = params['bgroup']
    gender = params['gender']

    try: 
        exist = Patient.objects.filter(email=email).exists()

        if not exist:
            patient = PatientSerializer(data=params)
            
            if patient.is_valid():
                patient.save()
                statusCode = 200

        else:
            statusCode = 409

    except Exception as e:
        print(e)
        statusCode = 401

    return Response({'statusCode':statusCode})


@api_view(['GET'])
def load_patient(request):
    patient = Patient.objects.all()
    ser = PatientSerializer(patient,many=True)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_doctor(request,id):
    statusCode = 0

    try:
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        statusCode = 200

    except:
        statusCode = 409
        pass

    return Response({'statusCode':statusCode})





@api_view(['DELETE'])
def delete_patient(request):
    statusCode = 0

    try:
        patient = Patient.objects.get(id=id)
        patient.delete()
        statusCode = 200

    except:
        statusCode = 409
        pass

    return Response({'statusCode':statusCode})





@api_view(['PUT'])
def update_doctor(request,id):
    statusCode = 0
    params = request.data

    try:
        doctor = Doctor.objects.get(id=id)
        ser = DoctorSerializer(doctor,data=params,partial=True)
        if ser.is_valid():
            ser.save()
            statusCode = 200

        else:
            pass

    except Exception as e:
        print(e)
        statusCode = 409
        pass

    return Response({'statusCode':statusCode})



@api_view(['PUT'])
def update_patient(request,id):
    statusCode = 0
    params = request.data

    try:
        patient = Patient.objects.get(id=id)
        ser = PatientSerializer(patient,data=params,partial=True)
        if ser.is_valid():
            ser.save()
            statusCode = 200

        else:
            pass

    except Exception as e:
        print(e)
        statusCode = 409
        pass

    return Response({'statusCode':statusCode})



@api_view(['GET'])
def search_doctor(request):
    params = request.data
    search_text = params['name']

    doctor=Doctor.objects.filter(name__icontains = search_text)
    ser=DoctorSerializer(doctor,many=True)
    return Response(ser.data)



@api_view(['GET'])
def search_patient(request):
    search_text = request.GET['fullname']
    patient = Patient.objects.filter(fullname__icontains = search_text)
    ser = PatientSerializer(patient,many=True)
    return Response(ser.data)


@api_view(['GET'])
def auth_doctor(request):
    statusCode = 0
    params = request.data
    username = params['username']
    passwd = params['password']

    try:
        doctor = Doctor.objects.get(username=username,password=passwd)
        statusCode = 200

    except:
        statusCode = 401

    return Response({'statusCode':statusCode})



@api_view(['GET'])
def auth_patient(request):
    statusCode = 0
    params = request.data
    username = params['username']
    password = params['password']
    try:
        patient = Patient.objects.get(username = username , password = password)
        statusCode = 200
    except:
        statusCode = 401
    return Response({'statusCode':statusCode})





@api_view(['GET'])
def load_singledoctor(request,id):
    statusCode = 0
    try:
        doctor = Doctor.objects.get(id=id)
        ser = DoctorSerializer(doctor)
        return Response(ser.data)
    
    except Exception as e:
        print(e)
        statusCode = 409
        return Response({'statusCode':statusCode})




@api_view(['GET'])
def load_singlepatient(request,id):
    statusCode = 0
    try:
        patient = Patient.objects.get(id = id)
        ser = PatientSerializer(patient)
        return Response(ser.data)
    
    except Exception as e:
        print(e)
        statusCode = 409
        return Response({'statusCode':statusCode})