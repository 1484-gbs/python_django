from django import forms


class SampleForm(forms.Form):
    guitar = forms.ChoiceField(required=False)

    def __init__(self, mst={}, *args, **kwargs):
        has_item = []
        if "has_item" in kwargs:
            has_item = kwargs.pop("has_item")

        super(SampleForm, self).__init__(*args, **kwargs)

        if "initial" in kwargs:
            mst = kwargs["initial"]
            self.fields["guitar"] = forms.ChoiceField(
                choices=[("", "")] + [(mst["cd"], mst["value"])],
                label=mst["name"],
                required=False,
                initial=mst["cd"] if mst["cd"] in has_item else "",
            )


SampleFormset = forms.formset_factory(form=SampleForm, min_num=1, extra=0)
