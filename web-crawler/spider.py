from urllib.request import urlopen
from link_finder import LinkFinder
from main import *

class Spider:
    # creating class variables
    project_name = ''
    base_url = ''
    domain_url = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self):
        pass




