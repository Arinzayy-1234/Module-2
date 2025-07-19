from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy

from . models import Book

# Create your views here.

def index(request):

    return HttpResponse('Welcome to Arinze\'s Book World 👀👀. All are welcome ')

def book_list(request):
    # This view would typically retrieve a list of books from the database
    # and render them in a template.

    context = {'books': Book.objects.all()}

    return render(request, 'my_app/book_list.html',context)
    
    
class hello_view(TemplateView):

    # A class based view rendering a template name hello.html

    template_name = 'my_app/hello.html'

class BookDetailView(DetailView):

    model = Book # The object that DetailView is dealing with is an instance of Book

    template_name = 'my_app/book_detail.html' # The template to render the book details

    def get_context_data(self, **kwargs):

        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['bookid'] = book.get_bookID()
        return context

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date']

    template_name = 'my_app/book_update_form.html'

    success_url = reverse_lazy('book_list')  # Redirect to book list after successful update

    def form_valid(self,form):
        """Handle the form submission and save the updated book."""
        response = super().form_valid(form)
        # You can add additional logic here if needed
        return response