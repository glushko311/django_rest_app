"""
URL configuration for my_collection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from collection.views import (
    ItemAPIList,
    ItemAPIView,
    ItemAPIUpdate,
    ItemAPIDestroy,
    CollectionItemsApiList,
    UserCollectionsApiList,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from my_collection import settings
# from collection.views import ItemApiViewSet
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'items', ItemApiViewSet, basename='item')

urlpatterns = [
    path('admin/', admin.site.urls),
    # # -------------------------------
    # path('api/v1/', include(router.urls)),
    # # Роутер заменил эти пути
    # # path('api/v1/items', ItemApiViewSet.as_view({'get': 'list', 'post': 'create'})),
    # # path('api/v1/items/<int:pk>/', ItemApiViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # # -------------------------------

    path('api/v1/items/', ItemAPIList.as_view()),
    path('api/v1/items/<int:pk>/', ItemAPIView.as_view()),
    path('api/v1/items/<int:pk>/update/', ItemAPIUpdate.as_view()),
    path('api/v1/items/<int:pk>/delete/', ItemAPIDestroy.as_view()),

    path('api/v1/collection/', UserCollectionsApiList.as_view()),
    path('api/v1/collection/<int:collection_id>/items/', CollectionItemsApiList.as_view()),

    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)