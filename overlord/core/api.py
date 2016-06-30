from django.conf.urls import url

from overlord.users import views as user_views
from overlord.networks import views as network_views
from overlord.nodes import views as node_views
from overlord.sensors import views as sensor_views
from overlord.actuators import views as actuator_views

urlpatterns = [
    # url confs for users app
    url(
        regex=r'^users/$',
        view=user_views.UserList.as_view(),
        name='user_rest_api'
    ),

    url(
        regex=r'^users/(?P<pk>[0-9]+)/$',
        view=user_views.UserDetail.as_view(),
        name='user_rest_api'
    ),
]
