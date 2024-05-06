from django.db import models
import uuid


# Create your models here.
class Skill(models.Model):

    skill_id = models.BigAutoField(editable=False, primary_key=True)
    skill_name = models.CharField()
    skill_type = models.IntegerField(null=True, blank=True)
    display_order = models.IntegerField()

    class Meta:
        db_table = "skill"
