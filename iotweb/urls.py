from django_request_mapping import UrlPattern
from iotweb.views import MyView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)