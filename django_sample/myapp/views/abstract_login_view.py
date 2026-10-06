from django.views import View
from two_factor.views.mixins import OTPRequiredMixin


class AbstractLoginRequiredView(OTPRequiredMixin, View):
    pass
