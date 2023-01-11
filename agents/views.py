from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.urls import reverse
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        return Agent.objects.filter(userprofile=self.request.user.userprofile)


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/create_agent.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.userprofile = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(userprofile=self.request.user.userprofile)


class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agents/update_agent.html"
    form_class = AgentModelForm

    def get_queryset(self):
        return Agent.objects.filter(userprofile=self.request.user.userprofile)

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agents/delete_agent.html"

    def get_queryset(self):
        return Agent.objects.filter(userprofile=self.request.user.userprofile)

    def get_success_url(self):
        return reverse("agents:agent-list")
