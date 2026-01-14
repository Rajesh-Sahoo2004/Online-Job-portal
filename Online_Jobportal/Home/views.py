from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faq.html')