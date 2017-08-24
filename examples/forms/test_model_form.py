from django.core.validators import validate_slug
from django.db import models

from django.forms import ModelForm, Textarea, CharField
from tornado.platform.twisted import _

from examples.models.article import Article

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']


class ArticleForm(ModelForm):
    slug = CharField(validators=[validate_slug])

    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']
        field_classes = {
            'slug': 'MySlugFormField',
        }


# inherit ArticleForm
class EnhancedArticleForm(ArticleForm):

    def clean_pub_date(self):
        ...

    class Meta(ArticleForm.Meta):
        exclude = ('body',)
