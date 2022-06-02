from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class NounGender(models.TextChoices):
    MASCULINE = 'M.', _('Masculine')
    FEMININE = 'F.', _('Feminine')
    NEUTER = 'N.', _('Neuter')

class Declension(models.TextChoices):
    FIRST = '1st', _('First')
    SECOND = '2nd', _('Second')
    THIRD = '3rd', _('Third')
    FOURTH = '4th', _('Fourth')
    FIFTH = '5th', _('Fifth')

class Noun(models.Model):
    nom_sing = models.TextField()
    gen_sing = models.TextField()
    gender = models.CharField(max_length=2, choices = NounGender.choices, default = NounGender.MASCULINE)
    declension = models.CharField(max_length=3, choices = Declension.choices, default=Declension.FIRST)
    definition = models.TextField()
    chapter = models.IntegerField(default=1)

    def __str__(self):
        return (f'{self.nom_sing}, {self.gen_sing}, {self.gender}, {self.definition}')