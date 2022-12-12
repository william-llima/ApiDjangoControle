from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from api.urlscontroller.Motorista import MotoristaDao
from api.urlscontroller.Veiculo import VeiculoDao

from api.models import Veiculo,Controle

from api.serializers import MotoristaSerializer,VeiculoSerializer,ControleSerializer

# Create your views here.
@csrf_exempt
def RestApiMotorista(request):
    MotoristaClass=MotoristaDao(request)
    if request.method=="GET":
        return MotoristaClass.motoristaGet()
     
    elif request.method=="POST":
        return MotoristaClass.motoristaPost()

    elif request.method =="PUT":
        return MotoristaClass.motoristaPut()
    elif request.method == 'DELETE':
       return MotoristaClass.motoristaDelete()
    else:
        return JsonResponse("Invalid request",safe=False)

@csrf_exempt
def RestApiVeiculo(request,id=0):
    veiculoClass= VeiculoDao(request)
    if request.method=="GET":
       return veiculoClass.veiculoGet()
    if request.method == "POST":
        return veiculoClass.veiculoPost()
    if request.method == "PUT":
        return veiculoClass.veiculoPut()
    if request.method == "DELETE":
        return veiculoClass.veiculoDelete()
    else:
        return JsonResponse("Invalid request",safe=False)

@csrf_exempt
def RestApiControle(request,id=0):
    if request.method == "GET":
       controle = Controle.objects.all()
       controle_serializer = ControleSerializer(controle,many=True)
       return JsonResponse(controle_serializer.data,safe=False)
    if request.method == "POST":
       controle_data = JSONParser().parse(request)
       controle_serializer =  ControleSerializer(data=controle_data)
       if controle_serializer.is_valid():
          controle_serializer.save()
          return JsonResponse("Added SucessFully",safe=False)
       print(controle_serializer.errors)
       return JsonResponse("Failed to Add",safe=False)
    if request.method == "PUT":
       controle_data = JSONParser().parse(request)
       controle      = Controle.objects.get(controle_ID=controle_data['controle_ID'])
       controle_serializer = ControleSerializer(controle,data=controle_data)
       if controle_serializer.is_valid():
            controle_serializer.save()
            return JsonResponse("Update SucessFully",safe=False)              
       return JsonResponse("Failed to Update",safe=False)
    if request.method == 'DELETE':
        controle_data = JSONParser().parse(request)
        controle = Controle.objects.get(controle_ID=controle_data['controle_ID'])
        controle.delete()
        return JsonResponse("Deleted SucessFully",safe=False)
    else:
        return JsonResponse("Invalid request",safe=False)





