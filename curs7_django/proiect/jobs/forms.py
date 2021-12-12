from django import forms

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
        name_value = cleaned_data.get('name')
        if self.job_pk:
            if Job.objects.filter(name=name_value).exclude(id=self.job_pk).exists():
                self._errors['name'] = self.error_class(["Numele jobului deja exista"])
        else:
            if Job.objects.filter(name=name_value).exists():
                self._errors['name'] = self.error_class(["Numele jobului deja exista"])
        return cleaned_data