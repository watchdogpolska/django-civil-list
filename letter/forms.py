from django import forms
from .models import Letter
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class SendLetter(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SendLetter, self).__init__(*args, **kwargs)
        qs = self.instance.category.person_set.all()
        self.fields['to'] = forms.ModelMultipleChoiceField(queryset=qs)
        self.fields['doc_from'] = forms.CharField(
            widget=forms.HiddenInput())
        self.fields['doc_title'] = forms.CharField(
            widget=forms.HiddenInput(attrs={'value': self.instance.title}))
        self.fields['doc_content'] = forms.CharField(
            widget=forms.HiddenInput(attrs={'value': self.instance.content}))
        self.fields['doc_sign'] = forms.CharField(widget=forms.HiddenInput())
        self.helper = FormHelper(self)
        self.helper.form_id = "form_send_letter"
        self.helper.layout = Layout(
                'to',
                Div(css_class="paper", template="letter/paper.html"),
                'doc_from',
                'doc_title',
                'doc_content',
                'doc_sign',
            )
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class='button white'))

    class Meta:
        model = Letter
        fields = ()

    def send_mails(self):
        # self.cleaned_data['']

        subject = self.cleaned_data['doc_title']
        html_content = self.cleaned_data['doc_content'] + \
            "<br />" + settings.LETTER_FOOTER_HTML
        text_content = strip_tags(self.cleaned_data['doc_content']) + \
            "\n\n" + settings.LETTER_FOOTER_TEXT
        recipient_list = [p.email for p in self.cleaned_data['to']]
        send_mail(
            subject=subject,
            message=text_content,
            html_message=html_content,
            from_email=settings.LETTER_FROM,
            recipient_list=recipient_list)
