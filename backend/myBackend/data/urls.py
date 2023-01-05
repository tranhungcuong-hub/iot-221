from django.urls import path, include
from django.views.generic import RedirectView

from data.views import GetLedAPI, GetHumidityAPI, GetLightAPI, GetTempAPI, PostLedAPI, PostHumidityAPI, PostLightAPI, PostTempAPI, GetPumpAPI, PostPumpAPI

urlpatterns = [
    # LED API VIEW
    path('led/GET/', GetLedAPI.as_view(), name='led_list_view'),
    path('led/POST/', PostLedAPI.as_view(), name='post_led_api'),

     # Pump API VIEW
    path('pump/GET/', GetPumpAPI.as_view(), name='Pump_list_view'),
    path('pump/POST/', PostPumpAPI.as_view(), name='post_Pump_api'),

    # HUMIDITY
    path('humidity/GET/', GetHumidityAPI.as_view(), name='humidity_list_view'),
    path('humidity/POST/', PostHumidityAPI.as_view(), name='post_humidity_api'),

    # TEMP
    path('temp/GET/', GetTempAPI.as_view(), name='temp_list_view'),
    path('temp/POST/', PostLightAPI.as_view(), name='post_temp_api'),
    
    # LIGHT
    path('light/GET/', GetLightAPI.as_view(), name='light_list_view'),
    path('light/POST/', PostTempAPI.as_view(), name='post_light_api'),
]