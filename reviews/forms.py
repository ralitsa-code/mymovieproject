from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        movie = kwargs.pop('movie')
        self.user = user
        self.movie = movie
        super().__init__(*args, **kwargs)
        self.instance.user = user
        self.instance.movie = movie


    def clean(self):
        cleaned_data = super().clean()
        already_reviewed = Review.objects.filter(
            user=self.user,
            movie=self.movie
        ).exists()

        if already_reviewed:
            raise forms.ValidationError(
                message='Review already made',
                code='already_reviewed'
            )
        return cleaned_data


    class Meta:
        model = Review
        fields = ['review', 'rating']



