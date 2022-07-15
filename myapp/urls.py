from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.useradd.as_view(), name='add-show'),
    path('delete/<int:id>/', views.deletedata.as_view(), name="delete-data"),
    path('<int:id>/', views.userupdate.as_view(), name="update-data"),
    # path('<int:id>/', views.update_data, name="update-data"),
]
