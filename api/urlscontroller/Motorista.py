from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse

from api.models import Motorista

from api.serializers import MotoristaSerializer

class MotoristaDao():
    def __init__(self,request):
        self.request_data = request
    def motoristaGet(self):
        motorista = Motorista.objects.all()
        motorista_serializer= MotoristaSerializer(motorista,many=True)
        return JsonResponse(motorista_serializer.data,safe=False)
    def motoristaPost(self):
        motorista_data = JSONParser().parse(self.request_data)
        motorista_serializer = MotoristaSerializer(data=motorista_data)
        if motorista_serializer.is_valid():
            motorista_serializer.save()
            return JsonResponse("Added SucessFully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    def motoristaPut(self):
        motorista_data = JSONParser().parse(self.request_data)
        motorista = Motorista.objects.get(Cod_Motorista=motorista_data['Cod_Motorista'])
        motorista_serializer = MotoristaSerializer(motorista,data=motorista_data)
        if motorista_serializer.is_valid():
            motorista_serializer.save()
            return JsonResponse("Update SucessFully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    def motoristaDelete(self):
        motorista_data = JSONParser().parse(self.request_data)
        motorista=Motorista.objects.get(Cod_Motorista=motorista_data['Cod_Motorista'])
        motorista.delete()
        return JsonResponse("Deleted SucessFully",safe=False)
