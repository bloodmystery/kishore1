from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
# Create your views here.
username = ''
password = ''
disability = ''
def index(request):
    return render(request,"index.html")

def signup(request):
    global username,password,disability
    if request.method == "POST":
        m = sql.connect(host="localhost",user="bloodmystery",passwd="Tesla@2021",database="Learning")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == 'uname':
                username = value
            if key == 'psw':
                password = value
            if key == 'disability':
                disability = value 
        
        c = "Insert into users values('{}','{}','{}')".format(username,password,disability)
        
        cursor.execute(c)
        m.commit()

    return render(request,"index.html")

def login(request):
    global username,password
    if request.method == "POST":

        m = sql.connect(host="localhost",user="bloodmystery",passwd="Tesla@2021",database="Learning")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == 'uname':
                username = value
            if key == 'psw':
                password = value
        
        c = '''select * from users where username = "{}" and password = "{}"'''.format(username,password)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"welcome.html")
        
def blind(request):
    return render(request,"blind.html")

def deaf(request):
    return render(request,"deaf.html")

def paralyzed(request):
    return render(request,"paralyzed.html")

def slb(request):
    return render(request,"slb.html")

def flb(request):
    return render(request,"flb.html")

def slb1(request):
    return render(request,"slb1.html")

def flb1(request):
    return render(request,"flb1.html")

def sld(request):
    return render(request,"sld.html")

def fld(request):
    return render(request,"fld.html")

def sld1(request):
    return render(request,"sld1.html")

def fld1(request):
    return render(request,"fld1.html")

def slp(request):
    return render(request,"slp.html")

def flp(request):
    return render(request,"flp.html")

def slp1(request):
    return render(request,"slp1.html")

def flp1(request):
    return render(request,"flp1.html")

