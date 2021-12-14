from django import forms
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

from aplicatie2.models import UserExtend
from jobs.models import Job


class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        # fields = '__all__'
        fields = ['name', 'url', 'description', 'customer']

    def __init__(self, pk, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.job_pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        job_name = cleaned_data.get('name')
        if self.job_pk:
            if Job.objects.filter(name=job_name).exclude(id=self.job_pk).exists():
                self._errors['name'] = self.error_class(["Numele jobului deja exista"])
        else:
            if Job.objects.filter(name=job_name).exists():
                self._errors['name'] = self.error_class(["Numele jobului deja exista"])
        return cleaned_data
