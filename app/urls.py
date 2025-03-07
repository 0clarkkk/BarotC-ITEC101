from django.urls import path
from .views import HomePageView, AboutPageView, PortfolioPageView, ContactPageView, SkillsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('skills/', SkillsPageView.as_view(), name='skills')
]