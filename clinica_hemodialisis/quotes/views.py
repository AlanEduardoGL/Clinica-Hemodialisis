from django.shortcuts import render, redirect
from .forms import FormQuotes

# Create your views here.


def quotes(request):

    error_message = None

    if request.method == 'POST':
        form = FormQuotes(request.POST)
    else:
        form = FormQuotes()

    return render(request, 'quotes/quotes.html', {'form': form, 'error_message': error_message})
