from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser

from .serializers import NumAct , SaveActsSerializer
from .utils import append_date,createAct,append_files

from .serializers import Firm , Acts,CreateAct,EmplSe

from .models import Firms , Cact719,Empl

class UpdateDocxAPIView(APIView):

    def post(self, request, format=None):
        #MySQl

        numbact = request.data.get('numbact')
        print(numbact)
        # Поиск объекта Cact719
        try:
            existing_object = Cact719.objects.get(numbact=numbact)
        except Cact719.DoesNotExist:
            return JsonResponse({'error': 'Объект не найден'}, status=404)

        # Создание экземпляра сериализатора с существующим объектом и данными из запроса
        serializer = SaveActsSerializer(existing_object, data=request.data)

        #Файловая часть
        # Проверка валидности и сохранение изменений
        if serializer.is_valid():
            numAct = serializer.validated_data['numbact']
            kpp = serializer.validated_data['custexp_kpp']
            inn = serializer.validated_data['custexp_inn']
            nameZaivitel = serializer.validated_data['custexp_namef']
            adress = serializer.validated_data['custexp_addr']
            OGRN = serializer.validated_data['custexp_ogrn']
            adreesPlaceProizvod = serializer.validated_data['custexp_addr_pa']


            # Генерирование docx-файла
            append_date(numAct, kpp, inn, nameZaivitel, adress, OGRN,adreesPlaceProizvod)

            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)












        #return Response(serializer_save.errors, status=400)


def GetSereliazerNum(request):
    serializer = NumAct(data=request.data)
    if serializer.is_valid():
        number = serializer.validated_data['number']
        return serializer, number  # Возврат сериализатора и числа
    else:
        return None, None  # Возврат None, если сериализатор не валиден




class openDocxAPI(APIView):
    def post(self, request):
        numbact = request.data.get('numbact')
        file_path =  f'C:/Users/Нур/PycharmProjects/CreaterDocx/creater/docxer/acts/{numbact}/docxDA.docx'
        file = open(file_path, 'rb')
        response = FileResponse(file, as_attachment=True)
        return response


class Create_New_Act(APIView):
    def post(self,request):
        serializer = CreateAct(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        numAct = serializer.validated_data['numbact']

        createAct(numAct)
        serializer.save()
        return Response(serializer.data)


class UploadFiles(APIView):
    parser_classes = (MultiPartParser,)

    def post(self,request):
        TableDa = request.FILES['TableDA']
        numbact = request.data.get('numbact')

        print(request.data.get('TableDA'))
        print(request.data.get('numbact'))

        try:
            append_files(numbact,TableDa)
            return Response({'message': 'Файл успешно загружен и сохранен'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)








class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firms.objects.all()
    serializer_class = Firm

class ActViewSet(viewsets.ModelViewSet):
    queryset = Cact719.objects.all()
    serializer_class = Acts

class EmplViewSet(viewsets.ModelViewSet):
    queryset = Empl.objects.all()
    serializer_class = EmplSe