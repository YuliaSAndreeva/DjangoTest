from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


MAX_FILE_SIZE= 10 * 1024 # 10 Kb

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
    return render(request, 'request_app/user_form.html')


def upload_form(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        if myfile.size > MAX_FILE_SIZE:
            print(f'Файл слишком большой! Максимальный размер {MAX_FILE_SIZE // 1024}KB')
            return render(request, 'request_app/file_upload.html')

        fs = FileSystemStorage()
        try:
            filename = fs.save(myfile.name, myfile)
            print(f'сохранили файл: {filename}')
            return render(request, 'request_app/file_upload.html')
        except Exception as e:
            print(f'Ошибка загрузки файла {e}')
            return render(request, 'request_app/file_upload.html')
    return render(request, 'request_app/file_upload.html')