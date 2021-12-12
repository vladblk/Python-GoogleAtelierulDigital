from django.urls import path

from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('index/', views.ListJobsView.as_view(), name='listare_jobs'),
    path('add/', views.CreateJobsView.as_view(), name='adauga_job'),
    path('update/<int:pk>', views.UpdateJobsView.as_view(), name='modifica_job'),
    path('delete/<int:pk>', views.delete_job, name='sterge_job')
]