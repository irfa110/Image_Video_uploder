from django.shortcuts import render ,redirect

# Create your views here.
from .models import Video

def home(request):
    if request.method == 'POST':
        caption = request.POST['caption']
        video = request.FILES['video']
        form = Video(caption=caption,video=video)
        form.save()
        return redirect('home')

    video =  Video.objects.all()[::-1]
    return render(request,'video/home.html',{'video':video})

def delete(request,id):
    data = Video.objects.get(id=id)
    data.delete()
    return redirect('home')

# def index(request):
#     return render(request, 'video/index.html')