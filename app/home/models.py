from django.conf import settings
from wagtail import __version__ as WAGTAIL_VERSION
from wagtail.models import Page


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["wagtail_version"] = WAGTAIL_VERSION
        context["is_development"] = settings.DEBUG
        return context
