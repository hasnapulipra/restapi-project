from django.urls import path
from . import views
urlpatterns = [
    
    path('add-staff',views.add_staff),
    path('load-staff',views.load_staff),
    path('add-doctor',views.add_doctor),
    path('load-doctor',views.load_doctor),
    path('add-patient',views.add_patient),
    path('load-patient',views.load_patient),
    path('delete-doctor/<int:id>',views.delete_doctor),
    path('delete-patient/<int:id>',views.delete_patient),
    path('update-doctor/<int:id>',views.update_doctor),
    path('update-patient/<int:id>',views.update_patient),
    path('search-doctor',views.search_doctor),
    path('search-patient',views.search_patient),
    path('auth-checkdoctor',views.auth_doctor),
    path('auth-checkpatient',views.auth_patient),
    path('load-singledoctor/<int:id>',views.load_singledoctor),
    path('load-singlepatient/<int:id>',views.load_singlepatient),


    
]
