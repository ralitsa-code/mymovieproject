from datetime import date
from django import forms
from movies.models import Movie, Genre, Actor, Director

class MovieCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['genre'].queryset = Genre.objects.filter(status=Genre.APPROVED)
        self.fields['actors'].queryset = Actor.objects.filter(status=Actor.APPROVED)
        self.fields['director'].queryset = Director.objects.filter(status=Director.APPROVED)

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = date.today().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be in the future")
        return year

    class Meta:
        model = Movie
        fields = ['title', 'director', 'genre', 'description', 'year', 'actors', 'picture']


class MovieDeleteForm(MovieCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class ActorCreateForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']


class DirectorCreateForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name']

