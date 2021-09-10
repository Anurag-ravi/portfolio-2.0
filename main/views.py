from django.shortcuts import render,redirect
from.models import Education,Portfolio,Profile,Service,ServiceDetail,Skill,SocialLink,Subskill,Testimonial,Work
from django.core.mail import send_mail
from portfolio import settings
import random

# Create your views here.
def index(request):
    topsocials = SocialLink.objects.filter(label='t')
    bottomsocials = SocialLink.objects.filter(label='b')
    profile = Profile.objects.all().first()
    profile.colortheme = random.randint(0,360)
    profile.save()
    educations = Education.objects.all()
    works = Work.objects.all()
    skills = Skill.objects.all()
    subskills = Subskill.objects.all()
    services = Service.objects.all()
    servicedetails = ServiceDetail.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    length = Skill.objects.all().count()

    param = {
        'topsocials':topsocials,
        'bottomsocials':bottomsocials,
        'profile':profile,
        'educations':educations,
        'works':works,
        'skills':skills,
        'subskills':subskills,
        'services':services,
        'servicedetails':servicedetails,
        'portfolios':portfolios,
        'testimonials':testimonials,
    }

    return render(request, 'main/index.html', param)

def send(request):
    if(request.method == 'POST'):
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        project = request.POST.get('project', 'default')
        message = request.POST.get('message', 'default')
        to_email = "kumarayush1014@gmail.com"
        send_mail(
            subject = "mail from portfolio",
            message = "name = " + name + ".      email = " + email + ".      project = " + project + ".     message = " + message +".",
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_email],
            fail_silently = True,
        )
        return redirect('home')