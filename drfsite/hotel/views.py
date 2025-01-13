from logging import exception

from django.core.serializers import serialize
from django.db import connection
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee, Position, OrderOfEmployment, Schedule, Visit, Award, EmployeeAuthorization, \
    NeedsByPosition, Agreement, Client, ClientAuthorization, ServiceAccount, AccountAccommodation, ListOfServices, \
    Service, Room, RoomType
from .queries import ALLOWED_QUERIES
from .serializers import EmployeeSerializer, PositionSerializer, OrderOfEmploymentSerializer, ScheduleSerializer, \
    VisitSerializer, AwardSerializer, EmployeeAuthorizationSerializer, NeedsByPositionSerializer, AgreementSerializer, \
    ClientSerializer, ClientAuthorizationSerializer, ServiceAccountSerializer, AccountAccommodationSerializer, \
    ListOfServicesSerializer, ServiceSerializer, RoomSerializer, RoomTypeSerializer


# Представление для модели Сотрудник
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Представление для модели Должность
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

# Представление для модели Приказ
class OrderOfEmploymentViewSet(viewsets.ModelViewSet):
    queryset = OrderOfEmployment.objects.all()
    serializer_class = OrderOfEmploymentSerializer

# Представление для модели График работ
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# Представление для модели Фиксация посещений
class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

# Представление для модели Премии сотрудникам
class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

# Представление для модели Авторизация сотрудников
class EmployeeAuthorizationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAuthorization.objects.all()
    serializer_class = EmployeeAuthorizationSerializer

# Представление для модели Вакансии
class NeedsByPositionViewSet(viewsets.ModelViewSet):
    queryset = NeedsByPosition.objects.all()
    serializer_class = NeedsByPositionSerializer

# Представление для модели Договор о проживании
class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

# Представление для модели Клиент
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Представление для модели Авторизация клиента
class ClientAuthorizationViewSet(viewsets.ModelViewSet):
    queryset = ClientAuthorization.objects.all()
    serializer_class = ClientAuthorizationSerializer

# Представление для модели Счет услуг
class ServiceAccountViewSet(viewsets.ModelViewSet):
    queryset = ServiceAccount.objects.all()
    serializer_class = ServiceAccountSerializer

# Представление для модели Счет за проживание
class AccountAccommodationViewSet(viewsets.ModelViewSet):
    queryset = AccountAccommodation.objects.all()
    serializer_class = AccountAccommodationSerializer

# Представление для модели Список услуг
class ListOfServicesViewSet(viewsets.ModelViewSet):
    queryset = ListOfServices.objects.all()
    serializer_class = ListOfServicesSerializer

# Представление для модели Услуга
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Представление для модели Номер
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# Представление для модели Вид номера
class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

# SQL запросы
class CustomQueryView(APIView):
    def post(self, request, *args, **kwargs):
        query_name = request.data.get("query_name")
        params = request.data.get("params", [])

        # Если params = None, заменяем на пустой список
        if params is None:
            params = []

        # Проверка разрешенных запросов
        if query_name not in ALLOWED_QUERIES:
            return Response({"error": f"Query '{query_name}' not allowed"})

        query = ALLOWED_QUERIES[query_name]

        # Запрос к базе данных
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                # Если запрос типа SELECT
                if query.strip().upper().startswith("SELECT"):
                    columns = [col[0] for col in cursor.description]
                    rows = cursor.fetchall()
                    result = [dict(zip(columns, row)) for row in rows]
                    return Response({"success": True, "data": result})
                else:
                    return Response({"success": True, "message": "Query executed successfully"})
        except Exception as e:
            return Response({"error": str(e)})

# class EmployeeAPIList(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeAPIUpdate(generics.UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeAPIView(APIView):
#     def get(self, request):
#         lst = Employee.objects.all()
#         print(EmployeeSerializer(lst, many=True).data)
#         return Response({'posts': EmployeeSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#
#     def patch(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error: Method PATCH is not allowed"})
#         try:
#             instance = Employee.objects.get(pk=pk)
#         except:
#             return Response({"error: Object does not exist"})
#         serializer = EmployeeSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error: Method DELETE is not allowed"})
#         try:
#             instance = Employee.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error: Object does not exist"})
#         return Response({"post": "deleted record: " + str(pk)})