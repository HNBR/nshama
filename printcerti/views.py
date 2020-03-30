from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from printcerti.models import Person, PersonForm
from django.shortcuts import render


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
            person = Person.objects.create(w_name=request.POST["w_name"])
            # person.save()
            return HttpResponseRedirect(person.certificate.image.url)

    def get_success_url(self):
        return reverse("create")

