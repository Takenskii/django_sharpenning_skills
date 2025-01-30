from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
import random
from home.forms import ContactForm
from home.models import Contact


# Create your views here.

# class HomeView(View):
#     template_name = 'index.html'

#     def get(self, request):
#         return render(request, self.template_name)
#     def post(self, request):
#         return render(request, self.template_name)

def index(request):
    lucky_number=random.randint(100,999)
    vegetables = ["tomatoes", "potatoes", "chilly", "carrot", "cucumber"]
    person_age = 18

    cities = [
        {"name": "Mumbai", "population": "20 000 000", "country": "India"},
        {"name": "London", "population": "30 000 000", "country": "UK"},
        {"name": "New York", "population": "25 000 000", "country": "USA"},
        {"name": "Shanghai", "population": "50 000 000", "country": "China"},
    ]

    context = {"lucky_number":lucky_number, "vegetables": vegetables, "person_age": person_age, "cities":cities}
    # return HttpResponse("Hi from Django!")
    return render(request, 'index.html', context)
def about(request):
    # return HttpResponse("Hi from Django server this is a about page!")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hi from Django server this is a contact page!")
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # contact = Contact(**form.cleaned_data)
            form.save()
            return redirect('/contact/')
            
    form = ContactForm()
    context = {'form':form}
    return render(request, 'contact.html', context)

def dynamic_url(request, id, name):
    print(f"This is the value that we got in the func -> {id}")
    return render(request, 'dynamic_url.html', context={"id":id, "name":name})

def project(request):
    lucky_number = random.randint(0, 100)
    context = {"lucky_number":lucky_number}
    return render(request, "project/project.html", context)