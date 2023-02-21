from django.test import TestCase

# Create your tests here.
import codecs
file = codecs.open(r"C:\Users\abhil\PycharmProjects\Ems_django2\Ems_project\Ems_app\dummy_models.py", "w", "utf-8")
file.write(u'\ufeff')
file.close()