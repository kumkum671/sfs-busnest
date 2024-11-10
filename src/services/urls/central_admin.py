from django.urls import path
from core import views
from services.views import central_admin

app_name = 'central_admin'

urlpatterns = [
     path('institutions/', central_admin.InstitutionListView.as_view(), name='institution_list'),
     path('institutions/create/', central_admin.InstitutionCreateView.as_view(), name='institution_create'),
     path('institution/<slug:slug>/update/', central_admin.InstitutionUpdateView.as_view(), name='institution_update'),
]