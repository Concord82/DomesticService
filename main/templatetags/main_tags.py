from django import template

register = template.Library()


@register.inclusion_tag('__base_menu.html', takes_context=True)
def main_menu(context):
    return {}

@register.inclusion_tag('tag_social_media.html', takes_context=True)
def social_links(context):
    return {}
