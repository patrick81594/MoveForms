from django import forms
from django.forms import ModelForm
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class mvForm(forms.ModelForm):
    class Meta:
        model = moveForm
        fields = ['First_Name', 'Last_Name', 'eMail', 'Citizenship', 'Company', 'Manager', 'subPOC', 'program', 'location', 'phoneNum',
                  'faaBadge', 'faaParking', 'comments', 'publication_date']

    def __init__(self, *args, **kwargs):
        super(mvForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
             Fieldset( "Name ",
                Field('First_Name', css_class='col-sm-2', id = "firstName"),
                Field('Last_Name', css_class='col-sm-2'),
                Div('eMail', css_class='col-sm-2'),
                ),
             Field('Citizenship', css_class = "form-control"),
             Field('Company'),
             Field('Manager'),
             Field('subPOC'),
             Field('program'),
             Field('location'),
             Field('phoneNum'),
             Field('faaBadge'),
             Field('faaParking'),
             Field('publication_date'),
             Field('comments'),
        
             
             FormActions(
                    Submit('submit', 'Submit', css_class='btn-primary'),
                    Button('cancel', 'Cancel', css_clas='btn'),
                    css_class = 'row',
            ),
        self.helper[1:3].wrap_together(layout.Fieldset, 'Name: ')

           
)
class assignedTaskForm(forms.ModelForm):
    class Meta:
        model = assignedTask
        fields = ['assignee', 'assignedTo','dateDue', 'task', 'relatedForm']

    def __init__(self, *args, **kwargs):
        super(assignedTaskForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
             Field('assignee', css_class='col-sm-2'),   
             Field('assignedTo', css_class='col-sm-2', id = "firstName"),
             Field('dateDue', css_class='col-sm-2'),                      
             Field('task', css_class='col-sm-2'),
             FormActions(
                    Submit('submit', 'Submit', css_class='btn-primary'),
                    Button('cancel', 'Cancel', css_clas='btn'),
                    css_class = 'row',
            ),

           
)

class userRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('firstName', 'lastName','username','password', 'eMail', 'company', 'Manager',
                  'program', 'phoneNum')
    def __init__(self, *args, **kwargs):
        super(userRegisterForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
                Field('firstName', css_class='fieldset', id = "firstName"),
                Field('lastName', rows="3", css_class='input-xlarge'),
                Field('username', css_class='input-xlarge'),
                Field('password', css_class='input-xlarge'),
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
