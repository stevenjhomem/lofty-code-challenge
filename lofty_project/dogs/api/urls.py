from django.urls import path

import lofty_project.dogs.api.views as views

app_name = 'dogs'  # url up to this point /dogs/

urlpatterns = [
    path('', views.DogListView.as_view(), name='dog-list'),
    path('<int:dog_id>/', views.DogDetailView.as_view(), name='dog-detail'),
]
