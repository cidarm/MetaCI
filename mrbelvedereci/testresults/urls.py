from django.conf.urls import url

from mrbelvedereci.testresults import views


urlpatterns = [
    url(
        r'^(?P<build_id>\d+)/(?P<flow>.*)$',
        views.build_flow_tests,
        name='build_flow_tests',
    ),
    url(
        r'^trend/method/(?P<method_id>\d+)$',
        views.test_method_trend,
        name='test_method_trend',
    ),
]
