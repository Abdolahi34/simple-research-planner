from django import forms


class ResearchForm(forms.Form):
    topic = forms.CharField(
        label="موضوع تحقیق",
        max_length=200,
        widget=forms.TextInput(attrs={'style': 'width:400px'})
    )

    method = forms.ChoiceField(
        label="روش تحقیق",
        choices=[
            ('quant', 'کمی'),
            ('qual', 'کیفی'),
        ]
    )
