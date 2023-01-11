from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
    TemplateView,
)
from .models import Lead, Agent
from .forms import LeadModelForm, CreateUserForm


class LandingPageView(TemplateView):
    template_name = "home.html"


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse("login")


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/create_lead.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_vaild(self, form):
        ## TODO: Check why email is not working
        # Send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="prateek9jain8@gmail.com",
            recipient_list=["test@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/update_lead.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/delete_lead.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


## ALL FUNCTION BASED VIEWS

# def home_page(request):
#     return render(request, "home.html")

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {"leads": leads}
#     return render(request, "leads/lead_list.html", context)

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {"lead": lead}
#     return render(request, "leads/lead_detail.html", context)

# def create_lead(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print(request.POST)
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {"form": form}
#     return render(request, "leads/create_lead.html", context)

# def update_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         print(request.POST)
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {"form": form, "lead": lead}
#     return render(request, "leads/update_lead.html", context)

# def create_lead(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print(request.POST)
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print("Form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name, last_name=last_name, age=age, agent=agent
#             )
#             return redirect("/leads")

#     context = {"form": form}
#     return render(request, "leads/create_lead.html", context)

# def delete_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
