
from django.urls import reverse
from gallery.models import Photo
from django.views.generic import CreateView
from gallery.forms import PhotoForm

class PhotoList(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "gallery/home.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoList, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.all().order_by('-uploaded')
        return context

    def get_success_url(self):
        return reverse('home')
