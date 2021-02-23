from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/employees/(?P<pk>[0-9]+)$', # Url to get update or delete a movie
        views.EmployeeView.as_view(),
        name='get_delete_update_employees'
    ),
    path('api/v1/employees/', # urls list all and create new one
        views.get_post_employees().as_view(),
        name='get_post_employees'
    )
]