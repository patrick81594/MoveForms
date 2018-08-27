# -*- coding: utf-8 -*-
from django import forms
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class mvForm(forms.ModelForm):
    class Meta:
        model = moveForm
        fields = ['First_Name', 'Last_Name', 'eMail', 'Citizenship', 'Company', 'Manager', 'subPOC', 'program', 'location', 'phoneNum',
                  'faaBadge', 'faaParking', 'comments', 'publication_date']

        # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Field('First_Name', css_class='input-xlarge', id = "firstName"),
        Field('Last_Name', rows="3", css_class='input-xlarge'),
        Field('eMail', css_class = 'input-xlarge'),
        Field('Citizenship', css_class = 'input-xlarge'),
        Field('Company', css_class = 'input-xlarge'),
        Field('Manager', css_class = 'input-xlarge'),
        Field('subPOC', css_class = 'input-xlarge'),
        Field('program', css_class = 'input-xlarge'),
        Field('location', css_class = 'input-xlarge'),
        Field('phoneNum', css_class = 'input-xlarge'),
        Field('faaBadge', css_class = 'input-xlarge'),
        Field('faaParking', css_class = 'input-xlarge'),
        Field('comments', css_class = 'input-xlarge'),
        Field('publication_date', css_class = 'input-xlarge'),
        #'radio_buttons',
        #Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        #AppendedText('appended_text', '.00'),
        #PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        #PrependedText('prepended_text_two', '@'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
    )
)

class userRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('firstName', 'lastName', 'userName', 'password', 'eMail', 'company', 'Manager',
                  'program', 'phoneNum')
        # Uni-form
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.form_method = 'POST'
        helper.layout = Layout(
        Field('firstName', css_class='input-xlarge', id = "firstName"),
        Field('lastName', rows="3", css_class='input-xlarge'),
        Field('userName', css_class = 'input-xlarge'),
        Field('eMail', css_class = 'input-xlarge'),
        Field('Company', css_class = 'input-xlarge'),
        Field('Manager', css_class = 'input-xlarge'),
        Field('program', css_class = 'input-xlarge'),
        Field('phoneNum', css_class = 'input-xlarge'),
        #'radio_buttons',
        #Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        #AppendedText('appended_text', '.00'),
        #PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        #PrependedText('prepended_text_two', '@'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
    )
)