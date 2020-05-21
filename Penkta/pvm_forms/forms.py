from django.forms import ModelForm

from pvm_forms.models import PvmForm, Form


class PvmFormNewForm(ModelForm):
    class Meta:
        model = PvmForm
        fields = ('pavadinimas', 'vieta', 'vnt', 'kiekis', 'suma')


class MainFormNewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MainFormNewForm, self).__init__(*args, **kwargs)
        self.fields['numeris'].widget.attrs = {'class': 'form-control'}
        self.fields['istaiga'].widget.attrs = {'class': 'form-control'}
        self.fields['vieta'].widget.attrs = {'class': 'form-control'}
        self.fields['komisijos_nariai'].widget.attrs = {'class': 'form-control'}
        self.fields['atsakingas_darbuotojas'].widget.attrs = {'class': 'form-control'}
        self.fields['pardavejas'].widget.attrs = {'class': 'form-control'}
        self.fields['serija'].widget.attrs = {'class': 'form-control'}
        self.fields['pardavimo_data'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Form
        fields = ('numeris', 'istaiga', 'vieta', 'komisijos_nariai', 'atsakingas_darbuotojas', 'pardavejas', 'serija', 'pardavimo_data')
        labels = {'numeris': 'Numeris', 'istaiga': 'Įstaiga', 'vieta': 'Vieta', 'komisijos_nariai': 'Komisijos nariai', 'atsakingas_darbuotojas': 'Atsakingas darbuotojas', 'pardavejas': 'Pardavėjas', 'serija': 'Serija', 'pardavimo_data': 'Pardavimo data'}

    # pavadinimas = forms.CharField(label='Pavadinimas', max_length=200)
    # vieta = forms.CharField(label='Vieta', max_length=500)
    # vnt = forms.CharField(label='Vienetai', max_length=200)
    # kiekis = forms.IntegerField(label='Kiekis')
    # suma = forms.FloatField(label='Bendra suma')
