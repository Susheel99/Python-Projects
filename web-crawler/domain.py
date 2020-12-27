from urllib.parse import urlparse


# get domain name(suhseel.pythonanywhere.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

#results[-3] + '.'
# Get subdomain name
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


print(get_domain_name('https://www.thenewboston.com/'))