from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book, Author, Publisher

# Create your views here.

#-- TemplateView

class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

#-- ListView
class BooksList(ListView):
    model = Book

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher

#-- DetaView
class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher