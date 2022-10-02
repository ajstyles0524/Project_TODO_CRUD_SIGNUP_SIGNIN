from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from .forms import GeeksForm
from .models import GeeksModel


class GeeksCreate(CreateView):
    # specify the model for create view
    model = GeeksModel
    # specify the fields to be displayed
    fields = ['title', 'description']
    success_url = '/'


class GeeksList(ListView):
    # specify the model for list view
    model = GeeksModel


class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel


class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel

    # specify the fields
    fields = [
        "title",
        "description"
    ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/"


class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/"


class GeeksFormView(FormView):
    # specify the Form you want to use
    form_class = GeeksForm

    # specify name of template
    template_name = "ClassView/geeksmodel_form.html"

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/thanks/"
