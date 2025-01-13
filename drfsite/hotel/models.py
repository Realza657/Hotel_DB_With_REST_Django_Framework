from django.db import models

# Приказ о зачислении на работу
class OrderOfEmployment(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)  # Должность (внешний ключ)
    date_hired = models.DateField()  # Дата приема на работу
    date_fired = models.DateField(null=True, blank=True)  # Дата увольнения (может быть пустой)

    def __str__(self):
        return f"Order #{self.id} - {self.employee}"

# Сотрудник
class Employee(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    full_name = models.CharField(max_length=255)  # ФИО
    position = models.ForeignKey('Position', on_delete=models.CASCADE)  # Должность (внешний ключ)

    def __str__(self):
        return self.full_name
# Должность
class Position(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    name = models.CharField(max_length=255)  # Название должности
    staff = models.IntegerField()  # Штат (число сотрудников на должности)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Оклад (с плавающей точкой)

    def __str__(self):
        return self.name
# График работ
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    start_date = models.DateField()  # Дата начала работы
    end_date = models.DateField()  # Дата конца работы

    def __str__(self):
        return f"Schedule #{self.id} - {self.employee}"

# Фиксация посещений
class Visit(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    date = models.DateField()  # Дата посещения
    arrived = models.BooleanField()  # Пришел (булево значение)
    start_hour = models.IntegerField()  # Часы начала
    end_hour = models.IntegerField()  # Часы конца

    def __str__(self):
        return f"Visit #{self.id} - {self.employee} on {self.date}"

# Премии сотрудникам
class Award(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)  # Премия (с плавающей точкой)

    def __str__(self):
        return f"Award #{self.id} - {self.employee} ({self.bonus} ₽)"

# Авторизация сотрудников
class EmployeeAuthorization(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    login = models.CharField(max_length=150, unique=True)  # Логин
    password = models.CharField(max_length=128)  # Пароль

    def __str__(self):
        return f"Authorization for {self.employee}"

# Нужды по должностям
class NeedsByPosition(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    position = models.ForeignKey('Position', on_delete=models.CASCADE)  # Должность (внешний ключ)
    quantity = models.IntegerField()  # Количество

    def __str__(self):
        return f"Needs for {self.position} - {self.quantity} required"

# Договор о проживании
class Agreement(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # Клиент (внешний ключ)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    check_in_date = models.DateField()  # Дата заселения
    check_out_date = models.DateField()  # Дата выселения
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Итоговая сумма

    def __str__(self):
        return f"Agreement #{self.id} - Client: {self.client}, Total: {self.total} ₽"

# Клиент
class Client(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    full_name = models.CharField(max_length=255)  # ФИО клиента

    def __str__(self):
        return self.full_name

# Авторизация клиента
class ClientAuthorization(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    client = models.ForeignKey('Client', on_delete=models.CASCADE)  # Клиент (внешний ключ)
    login = models.CharField(max_length=150, unique=True)  # Логин
    password = models.CharField(max_length=128)  # Пароль

    def __str__(self):
        return f"Authorization for {self.client}"

# Счет услуг
class ServiceAccount(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE)  # Договор (внешний ключ)
    amount = models.IntegerField()  # Сумма

    def __str__(self):
        return f"Service Account #{self.id} - Agreement: {self.agreement}, Amount: {self.amount} ₽"

# Счет за проживание
class AccountAccommodation(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE)  # Договор (внешний ключ)
    number = models.ForeignKey('Room', on_delete=models.CASCADE)  # Номер (внешний ключ)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма (с плавающей точкой)

    def __str__(self):
        return f"Account for Accommodation #{self.id} - Agreement: {self.agreement}, Room: {self.number}, Amount: {self.amount} ₽"

# Список услуг
class ListOfServices(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    service_account = models.ForeignKey('ServiceAccount', on_delete=models.CASCADE)  # Счет услуг (внешний ключ)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Сотрудник (внешний ключ)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)  # Услуга (внешний ключ)

    def __str__(self):
        return f"Service #{self.id} - Account: {self.service_account}, Employee: {self.employee}, Service: {self.service}"

# Услуга
class Service(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    name = models.CharField(max_length=255)  # Название услуги
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость (с плавающей точкой)

    def __str__(self):
        return f"Service: {self.name} - Price: {self.price} ₽"

# Номер
class Room(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)  # Вид номера (внешний ключ)
    surcharges = models.DecimalField(max_digits=10, decimal_places=2)  # Надбавки (с плавающей точкой)

    def __str__(self):
        return f"Room #{self.id} - Type: {self.room_type}, Surcharges: {self.surcharges} ₽"

# Вид номера
class RoomType(models.Model):
    id = models.AutoField(primary_key=True)  # ID с автоинкрементом
    name = models.CharField(max_length=255)  # Наименование (тип номера)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость (с плавающей точкой)
    quantity = models.IntegerField()  # Количество (целое число)

    def __str__(self):
        return f"RoomType: {self.name} - Price: {self.price} ₽ - Quantity: {self.quantity}"