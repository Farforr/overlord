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

    # url confs for networks app
    url(
        regex=r"^networks/$",
        view=network_views.NetworkList.as_view(),
        name="network_rest_api"
    ),

    url(
        regex=r"^networks/(?P<pk>[0-9]+)/$",
        view=network_views.NetworkDetail.as_view(),
        name="network_rest_api"
    ),

    # url confs for nodes app
    url(
        regex=r"^nodes/$",
        view=node_views.NodeList.as_view(),
        name="node_rest_api"
    ),

    url(
        regex=r"^nodes/(?P<pk>[0-9]+)/$",
        view=node_views.NodeDetail.as_view(),
        name="node_rest_api"
    ),

    # url confs for sensors app
    url(
        regex=r"^sensors/$",
        view=sensor_views.SensorList.as_view(),
        name="sensor_rest_api"
    ),

    url(
        regex=r"^sensors/(?P<pk>[0-9]+)/data/$",
        view=sensor_views.SensorDataList.as_view(),
        name="sensor_rest_api"
    ),

    url(
        regex=r"^sensors/(?P<pk>[0-9]+)/$",
        view=sensor_views.SensorDetail.as_view(),
        name="sensor_rest_api"
    ),

    # url confs for actuators app
    url(
        regex=r"^actuators/$",
        view=actuator_views.ActuatorList.as_view(),
        name="actuator_rest_api"
    ),

    url(
        regex=r"^actuators/(?P<pk>[0-9]+)/$",
        view=actuator_views.ActuatorDetail.as_view(),
        name="actuator_rest_api"
    ),

    url(
        regex=r"^actuators/(?P<pk>[0-9]+)/data/$",
        view=actuator_views.ActuatorDataList.as_view(),
        name="actuator_rest_api"
    ),
]
