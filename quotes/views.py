from django.shortcuts import render
from quotes.models import Item

# Create your views here.
def main(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'quotes/main.html', context)
