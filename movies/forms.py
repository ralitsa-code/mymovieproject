from datetime import date
from django import forms

from common.forms import DisabledFieldsMixin
from movies.models import Movie, Genre, Actor, Director

class MovieCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['genre'].queryset = Genre.objects.filter(status=Genre.APPROVED)
        self.fields['actors'].queryset = Actor.objects.filter(status=Actor.APPROVED)
        self.fields['director'].queryset = Director.objects.filter(status=Director.APPROVED)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter movie title'
        self.fields['year'].widget.attrs['placeholder'] = 'e.g. 2024'
        self.fields['description'].widget.attrs['placeholder'] = 'Write a short movie description'


    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = date.today().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be in the future!")
        return year

    class Meta:
        model = Movie
        fields = ['title', 'director', 'genre', 'description', 'year', 'actors', 'picture']

        labels = {
            'title': 'Movie Title',
            'director': 'Director(s)',
            'genre': 'Genre(s)',
            'description': 'Movie Description',
            'year': 'Release Year',
            'actors': 'Cast',
            'picture': 'Movie Poster',
        }

        help_texts = {
            'title': 'Enter the official movie title',
            'director': 'Select one or more directors',
            'genre': 'Select the genres that describe the movie',
            'actors': 'Select the actors featured in the movie',
            'description': 'Provide a short description of the movie',
            'year': 'Enter the release year of the movie',
            'picture': 'Upload a poster image of the movie',
        }

        error_messages = {
            'title': {
                'required': 'Please enter a movie title!',
            },
            'description': {
                'required': 'Please enter a movie description.',
            },
            'year': {
                'required': 'Please enter the movie release year.',
            }
        }


class MovieDeleteForm(DisabledFieldsMixin, MovieCreateForm):
    ...


class GenreCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter genre name'

    class Meta:
        model = Genre
        fields = ['name']

        labels = {
            'name' : 'Genre Name',
        }



        error_messages = {
            'name': {
                'required': 'Please enter a genre name!'
            },
        }


class ActorCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter the first name of the actor'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter the last name of the actor'

    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']

        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
        }

        error_messages = {
            'first_name': {
                'required': 'Please enter the first name of the actor!'
            },
            'last_name': {
                'required': 'Please enter the last name of the actor!'
            }
        }


class DirectorCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter the first name of the director'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter the last name of the director'

    class Meta:
        model = Director
        fields = ['first_name', 'last_name']

        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
        }


        error_messages = {
            'first_name': {
                'required': 'Please enter the first name of the director!'
            },
            'last_name' : {
                'required': 'Please enter the last name of the director!'
            }
        }

