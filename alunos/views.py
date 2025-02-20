from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def criar_aluno(request):
    return render(request, 'criar_aluno.html')