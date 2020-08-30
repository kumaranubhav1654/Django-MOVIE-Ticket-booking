from django.shortcuts import render
from django.http import HttpResponse
from . models import movie,ticket
from datetime import datetime
# Create your views here.
def index (requests):
    movies = movie.objects.all()
    return render(requests,'index.html',{'movies':movies})

def bookt(requests):
    movie1=requests.GET['movie']
    booking=int(requests.GET['booking'])
    nos=int(requests.GET['nos'])
    username=requests.GET['name']
    phone=requests.GET['phone']
    booking=booking-nos
    book_time=datetime.now()
    ticket1 = ticket.objects.create(movie=movie1, book_time=book_time,user=username,phone=phone,nos=nos)
    movie.objects.filter(name=movie1).update(bookings=booking)
    obj= ticket.objects.get(movie=movie1, book_time=book_time,user=username,phone=phone,nos=nos)
    id=obj.id
    return render(requests,'booked.html',{'obj':obj})

def delt(requests):
    ticketid=requests.GET['id']
    movie2=requests.GET['movienm']
    obj = movie.objects.get(name=movie2)
    booking=int(obj.bookings)
    nos=int(requests.GET['nos'])
    username=requests.GET['username']
    phone=requests.GET['phone']
    book=booking+nos
    objt=ticket.objects.get(id=ticketid,user=username,phone=phone)
    print(objt.nos)
    left=objt.nos-nos
    if(left>0):
        movie.objects.filter(name=movie2).update(bookings=book)
        ticket.objects.filter(id=ticketid,user=username,phone=phone).update(nos=left)
    else :
        ticket.objects.filter(id=ticketid,user=username,phone=phone).delete()
    return render(requests,'deleted.html')

def delete(requests):
    return render(requests,'delete.html')

def updatetime(requests):
    return render(requests,'updateticket.html')

def viewticket(requests):
    return render(requests,'viewticket.html')

def details(requests):
    return render(requests,'userdetails.html')

def updatetimefn(requests):
    tid=int(requests.GET['tcid'])
    timing_start=requests.GET['ts']
    timing_end=requests.GET['te']
    movie.objects.filter(id=tid).update(time_start=timing_start,time_end=timing_end)
    return render(requests,'updated.html')

def viewticketfn(requests):
    timing_start=requests.GET['ts']
    obj=movie.objects.get(time_start=timing_start)
    mov=obj.name
    print(mov)
    tts=ticket.objects.filter(movie=mov)
    print(tts)
    return render(requests,'viewticketdisplay.html',{'obj':tts})

def userdetailsfn(requests):
    tid=int(requests.GET['tcid'])
    print(tid)
    obj=ticket.objects.get(id=tid)
    print (obj.phone)
    return render(requests,'userdetailsdisplay.html',{'obj':obj})


