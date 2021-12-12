from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import UserExtend
from jobs.forms import JobsForm
from jobs.models import Job


# Create your views here.


class ListJobsView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/jobs_index.html'

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return self.model.objects.all()
        return self.model.objects.filter(id=self.request.user.userextend.customer.id)


class CreateJobsView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobsForm

    template_name = 'jobs/jobs_form.html'

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.userextend.customer.id)

    def get_form_kwargs(self):
        variable_to_send = super(CreateJobsView, self).get_form_kwargs()
        variable_to_send.update({'pk': None})
        return variable_to_send

    def get_success_url(self):
        return reverse('jobs:listare_jobs')


class UpdateJobsView(LoginRequiredMixin, UpdateView):
    model = Job
    # fields = '__all__'
    form_class = JobsForm
    template_name = 'jobs/jobs_form.html'

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.userextend.customer.id)

    def get_form_kwargs(self):
        variable_to_send = super(UpdateJobsView, self).get_form_kwargs()
        variable_to_send.update({'pk': self.kwargs['pk']})
        return variable_to_send

    def get_success_url(self):
        return reverse('jobs:listare_jobs')


@login_required
def delete_job(request, pk):
    if request.user.is_authenticated:
        Job.objects.filter(id=pk).update(active=0)

    return redirect('jobs:listare_jobs')