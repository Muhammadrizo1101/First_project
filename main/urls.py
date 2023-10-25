from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('create_task/', create_task_view, name="create_task_url"),
    path('swap-status-deleted/<int:id>/', swap_status_deleted, name="swap_status_deleted_url"),
    path('swap-status-finished/<int:id>/', swap_status_finished, name="swap_status_finished_url"),
    path('get-inprogress-task/', inprogress_view, name="get_inprogress_view"),
    path('delete-task/<int:pk>/', deleted_task_view, name="delete_task_url")
]