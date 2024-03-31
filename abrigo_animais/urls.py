from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pagina_inicial.views import inicio
from cadastro_voluntarios.views import cadastro_voluntario

urlpatterns = [
    path("admin/", admin.site.urls),
    path("adocoes/", include("adocoes.urls"), name="adocoes"),
    path('', inicio),
    path('cadastro_voluntario/', cadastro_voluntario)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# "+ static" é uma maneira de adicionar URLs de arquivos de mídia aos urlpatterns no Django