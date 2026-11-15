from django import forms
from movies.models import Movie

class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'genre', 'description', 'year', 'actors', 'picture']


class MovieDeleteForm(MovieCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True

