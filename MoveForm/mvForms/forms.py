from django import forms
from django.forms import ModelForm
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class mvForm(forms.ModelForm):
    class Meta:
        model = moveForm
        fields = ['First_Name', 'Last_Name', 'eMail', 'Citizenship', 'Company', 'Manager', 'subPOC', 'program', 'location', 'phoneNum',
                  'faaBadge', 'faaParking', 'comments', 'publication_date']

    def __init__(self, *args, **kwargs):
        super(mvForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('cancel', 'Cancel'))
        self.helper.layout = Layout(
           Fieldset(
             Field('First_Name', css_class='form-control', id = "firstName"),
             Field('Last_Name', rows="3", css_class='input-xlarge'),
             Field('eMail'),
             ),
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
        
             
             FormActions(
                    Submit('submit', 'Submit', css_class='btn-primary'),
                    Button('cancel', 'Cancel'),
            ),
        self.helper[0:2].wrap_together(layout.Fieldset, 'Your name')

           
)

class userRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('firstName', 'lastName', 'username', 'password', 'eMail', 'company', 'Manager',
                  'program', 'phoneNum')
    def __init__(self, *args, **kwargs):
        super(userRegisterForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
       # self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
                Field('firstName', css_class='fieldset', id = "firstName"),
                Field('lastName', rows="3", css_class='input-xlarge'),
                Field('username', css_class = 'input-xlarge'),
                Field('password', css_class = 'input-xlarge'),
                Field('eMail', css_class = 'input-xlarge'),
                Field('company', css_class = 'input-xlarge'),
                Field('Manager', css_class = 'input-xlarge'),
                Field('program', css_class = 'input-xlarge'),
                Field('phoneNum', css_class = 'input-xlarge'),
                FormActions(
                     Submit('save_changes', 'Save changes', css_class="btn-primary"),
                     Submit('cancel', 'Cancel'),
                )
)
