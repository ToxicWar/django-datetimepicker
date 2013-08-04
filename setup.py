from setuptools import setup, find_packages

setup(
    name='django-datetimepicker',
    description='Django-datetimepicker is a simple widget for DateTimeField.',
    long_description=open('README.md').read(),
    version='0.0.1',
    author='Anton Larkin',
    author_email='toxicwar94@yandex.ru',
    url = "",
    packages = find_packages(),
    include_package_data = True,
    install_requires = [],
)
