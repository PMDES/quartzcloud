from django.urls import path
from . import views

urlpatterns = [
  path('<int:dm_id>', views.dm_view, name='dm_view'),
  path('create/<int:user_id>', views.dm_create)
]
