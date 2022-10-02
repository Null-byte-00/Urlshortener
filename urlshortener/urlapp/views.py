from django.shortcuts import render, redirect
from django.views import View
from .models import ShortenedUrl
from django.contrib.sites.shortcuts import get_current_site
from django.utils.text import slugify
# Create your views here.

class MakeUrl(View):
    """
    Creates ShortenedUrl object from posted target_url and slug arguments.
    ---------------------------------------------------------------------
    target_url : The url that the user will be redirected to.
    slug : The slug used in shortened url.
    """
    def get(self, request):
        return render(request, 'urlapp/make_url.html', {'domain': get_current_site(self.request).domain})

    def post(self,request):
        target_url = request.POST.get('target_url')
        slug = slugify(request.POST.get('slug'))

        #check if the requested url slug already exists or not
        if ShortenedUrl.objects.filter(slug=slug).exists():
            error = 'a url with this name already exists. try using another one'
            return render(request, 'urlapp/make_url.html', {'domain': get_current_site(self.request).domain,'error': error})
        
        shortened_url = ShortenedUrl.objects.create(target_url = target_url, slug = slug)
        shortened_url.save()
        return render(request, 'urlapp/show_url.html', {'shortened_url': shortened_url.link})

 
def redirect_url(request, urlslug):
    """ redirects user to target url. """
    url = ShortenedUrl.objects.get(slug = urlslug)
    return redirect(url.target_url)
