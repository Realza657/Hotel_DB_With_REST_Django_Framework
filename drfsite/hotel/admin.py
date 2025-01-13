from django.contrib import admin

from .models import OrderOfEmployment, Employee, Position, Schedule, Visit, Award, EmployeeAuthorization, \
    NeedsByPosition, Agreement, Client, ClientAuthorization, ServiceAccount, AccountAccommodation, ListOfServices, \
    Service, Room, RoomType

admin.site.register(OrderOfEmployment)
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Schedule)
admin.site.register(Visit)
admin.site.register(Award)
admin.site.register(EmployeeAuthorization)
admin.site.register(NeedsByPosition)
admin.site.register(Agreement)
admin.site.register(Client)
admin.site.register(ClientAuthorization)
admin.site.register(ServiceAccount)
admin.site.register(AccountAccommodation)
admin.site.register(ListOfServices)
admin.site.register(Service)
admin.site.register(Room)
admin.site.register(RoomType)