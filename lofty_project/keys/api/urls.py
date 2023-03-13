from django.urls import path

import lofty_project.keys.api.views as views

app_name = 'keys'  # url up to this point /keys/

urlpatterns = [
    path('', views.KeysListView.as_view(), name='keys-list'),
    path('create/', views.KeyDetailView.as_view(), name='keys-detail'),
    path('<int:pk>/increment/', views.KeyDetailView.as_view(), name='key-increment'),

]
