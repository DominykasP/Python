from django.urls import path

from . import views

app_name = 'pvm_forms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:form_id>/', views.form_detail, name="form_detail"),
    path('<int:form_id>/raw_table', views.raw_table, name="raw_table"),
    path('<int:form_id>/pdf', views.form_pdf, name="form_pdf")
]
