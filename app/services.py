import urllib.request
from .models import URL

def getURL(url):
    try:
        model = URL.objects.get(short_url=url)
        model.checks += 1
        model.save()
        return model
    except:
        return __getURLInRedirect(url)


def __getURLInRedirect(url):
    req = urllib.request.Request(
    url=url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            full_url = response.geturl()
            if full_url != url:
                model = URL(final_url = full_url, short_url=url, checks=1)
                model.save()
                return model
            else:
                raise Exception
    except:
        return None