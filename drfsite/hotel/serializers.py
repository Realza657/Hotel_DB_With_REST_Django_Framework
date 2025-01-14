from rest_framework import serializers
from .models import Employee, Position, OrderOfEmployment, Schedule, Visit, Award, EmployeeAuthorization, \
    NeedsByPosition, Agreement, Client, ClientAuthorization, ServiceAccount, AccountAccommodation, ListOfServices, \
    Service, Room, RoomType

# Сериалайзер объектов модели Сотрудник
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

# Сериалайзер объектов модели Должность
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

# Сериалайзер объектов модели Приказ
class OrderOfEmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOfEmployment
        fields = "__all__"

# Сериалайзер объектов модели График работ
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"

# Сериалайзер объектов модели Фиксация посещений
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"

# Сериалайзер объектов модели Премии сотрудникам
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"

# Сериалайзер объектов модели Авторизация сотрудников
class EmployeeAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAuthorization
        fields = "__all__"

# Сериалайзер объектов модели Вакансии
class NeedsByPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedsByPosition
        fields = "__all__"

# Сериалайзер объектов модели Договор о проживании
class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"

# Сериалайзер объектов модели Клиент
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

# Сериалайзер объектов модели Авторизация клиента
class ClientAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAuthorization
        fields = "__all__"

# Сериалайзер объектов модели Счет услуг
class ServiceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAccount
        fields = "__all__"

# Сериалайзер объектов модели Счет за проживание
class AccountAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountAccommodation
        fields = "__all__"

# Сериалайзер объектов модели Список услуг
class ListOfServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfServices
        fields = "__all__"

# Сериалайзер объектов модели Услуга
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

# Сериалайзер объектов модели Номер
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

# Сериалайзер объектов модели Вид номера
class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"
