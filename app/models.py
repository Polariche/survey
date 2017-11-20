from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class Photo(models.Model):
    UNIVS = (
        ('G', 'GIST'),
        ('J', 'Jeonnam')
    )

    filename = models.CharField(max_length=30, primary_key=True)
    univ_code = models.CharField(max_length=1, choices = UNIVS)
    gender = models.CharField(max_length=1, choices = (('M', 'Male'), ('F','Female')))

    @classmethod
    def CreatePhoto(cls, _filename, _univ_code, _gender):
        photo = cls(filename=_filename, univ_code = _univ_code, gender = _gender)
        return photo

    def GetVotes(self, univcode):
        return [x for x in Vote.objects.filter(photo=self) if x.voter.univ_code == univcode]

    def GetMean(self, univcode):
        votes = self.GetVotes(univcode)
        return sum([x.score for x in votes]) / len(votes)

    def GetTotalMean(self):
        scores = 0
        totalvotes = 0
        for u in self.UNIVS:
            vote = GetVotes(u[0])
            scores += sum([x.score for x in vote])
            totalvotes += len(vote)
        return scores / totalvotes

    def __str__(self):
        return self.filename


class Person(models.Model):
    UNIVS = (
        ('G', 'GIST'),
        ('J', 'Jeonnam')
    )

    studentcode = models.IntegerField(primary_key=True)
    univ_code = models.CharField(max_length=1, choices = UNIVS)

    def __str__(self):
        return str(self.studentcode)


class Vote(models.Model):
    voter = models.ForeignKey('Person', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)

    score1 = models.IntegerField(default=0, choices = tuple([(i,i) for i in range(1,6)]))
    score2 = models.IntegerField(default=0, choices = tuple([(i,i) for i in range(1,6)]))
    score3 = models.IntegerField(default=0, choices = tuple([(i,i) for i in range(1,6)]))

    def __str__(self):
        return ' - '.join([str(self.voter.studentcode), self.photo.filename])

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['studentcode', 'univ_code']

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = []


