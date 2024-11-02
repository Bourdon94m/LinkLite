from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.db.models import Sum
from .models import shortURL, URLClick


def home(request):
    context = {
        'total_links': shortURL.objects.count(),
        'total_clicks': shortURL.objects.aggregate(Sum('clicks'))['clicks__sum'] or 0
    }

    if request.method == 'POST':
        original_url = request.POST.get('url')
        if original_url:
            short_url = shortURL.objects.create(original_url=original_url)
            context['short_url'] = short_url
            context['full_short_url'] = request.build_absolute_uri(f'/{short_url.short_code}/')

    return render(request, 'shortner/home.html', context)


def create_short_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        if original_url:
            short_url = shortURL.objects.create(original_url=original_url)
            return redirect('shortener:stats')
    return redirect('shortener:home')


def url_stats(request):
    urls = shortURL.objects.all().order_by('-created_at')
    return render(request, 'shortner/home.html', {'urls': urls})


def redirect_to_original(request, short_code):
    url = get_object_or_404(shortURL, short_code=short_code)

    URLClick.objects.create(
        url=url,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        referrer=request.META.get('HTTP_REFERER')
    )

    url.clicks += 1
    url.save()

    return redirect(url.original_url)