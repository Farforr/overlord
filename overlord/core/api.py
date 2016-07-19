from django.conf.urls import url

from overlord.users import views as user_views
from django.conf.urls import include

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

    url(r'^minions/v1/', include("overlord.minions.api.v1.urls", namespace="minions_api_v1")),
]
