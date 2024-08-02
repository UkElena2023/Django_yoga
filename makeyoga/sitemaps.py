from django.contrib.sitemaps import Sitemap
from yoga.models import Asana


class AsanaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Asana.objects.all()

    def lastmod(self, obj):
        pass






