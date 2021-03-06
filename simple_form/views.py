from operator import ge
from django.shortcuts import render
from .forms import SearchForm
from .services import get_weather

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            data = get_weather(s_query)
            return render(request, 'search.html',{'form': form,'city':data[0],'discription':data[1],'temp':data[2],'temp_max': data[3],'Description':'Description','Temperature':'Temperature','Maximum_Temperature':'Maximum Temperature'})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form,})

#added a comment to the commit