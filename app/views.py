from django.shortcuts import render
from .models import Photo, Person, Vote, PersonForm, VoteForm
from survey import settings
import openpyxl

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

def create_sheet(request):
    wb = openpyxl.Workbook()

    #sheet 1 : score mean by photo
    ws = wb.active
    photos = Photo.objects.all()


    ws.append(['사진', '소속대학', '성별', '단정성', '세련성', '활동성'])

    for photo in photos:
        ws.append([photo.filename, photo.univ_code, photo.gender, *photo.GetMean()])


    #sheet 2 : votes
    ws = wb.create_sheet(title="투표")
    people = Person.objects.all()

    ws.append(['학번', '소속대학'])

    for person in people:
        votes = []
        for photo in photos:
            vote = Vote.objects.filter(photo=photo, voter=person)[0]
            votes += [vote.score1, vote.score2, vote.score3]

        ws.append([person.studentcode, person.univ_code, *votes])

    #sheet 3
    ws = wb.create_sheet(title="")

    ws.append(['사진 수', len(photos)])
    ws.append(['투표자 수', len(people)])

    wb.save('result.xlsx')

    return render(request, 'second.html')