from django.shortcuts import render


def about(request):
	return render(request, 'home/about.html', {})

def home(request):
	return render(request, 'home/home.html', {})

def projects(request):
	return render(request, 'home/projects.html', {})