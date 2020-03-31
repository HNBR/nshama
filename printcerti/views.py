from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from printcerti.models import Person, PersonForm
from django.shortcuts import render
import requests
from django.conf import settings


class CreateNewCertification(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = request.POST["w_name"].strip()
            person = Person.objects.create(w_name=name)
            with open(f"{settings.MEDIA_ROOT}/{name}.jpeg", "rb") as image:
                response = HttpResponse(image.read(),content_type="image/jpeg")
                response['Content-Disposition'] = f'attachment; filename={person.certificate.image.url}'
                return response

    def get_success_url(self):
        return reverse("create")

