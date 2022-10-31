from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOISES = (
        ('MEDIK', 'MEDIK'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            'media_type',
        ]
        
    def parser_data(self):
        if self.data['media_type'] == 'MEDIK':
            film_parser = parser.parser()
            for i in film_parser:
                models.AllMedApartment.objects.create(**i)
