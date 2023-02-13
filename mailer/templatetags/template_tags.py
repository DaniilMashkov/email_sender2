from django.template.defaulttags import register


@register.simple_tag
def media_path(path):
    return '/media/' + str(path) if path\
        else 'http://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/23fc5f6bbd18e66.png'


