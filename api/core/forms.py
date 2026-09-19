from django import forms
from .models import RunTime



class TokenWidget(forms.TextInput):
    template_name = "core/widgets/token.html"
    def __init__(self, *args, runtime_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.runtime_id = runtime_id

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.runtime_id is not None:
            context["widget"]["attrs"]["runtime_id"] = self.runtime_id
        return context



class RunTimeAdminForm(forms.ModelForm):
    class Meta:
        model = RunTime
        fields = "__all__"

        widgets = {
            "token": TokenWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["token"].widget.runtime_id = (self.instance.pk if self.instance.pk else None)