import urllib.request
from .models import URL
import ssl

def getURL(url):
    try:
        model = URL.objects.get(short_url=url)
        model.checks += 1
        model.save()
        return model
    except:
        return __getURLInRedirect(url)


def __getURLInRedirect(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(
    url=url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    )
    with urllib.request.urlopen(req, context=context) as response:
        full_url = response.geturl()
        print(response)
        if full_url != url:
            model = URL(final_url = full_url, short_url=url, checks=1)
            model.save()
            return model
        else:
            raise Exception