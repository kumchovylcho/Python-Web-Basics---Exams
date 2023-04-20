from django.forms import ModelForm

from Library.Book.models import BaseBook


class BookForm(ModelForm):

    class Meta:
        model = BaseBook
        fields = "__all__"
