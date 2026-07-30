from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/home.html')
def product_detail(request, pk):
    return render(request, 'store/product_detail.html')
