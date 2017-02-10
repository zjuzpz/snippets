#In views.py

from django.template.defaulttags import register

@register.filter(name="access")
def access(dictionary, key):
    return dictionary[key]
    
 
#In html
{% if key in dict %}
  {{dict|access:key}}
{% endif %}
