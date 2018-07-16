import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest.settings")
django.setup()

from appss.users.models import rest
from django.core import serializers
re = rest.objects.all()
res = serializers.serialize('json',re)
res['error'] = 'teset4est'

print(type(res))
print(res)

# rest.objects.create(username = 'ffffffffff')