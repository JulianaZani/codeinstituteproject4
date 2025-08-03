from django import template

register = template.Library()


@register.filter
def cloudinary_optimize(url):
    """
    Optimize Cloudinary image URLs by adding transformations
    for WebP/AVIF, automatic compression, and 800x600 resizing.
    """
    if not url or '/upload/' not in url:
        return url  # Return original if it's not a Cloudinary URL

    return url.replace(
        '/upload/',
        '/upload/f_auto,q_auto,w_800,h_600,c_fill/'
    )
