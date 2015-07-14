from __future__ import unicode_literals
from django.forms.widgets import DateTimeInput
from django.template.loader import get_template
from django.template.context import Context


class DateTimePicker(DateTimeInput):
    class Media:
        css = {
            'all' : ('css/bootstrap-datetimepicker.min.css',)
        }
        js = (
            "js/bootstrap-datetimepicker.min.js",
        )

    def __init__(self, attrs=None, params=None, format=None):
        self.params = params or 'language: "en"'
        if format:
            self.format = format
            self.manual_format = True
        super(DateTimePicker, self).__init__(attrs=attrs, format=format)

    def render(self, name, value, attrs=None):
        template = get_template("datetimepicker/date-time-picker.html")
        context = Context({'name': name, 'id': attrs['id'], 'params': self.params, 'format': self.format, 'value': value})
        return template.render(context)
