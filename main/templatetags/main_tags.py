from django import template
from main.models import SocialLink

register = template.Library()


@register.inclusion_tag('_tag_menu.html', takes_context=True)
def main_menu(context):
    return {}

@register.inclusion_tag('_tag_social_media.html', takes_context=True)
def social_links(context):
    soc_links = SocialLink.objects.order_by('my_order').filter(enabled=True)
    return {'soc_links': soc_links}
