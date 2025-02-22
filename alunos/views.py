from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        alunos = Aluno.objects.all()
        print(alunos)
        return render(request, 'criar_aluno.html', {'status': status, 'alunos': alunos})
    
    elif request.method == 'POST':

        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        if not nome or not idade or not email:
            # messages.error(request, 'Preencha todos os campos!')
            return redirect('/alunos/criar_aluno/?status=1')
        
        if not idade.isdigit() or int(idade) <= 0 or int(idade) > 99:
            messages.error(request, 'Idade inválida!')
            return redirect('/alunos/criar_aluno/?status=2')
        
        if not email.endswith(('@gmail.com', '@outlook.com', '@hotmail.com')):
            messages.error(request, 'E-mail inválido!')
            return redirect('/alunos/criar_aluno/?status=3')

        aluno = Aluno(
            nome=nome.capitalize(),
            idade=idade, 
            email=email
        )

        aluno.save()

        messages.success(request, 'Aluno criado com sucesso!')
        return redirect('/alunos/criar_aluno/?status=0')
        
    return redirect('/alunos/criar_aluno/')

def excluir_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('/alunos/criar_aluno/')