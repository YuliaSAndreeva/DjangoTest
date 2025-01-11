from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.template.context_processors import request

from request_app.forms import UserForm, UploadFileForm

MAX_FILE_SIZE= 1 * 1024 * 2 # 1 Mb

def process_get(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context =  {
       'a' : a,
        'b' : b,
        'result' : result,

    }
    return render(request,'request_app/request_query_params.html', context=context)

def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        'form' : UserForm(),
    }
    return render(request, 'request_app/user_form.html', context = context)


def upload_file(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST' and request.FILES.get('myfile'):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data['file']

            if myfile.size > MAX_FILE_SIZE:
                print(f'Файл слишком большой! Максимальный размер {MAX_FILE_SIZE // 1024 * 2}MB')

                url = reverse('request_app:file_upload.html')

                return redirect(url)

            fs = FileSystemStorage()
            try:
                filename = fs.save(myfile.name, myfile)
                print(f'сохранили файл: {filename}')
            except Exception as e:
                print(f'Ошибка загрузки файла {e}')

    else:
        form = UploadFileForm()

    context = {
        'form' : form,
    }
    return render(request, 'request_app/file_upload.html', context = context)