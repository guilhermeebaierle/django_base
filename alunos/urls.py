from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('criar_aluno/', views.criar_aluno, name='criar_aluno'),
    path('excluir_aluno/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
