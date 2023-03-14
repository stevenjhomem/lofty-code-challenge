from django.urls import path

import lofty_project.dogs.api.views as views

app_name = 'dogs'  # url up to this point /dogs/

urlpatterns = [
    path('', views.DogImageSetListView.as_view(), name='dog-set-list'),
    path('<int:dis_id>/', views.DogImageSetDetailView.as_view(), name='dog-set-detail'),
]
