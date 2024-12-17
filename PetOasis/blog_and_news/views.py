from django.shortcuts import render
from accounts.models import Profile
from django.contrib.auth.models import AnonymousUser
#from django.urls import reverse_lazy
#from django.views.generic import CreateView
#from blog_and_news.models import PawPost
#from blog_and_news.forms import PawPostForm

def show_blog_and_news_page(request):
    #render(request, template_name='blog_and_news/pawposts.html',
    # context = {'pawposts':PawPost.objects.all()})
    if not isinstance(request.user, AnonymousUser):
        profile = Profile.objects.get(user=request.user)
    else:
        profile = None
    
    context = {
        'profile': profile,
    }
    
    return render(request, 'blog_and_news/pawposts.html', context)

'''class PawPostCreateView(CreateView):
    form_class = PawPostForm
    template_name = 'blog_and_news/pawpost_create.html'
    success_url = reverse_lazy('blog_and_news')'''