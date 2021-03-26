import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
import pytesseract
# Create your views here.

# ctrl f5 to clear site cache or ctrl shift r

def index(request):
    # return HttpResponse("Hello World")
    pics = Image.objects.all()
    return render(request, 'search/index.html', {
        "upload": UploadForm(),
    })


def upload(request):
    if request.method == "POST":
        # print(request.FILES)
        form=UploadForm(request.POST, request.FILES)
        # uploaded_file=request.FILES['upload']
        # fs=FileSystemStorage()
        # name=fs.save(uploaded_file.name,uploaded_file)
        # print(uploaded_file.name,uploaded_file.size,fs.url())
        if form.is_valid():
            uploaded_file = form.cleaned_data["upload"]
            #ext=uploaded_file.split('/')[-1].split('.')[-1]
            ext = os.path.splitext(uploaded_file)
            if ext in ('gif','png','jpg','jpeg','bmp','tif','tiff','eps'):
                # print(form.cleaned_data)
                image=Image.objects.create(title=uploaded_file,image_file=uploaded_file)
                path='smartdoc'+image.image_file.url
                # print(path,image.image_file,image_file,type(image_file),image_file.content_type,image_file.read())
                text = pytesseract.image_to_string(path)
                image.text=text.strip()
                print(image.image_file.url,image.image_file.name,image.image_file.path)
                image.save()
            elif ext in ('wav'):
                audio=Audio.objects.create(title=uploaded_file,audio_file=uploaded_file)
                pass
            return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))

def search_image(request):
    pics = Image.objects.all()
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            search_text=form.cleaned_data["search"]
            print(search_text)
            pics = Image.objects.filter(text__icontains=search_text)
            context={'pics':pics,
            "upload": UploadForm(),
            "search": form,}
            return render(request, 'search/index.html', context)
    else:
         return render(request, 'search/search_image.html', {
        "search": SearchForm(),
        "pics": pics
    })

def search_audio(request):
    pass