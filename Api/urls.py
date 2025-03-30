from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static
from conta.views import UsuarioCreateView

def home(request):
    return HttpResponse("Bem-vindo ao catálogo online!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('produto.urls')), 
    path('api/', include('categoria.urls')),
    path('usuarios/', UsuarioCreateView.as_view(), name='create_usuario'),  
    path('', home),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)