from django.views.generic import  TemplateView


class SubmissionSuccessView(TemplateView):
    template_name = 'common/submission_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submission_type'] = self.request.GET.get('type', 'content')
        return context