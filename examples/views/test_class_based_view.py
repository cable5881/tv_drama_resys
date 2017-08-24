from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from examples.models.author import Author
from examples.models.book import Book
from examples.models.publisher import Publisher


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
    template_name = 'books/publisher_list.html'


class PublisherDetail(DetailView):
    # 相当于model = Publisher，但是可以自定义
    queryset = Publisher.order_by('-publication_date')
    context_object_name = 'publisher'
    template_name = 'books/acme_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


# a view that displayed all the books by some arbitrary publisher
class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object


"""
urlpatterns = [
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^books/([\w-]+)/$', PublisherBookList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author-detail'),
]
"""
