from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.
def home(request):
    image = Image.objects.all()
    category = Category.objects.all()
    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForms()
    context = {
        'image': image,
        'form': form,
        'category': category,
    }
    return render(request, 'upload/home.html', context)


def category(request, id):
    category = Category.objects.all()
    categ = Category.objects.get(pk=id)
    image = Image.objects.filter(cat=categ)

    context = {
        'image': image,
        'category': category,
    }
    return render(request, 'upload/home.html', context)
