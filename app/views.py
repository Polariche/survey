from django.shortcuts import render
from .models import Photo, Person, PersonForm, VoteForm
from survey import settings

# Create your views here.

def photo_survey(request, univcode):
    photos = Photo.objects.all()
    return render(request, 'index.html', 
        {'univcode': univcode,
        'studentcode': 0 if univcode == 'G' else len(Person.objects.filter(univ_code ='J')),
        'photos': photos,
        'names': ' '.join([photo.filename for photo in photos])})


def submit(request):
    if request.method == "POST":
        post = request.POST #univcode, studentcode, (photo)names, scores, answers

        studentcode = int(post['studentcode'])
        names = post['names'].split()
        scores = list(map(int, post['scores'].split()))

        personcheck = Person.objects.filter(studentcode=studentcode)
        person = None

        if not personcheck:
            personform = PersonForm({'univ_code': post['univ_code'], 'studentcode': studentcode})
            if personform.is_valid():
                person = personform.save(commit=False)
                person.save()
        else:
            person = personcheck[0]

        scores.reverse() #stack -> queue
        for name in names:
            voteform = VoteForm({})
            if voteform.is_valid():
                vote = voteform.save(commit=False)
                vote.score1 = scores.pop()
                vote.score2 = scores.pop()
                vote.score3 = scores.pop()
                vote.voter = person
                vote.photo = Photo.objects.get(filename=name)
                vote.save()
            
        #answers = post['answers'].split()

    return render(request, 'second.html')
