from django.shortcuts import render
from . import models

def mark(req):
    if req.method == 'POST':
        rollNum = str(req.POST['rollnum'])
        data = models.marks.objects.filter(roll_num=rollNum)
        return render(req,"marks.html",{'data':data})
    data = models.marks.objects.all()
    return render(req,"marks.html",{'data':data})