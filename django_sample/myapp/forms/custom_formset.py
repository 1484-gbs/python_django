from django import forms


class SampleForm(forms.Form):
    guitar = forms.ChoiceField()

    def __init__(self, mst={}, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        print(kwargs)
        if "initial" in kwargs:
            mst = kwargs["initial"]
            print(mst)
            self.fields["guitar"].widget = forms.Select(
                choices=[("", "")] + [(mst["cd"], mst["value"])]
            )
            self.fields["guitar"].label = mst["name"]


SampleFormset = forms.formset_factory(form=SampleForm, min_num=1, extra=0)
