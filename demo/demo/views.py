from django.views.generic import FormView
from .forms import TestForm


class Index(FormView):
    form_class = TestForm
    template_name = 'index.html'
    success_url = ''

index = Index.as_view()
