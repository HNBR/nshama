from django.db import models
from django import forms
from django.utils.translation import gettext as _
from django.conf import settings

import os

from django.urls import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.bootstrap import Field

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from arabic_reshaper import reshape

from bidi.algorithm import get_display







def arabic_certi(name, save, xline=798.503, yline=624.414, img_dir="test.jpeg"):
    img = Image.open(img_dir)
    W, H = (img.width, img.height)
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

class Person(models.Model):

    w_name = models.CharField(max_length=60, verbose_name=_("Full name"), default="")

    def __str__(self):
        return f"{self.w_name}"

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        arabic_certi(f"{self.w_name}", settings.MEDIA_ROOT + f"/{self.w_name}.jpeg", img_dir=settings.MEDIA_ROOT + "/test.jpeg")
        certificate = Certificate(person=self, image=settings.MEDIA_ROOT + f"/{self.w_name}.jpeg")
        certificate.image.name = f"/{self.w_name}.jpeg"
        certificate.save()

        

class Certificate(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default=settings.MEDIA_ROOT +"/" +"test.jpeg")

    def __str__(self):
        return f"{self.person.w_name}"




class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["w_name",]

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field("w_name", id="w_name", css_class="align-middle"),
            ButtonHolder(
                Submit('submit', _('print'), css_class='btn-primary btn-block')
            )
        )
