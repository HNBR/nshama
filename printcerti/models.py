from django.db import models
from django import forms
from django.utils.translation import gettext as _


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.bootstrap import Field


class Person(models.Model):

    w_name = models.CharField(
        max_length=60,
        verbose_name=_("Full name"),
        default="",
    )
    image = models.ImageField(blank=True, default="test.jpeg")

    def __str__(self):
        return f"{self.w_name}"


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["w_name", ]

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
