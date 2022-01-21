from django.shortcuts import render
from .forms import SearchForm

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            return render(request, 'search.html', {'form': form, 's_results': s_query})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form,})
