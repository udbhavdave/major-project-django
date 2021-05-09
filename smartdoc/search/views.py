import os
import pytesseract
import speech_recognition
import operator
from functools import reduce

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import F, Count, Q, Sum
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from .models import *
from .forms import *

BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT
# Create your views here.

def index(request):
    context = {
        "upload": UploadForm(),
    }
    if request.method == "POST":
        # print(request.FILES)
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data["upload_file"]
            ext = os.path.splitext(uploaded_file.name)[-1]
            if ext in (".gif", ".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".eps"):
                # print(form.cleaned_data)
                image = Image.objects.create(
                    title=uploaded_file.name, image_file=uploaded_file
                )
                path = "smartdoc" + image.image_file.url
                # print(path,image.image_file,image_file,type(image_file),image_file.content_type,image_file.read())
                text = pytesseract.image_to_string(path)
                image.text = text.strip()
                print(
                    image.image_file.url, image.image_file.name, image.image_file.path
                )
                image.save()
            elif ext in (".wav"):
                # AUDIO_FILE = os.path.join(MEDIA_ROOT, "test_files\\Welcome.wav")
                # print(AUDIO_FILE)
                audio_obj = Audio.objects.create(
                    title=uploaded_file, audio_file=uploaded_file
                )
                path = "smartdoc" + audio_obj.audio_file.url

                # use the audio file as the audio source

                recognizer = speech_recognition.Recognizer()

                with speech_recognition.AudioFile(path) as source:
                    #reads the audio file. Here we use record instead of
                    #listen
                    audio = recognizer.record(source)

                try:
                    text = recognizer.recognize_google(audio)
                    print("The audio file contains: " + text)
                    audio_obj.text = text
                    audio_obj.save()

                except speech_recognition.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")

                # except speech_recognition.RequestError as e:
                # 	print("Could not request results from Google Speech
                # 			Recognition service; {0}".format(e))
                pass
        context = {
            "upload": UploadForm(),
            "message": "File Uploaded Successfully", 
        }
        # send_mail('Hi','message','Udbhav',['d3bbcf86df-627722@inbox.mailtrap.io','udbhavdave@gmail.com'])
    return render(request, "search/index.html", context)


# def upload(request):
    
#             return redirect(reverse("index"))
#     return redirect(reverse("index"))
#     # return JsonResponse({})


def search_image(request):
    pics = Image.objects.all()
    search_text = ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data["search"]
            print(search_text)
            queries = search_text.strip().split()
            if queries:
                qset = reduce(operator.__or__, [Q(text__icontains=query) for query in queries])
            pics = Image.objects.filter(qset).distinct()
            context = {
                "pics": pics,
                "upload": UploadForm(),
                "search": form,
                "search_text": search_text, 
            }
            return render(request, "search/search_image.html", context)
    else:
        print(pics)
        context = {
            "search": SearchForm(), 
            "pics": pics, 
            "search_text": search_text
        }
        return render(
            request, "search/search_image.html", context
        )

 
def search_audio(request):
    audio_list = Audio.objects.all()
    search_text= ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data["search"]
            print(search_text)
            queries = search_text.strip().split()
            if queries:
                qset = reduce(operator.__or__, [Q(text__icontains=query) for query in queries])
            audio_list = Audio.objects.filter(qset).distinct()
            context = {
                "audio_list": audio_list,
                "upload": UploadForm(),
                "search": form,
                "search_text": search_text
            }
            return render(request, "search/search_audio.html", context)
    else:
        print(audio_list)
        return render(
            request, "search/search_audio.html", {"search": SearchForm(), "audio_list": audio_list}
        )
