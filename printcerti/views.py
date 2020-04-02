from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from printcerti.models import Person, PersonForm
from django.shortcuts import render
import os
from django.conf import settings

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import qrcode

from arabic_reshaper import reshape

from bidi.algorithm import get_display


def arabic_certi(name, save, qrimg, xline=798.503, yline=624.414, img_dir="test.jpeg"):
    base_img = Image.open(img_dir)
    qr_img = Image.open(qrimg)
    base_img = base_img.copy()
    base_img.paste(qr_img, (86, 870))
    base_img.save(save)
    img = Image.open(save)
    draw = ImageDraw.Draw(img)
    msg = get_display(reshape(name))

    for i in range(1, 100)[::-1]:
        font = ImageFont.truetype(os.path.join(settings.BASE_DIR, "static/bein-black.ttf"), i)
        w, h = draw.textsize(msg, font=font)

        if w < 614.943 and h < 97.07:
            correct_font_size = i
            print(correct_font_size)
            break

    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, "static/bein-black.ttf"), correct_font_size)
    w, h = draw.textsize(msg, font=font)
    draw.multiline_text((xline-w/2, yline-h/1.5), msg, (255, 255, 255), font=font, align="left")
    img.save(save)


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)


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
            qr.add_data(f"www.{request.get_host()}/verify/{person.id}")

            qr.make(fit=True)
            img = qr.make_image()
            img.save(os.path.join(settings.MEDIA_ROOT, f"{name}qr.jpeg"))

            arabic_certi(name, os.path.join(settings.MEDIA_ROOT, f"{name}.jpeg"),
                         os.path.join(settings.MEDIA_ROOT, f"{name}qr.jpeg"),
                         img_dir=os.path.join(settings.MEDIA_ROOT, "test.jpeg"))

            person.image = f"{name}.jpeg"
            os.remove(os.path.join(settings.MEDIA_ROOT, f"{name}qr.jpeg"))
            with open(os.path.join(settings.MEDIA_ROOT, f"{name}.jpeg"), "rb") as image:
                response = HttpResponse(image.read(), content_type="image/jpeg")
                response['Content-Disposition'] = f'attachment; filename={person.image.url}'
                return response

    def get_success_url(self):
        return reverse("create")


class DetailCertification(DetailView):
    
    template_name = "details.html"
    queryset = Person.objects.all()
