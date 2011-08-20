from django.contrib.syndication.views import Feed
from chicagocrime.models import NewsItem

class LatestEntriesFeed(Feed):
    title = "Chicagocrime.org site news"
    link = "/"
    description = "Updates on changes and additions to chicagocrime.org."

    def items(self):
        return NewsItem.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description