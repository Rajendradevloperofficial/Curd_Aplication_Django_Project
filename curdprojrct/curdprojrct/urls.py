from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="addshow"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
    path('update/<int:id>/',views.update,name="updatedata"),
    path('api/',include('app.api.urls'))
]
