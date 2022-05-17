from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()
    num_authors = Author.objects.all().count()

    context = {
        'num_authors': num_authors,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
    }

    return render(request, 'books/index.html', context)


def authors(request):
    authors = Author.objects.all()
    return render(request, 'books/authors.html', {'authors': authors})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'books/author.html', {'author': author})


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    # queryset = Book.objects.filter(title__icontains=':')[:5:1]
    template_name = 'books/book_list.html'
    extra_context = {'spalva': '#fc0'}

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request and self.request.GET and self.request.GET.get('search_title'):
            queryset = queryset.filter(title__icontains=self.request.GET.get('search_title'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {} # this and below line technically repeats the above
        # context.update({self.context_object_name: self.get_queryset()})
        context.update({'spalva': 'wheat'}) #overwrites self.extra_context if matched as well
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
