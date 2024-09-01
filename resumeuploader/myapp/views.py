from django.shortcuts import render , redirect
from .forms import ResumeForm
from .models import Resume

from django.views import View 

class HomeView(View):
    def get(self,request):
        candidates = Resume.objects.all()
        form = ResumeForm()
        return render(request,'myapp/home.html', {'form':form,'candidates':candidates})

    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate':candidate})