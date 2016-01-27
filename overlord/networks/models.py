from overlord.core.models import DatedModel, NamedModel
# from django.core.validators import ValidationError
from django.core.urlresolvers import reverse


class Network(DatedModel, NamedModel):

    def get_absolute_url(self):
        return reverse("networks:detail", kwargs={"name": self.name})
    # def validate_unique(self, *args, **kwargs):
    #     super(Network, self).validate_unique(*args, **kwargs)

    #     old_network = self.__class__.objects.filter(
    #         name=self.name)

    #     if old_network.exists():
    #         raise ValidationError("Network with that name already exists")
