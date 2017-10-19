from django.db import models
from django.utils import timezone

class Photo(models.Model):
    UNIVS = (
        ('G', 'GIST'),
        ('J', 'Jeonnam')
    )

    filename = models.CharField(max_length=30, primary_key=True)
    univ_code = models.CharField(max_length=1, choices = UNIVS)

    @classmethod
    def CreatePhoto(cls, _filename, _univ_code):
        photo = cls(filename=_filename, univ_code = _univ_code)
        return photo

    def AddScore(self, univcode, score):
        scoretable = self.gist_score if self.univcode == 'G' else self.jeonnam_score
        scoretable[score] += 1

    def GetMean(self, univcode):
        scoretable = self.gist_score if self.univcode == 'G' else self.jeonnam_score
        return sum([scoretable[i]*i for i in range(1,6)]) / sum(scoretable)

    def GetTotalMean(self):
        return sum([(self.gist_score[i]+jeonnam_score[i])*i for i in range(1,6)]) / (sum(gist_score)+sum(jeonnam_score))

    def __str__(self):
        return self.filename


class Person(models.Model):
    UNIVS = (
        ('G', 'GIST'),
        ('J', 'Jeonnam')
    )

    studentcode = models.IntegerField()
    univ_code = models.CharField(max_length=1, choices = UNIVS)


class Vote(models.Model):

    voter = models.ForeignKey(Person, on_delete = models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete = models.CASCADE)
