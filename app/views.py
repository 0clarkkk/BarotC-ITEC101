from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "app/home.html"

class AboutPageView(TemplateView):
    template_name = "app/about.html"

class PortfolioPageView(TemplateView):
    template_name = "app/portfolio.html"    

class ContactPageView(TemplateView):
    template_name = "app/contact.html"  
    
class SkillsPageView(TemplateView):
    template_name = "app/skills.html"  



def skills_view(request):
    skills = [
        {"name": "HTML", "level": 90},
        {"name": "CSS", "level": 85},
        {"name": "JavaScript", "level": 75},
        {"name": "Python", "level": 80},
        {"name": "Django", "level": 70},
    ]
    return render(request, "skills.html", {"skills": skills})
