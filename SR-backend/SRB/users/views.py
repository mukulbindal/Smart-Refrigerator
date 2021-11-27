from django.shortcuts import render
import json
from .models import Refrigerator, User
from django.http import JsonResponse
import bcrypt
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
import string
import random

# Initial Setup (Not to be used in Production) ** Begin
for IP_col_4 in range(50):
    try:
        r = Refrigerator(FID="RF-10{}".format("%02d"%IP_col_4), IP="192.168.1."+str(IP_col_4))
        r.save()
    except:
        print("Exception bypassed in creating refrigerator")
# Initial Setup (Not to be used in Production) ** End

def generate_token(N=20):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


# Expects UID and password
@csrf_exempt
def login(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            UID = data['UID']
            user = User.objects.filter(UID=UID)
            password = data['password']
            password = password.encode('utf-8')
            if not user:
                response = {'Error': 'User not found'}
                return JsonResponse(response, status=404)
            user = user[0]
            if not bcrypt.checkpw(password, user.password.encode('utf-8')):
                response = {'Error': 'User not found'}
                return JsonResponse(response, status=404)
            user.token = generate_token()
            user.save()
            return JsonResponse({'Login': 'OK', 'token': user.token, 'UID': UID, 'Uname':user.UNAME, 'CamIP':user.FID.IP})
    except Exception as e:
        print(e)
        return JsonResponse({'Error': 'Something went wrong!'}, status=404)


# Generates a new User ID
def generate_uid():
    maxUid = User.objects.aggregate(Max('UID'))['UID__max'][3:]
    maxUid = int(maxUid)
    if not maxUid:
        maxUid = 0
    return "US-" + "%04d"%(maxUid+1)


def hash_password(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode('utf-8')


# Expects UNAME, PASSWORD, FID
@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            print(request)
            print(data)
            UID = generate_uid()
            try:
                FID = Refrigerator.objects.filter(FID=data['FID'])[0]
            except Exception as e:
                return JsonResponse({'Error': 'FID is invalid'}, status=500)
            user = User(UID=UID, password=hash_password(data['password']), UNAME=data['UNAME'], FID=FID)
            user.save()
            return JsonResponse({'Success': {'UID': UID}})
        else:
            return JsonResponse({'Error': 'Else block Executed'}, status=500)
    except Exception as e:
        print("Here", e)
        return JsonResponse({'Error': e}, status=500)


@csrf_exempt
def logout(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            UID = data['UID']
            user = User.objects.filter(UID=UID)
            if not user:
                response = {'Error': 'User not found'}
                return JsonResponse(response)
            user.token = ""
            user.save()
            return JsonResponse({'Logout': 'Ok'})
    except Exception as e:
        print(e)
        return JsonResponse({"Error": 'Something went wrong'})
