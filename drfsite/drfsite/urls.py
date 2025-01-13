"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sys import implementation

from django.contrib import admin
from django.urls import path, include

from hotel.views import EmployeeViewSet, PositionViewSet, OrderOfEmploymentViewSet, ScheduleViewSet, VisitViewSet, \
    AwardViewSet, EmployeeAuthorizationViewSet, NeedsByPositionViewSet, AgreementViewSet, ClientViewSet, \
    ClientAuthorizationViewSet, ServiceAccountViewSet, AccountAccommodationViewSet, ListOfServicesViewSet, \
    ServiceViewSet, RoomViewSet, RoomTypeViewSet, CustomQueryView
from rest_framework import routers

router = routers.DefaultRouter() # роутер объединяющий вьюсеты разных типов запросов

# CRUD hotel_Tables
router.register(r'employee', EmployeeViewSet) # http://127.0.0.1:8000/api/v1/employee
router.register(r'position', PositionViewSet) # http://127.0.0.1:8000/api/v1/position
router.register(r'orderofemployment', OrderOfEmploymentViewSet) # http://127.0.0.1:8000/api/v1/orderofemployment
router.register(r'schedule', ScheduleViewSet) # http://127.0.0.1:8000/api/v1/schedule
router.register(r'visit', VisitViewSet) # http://127.0.0.1:8000/api/v1/visit
router.register(r'award', AwardViewSet) # http://127.0.0.1:8000/api/v1/award
router.register(r'employeeauthorization', EmployeeAuthorizationViewSet) # http://127.0.0.1:8000/api/v1/employeeauthorization
router.register(r'needsbyposition', NeedsByPositionViewSet) # http://127.0.0.1:8000/api/v1/needsbyposition
router.register(r'agreement', AgreementViewSet) # http://127.0.0.1:8000/api/v1/agreement
router.register(r'client', ClientViewSet) # http://127.0.0.1:8000/api/v1/client
router.register(r'clientauthorization', ClientAuthorizationViewSet) # http://127.0.0.1:8000/api/v1/clientauthorization
router.register(r'serviceaccount', ServiceAccountViewSet) # http://127.0.0.1:8000/api/v1/serviceaccount
router.register(r'accountaccommodation', AccountAccommodationViewSet) # http://127.0.0.1:8000/api/v1/accountaccommodation
router.register(r'listofservices', ListOfServicesViewSet) # http://127.0.0.1:8000/api/v1/listofservices
router.register(r'service', ServiceViewSet) # http://127.0.0.1:8000/api/v1/service
router.register(r'room', RoomViewSet) # http://127.0.0.1:8000/api/v1/room
router.register(r'roomtype', RoomTypeViewSet) # http://127.0.0.1:8000/api/v1/roomtype

# SQL-Requests mechanism
# Request URL: http://127.0.0.1:8000/api/v1/custom-query/NAME-OF-SQL-REQUEST
# Type of Request - POST
# Body (raw) : {
#     "query_name": "request_name"
#     // "params": [...] if we need ones
# }

# SQL-Requests
# update_accommodation_account(agreement_id[num])
# update_agreement_total(id[num])
# add_service_account_amount(agreement_id[num])
# get_employees_with_high_awards()
# get_total_by_client(client_id[num])
# get_employees_by_date_range(start_date_1[str_date], start_date_2[str_date], end_date_1[str_date], end_date_2[str_date]) form of date: YYYY-MM-DD
# count_rooms_below_price()
# get_most_frequent_client()
# get_fired_employees()
# update_needs_by_position(position_id[num])
# get_current_guests()
# get_top_3_highest_paid_employees()

urlpatterns = [
    path('admin/', admin.site.urls), # админка root 1234 http://127.0.0.1:8000/admin
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/*nameOfObject (get, post) or +/index/ (patch or put to one with index position)
    path('api/v1/custom-query/', CustomQueryView.as_view()), # http://127.0.0.1:8000/api/v1/custom-query
    # path('api/v1/employeelist/', EmployeeViewSet.as_view({'get':'list'})),
    # path('api/v1/employeelist/<int:pk>/', EmployeeViewSet.as_view({'put': 'update'})),
]
