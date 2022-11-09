from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from universium_test.movies.api.views import MovieViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", MovieViewSet)
app_name = "movies"

urlpatterns = router.urls
