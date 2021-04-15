from django.shortcuts import render
from django.views.generic import DetailView, ListView
from movies.models import Film, Genre, Attachment


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    num_films = Film.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    films = Film.objects.order_by('-rate')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_films': num_films,
        'films': films
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


class FilmListView(ListView):
    model = Film

    context_object_name = 'film_list'
    template_name = 'film/list.html'
    paginate_by = 2


class FilmDetailView(DetailView):
    model = Film

    context_object_name = 'film_detail'
    template_name = 'film/detail.html'


def topten(request):
    return render(request, 'topten.html')