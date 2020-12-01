from django.urls import path
from . import views

urlpatterns = [
	path('', views.hello, name = 'hello'),
	path('validate_finite_values_entity', views.validate_finite_values_entity, name = 'validate_finite_values_entity'),
	path('validate_numeric_entity', views.validate_numeric_entity, name = 'validate_numeric_entity')

]