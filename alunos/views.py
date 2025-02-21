from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    if request.method == 'GET':

        return render(request, 'criar_aluno.html')
    
    elif request.method == 'POST':

        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        if not nome or not idade or not email:
            messages.error(request, 'Preencha todos os campos!')
            return redirect('criar_aluno')
        
        if not idade.isdigit() or int(idade) <= 0 or int(idade) > 99:
            messages.error(request, 'Idade inválida!')
            return redirect('criar_aluno')
        
        if not email.endswith(('@gmail.com', '@outlook.com', '@hotmail.com')):
            messages.error(request, 'E-mail inválido!')
            return redirect('criar_aluno')

        aluno = Aluno(
            nome=nome.capitalize(),
            idade=idade, 
            email=email
        )

        aluno.save()

        messages.success(request, 'Aluno criado com sucesso!')
        return redirect('criar_aluno')
        
    return render(request, 'criar_aluno.html')