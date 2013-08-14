from django.forms import Form
from django.forms.fields import DateTimeField
from datetimepicker.widgets import DateTimePicker


class TestForm(Form):
    datetime = DateTimeField(widget=DateTimePicker(format='dd/MM/yyyy hh:mm:ss'))
