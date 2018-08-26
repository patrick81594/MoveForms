# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


#class mvForm(forms.Form):
#    text_input = forms.CharField()

#    textarea = forms.CharField(
#        widget = forms.Textarea(),
#    )

#    radio_buttons = forms.ChoiceField(
#        choices = (
#            ('option_one', "Option one is this and that be sure to include why it's great"), 
#            ('option_two', "Option two can is something else and selecting it will deselect option one")
#        ),
#        widget = forms.RadioSelect,
#        initial = 'option_two',
#    )

#    checkboxes = forms.MultipleChoiceField(
#        choices = (
#            ('option_one', "Option one is this and that be sure to include why it's great"), 
#            ('option_two', 'Option two can also be checked and included in form results'),
#            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
#        ),
#        initial = 'option_one',
#        widget = forms.CheckboxSelectMultiple,
#        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#    )

#    appended_text = forms.CharField(
#        help_text = "Here's more help text"
#    )

#    prepended_text = forms.CharField()

#    prepended_text_two = forms.CharField()


#    # Uni-form
#    helper = FormHelper()
#    helper.form_class = 'form-horizontal'
#    helper.layout = Layout(
#        Field('text_input', css_class='input-xlarge'),
#        Field('textarea', rows="3", css_class='input-xlarge'),
#        'radio_buttons',
#        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
#        AppendedText('appended_text', '.00'),
#        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
#        PrependedText('prepended_text_two', '@'),
#        FormActions(
#            Submit('save_changes', 'Save changes', css_class="btn-primary"),
#            Submit('cancel', 'Cancel'),
#        )
#    )

class mvForm(forms.Form):
        First_Name = forms.CharField(max_length=100)
        Last_Name = forms.CharField(max_length=200)
        eMail = forms.EmailField()
        Citizenship = forms.CharField(max_length = 100)
        Company = forms.CharField(max_length = 200)
        Manager = forms.CharField(max_length = 200)
        subPOC = forms.CharField(max_length = 200)
        program = forms.CharField(max_length = 200)
        location = forms.ChoiceField(choices = (('WJHTC', "Technical Center"), ('Gathesburg', "Maryland")))
        phoneNum = forms.IntegerField()
        
        faaBadge = forms.CharField(max_length = 200)
        faaParking = forms.CharField(max_length = 200)
        comments = forms.CharField(widget = forms.Textarea(),)
        publication_date = forms.DateTimeField()
        # Uni-form
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
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