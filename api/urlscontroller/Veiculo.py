from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse

from api.models import Veiculo

from api.serializers import VeiculoSerializer

class VeiculoDao():
    def __init__(self,request):
        self.request = request
    def veiculoGet(self):
        veiculo = Veiculo.objects.all()
        veiculo_serializer = VeiculoSerializer(veiculo,many=True)
        return JsonResponse(veiculo_serializer.data,safe=False)
    def veiculoPost(self):
        veiculo_data = JSONParser().parse(self.request)
        veiculo_serializer= VeiculoSerializer(data=veiculo_data)
        if veiculo_serializer.is_valid():
            veiculo_serializer.save()
            return JsonResponse("Added SucessFully",safe=False)
        return JsonResponse("Failed to Add")
    def veiculoPut(self):
        veiculo_data = JSONParser().parse(self.request)
        veiculo = Veiculo.objects.get(Placa=veiculo_data['Placa']) 
        veiculo_serializer = VeiculoSerializer(veiculo,data=veiculo_data)
        if veiculo_serializer.is_valid():
            veiculo_serializer.save()
            return JsonResponse("Update SucessFully",safe=False)
        return JsonResponse("Update Failed")
    def veiculoDelete(self):
        veiculo_data = JSONParser().parse(self.request)
        veiculo = Veiculo.objects.get(Placa=veiculo_data['Placa'])
        veiculo.delete()
        return JsonResponse('Deleted SucessFully',safe=False)