from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from resume.local import render_pdf
from resume.local import render_to_pdf


def index(request):
    return render(request, 'resume/index.html', {})


def english(request):
    return render(request, 'resume/english.html', {})

def english(request):

        if request.method == 'POST':

            message = ''
            message += 'Nome Completo: ' + request.POST['full-name'] + '\n'
            message += 'E-mail: ' + request.POST['email'] + '\n'
            message += 'Assunto: ' + request.POST['subject'] + '\n'
            message += 'Mensagem: ' + request.POST['message'] + '\n'

            send_mail('Contato do Formulário',
                    message,
                    settings.EMAIL_HOST_USER,
                    ['rafaelcorreiaaraujo18@gmail.com'],
                    fail_silently=False)
        return render(request, 'resume/english.html')


def index(request):

    if request.method == 'POST':

        message = ''
        message += 'Nome Completo: ' + request.POST['full-name'] + '\n'
        message += 'E-mail: ' + request.POST['email'] + '\n'
        message += 'Assunto: ' + request.POST['subject'] + '\n'
        message += 'Mensagem: ' + request.POST['message'] + '\n'

        send_mail('Contato do Formulário',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['rafaelcorreiaaraujo18@gmail.com'],
                  fail_silently=False)
    return render(request, 'resume/index.html')


class idiomaEN(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/english.html', {})


   

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_pdf('resume/portugues.html')

        return HttpResponse(pdf, content_type='application/pdf')


class InglesPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('resume/ingles.html')
        return HttpResponse(pdf, content_type='application/pdf')
