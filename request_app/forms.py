from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label='Возраст', max_value=100, min_value=1)
    info = forms.CharField(label = 'Информация', widget=forms.Textarea)


class UploadFileForm(forms.Form):
    file = forms.FileField()