from django.shortcuts import render,redirect

from django.http import HttpResponse

from.models import *

# Create your views here.

# def fun(req):
#     return HttpResponse("<h1>today the day</h1>")

# def fun1(req):
#     return render(req,"h.html",{"name":"ads"})
# def fun2(req):
#     context = {
#         'fruits':['apple','banaana','orange']
#     }
#     return render(req,'fruit.html',context)

# def fun3(request):
#     iteams = [
#         {'name':'laptop','price':20000,'quntity':5},
#         {'name':'phone','price':15000,'quntity':10},
#         {'name':'tv','price':5000,'quntity':5},
#     ]
#     return render(request,'iteam.html',{'item':iteams})

# def pro(req):
#     product = [
#         {'name':'laptop','price':9999,'status':True},
#         {'name':'Smartphone','price':5999,'status':False},
#         {'name':'Tablet','price':2999,'status':True},
#         {'name':'Headphone','price':999,'status':True},
#     ]
#     return render(req,'product.html',{'products':product})


# def fun4(req):
#     data = mymodel.objects.all()
#     return render(req,'all.html',{'datas':data})

# def funct(req):
#     if req.method =='POST':
#         id=req.POST.get('userid')
#         name=req.POST.get('name')
#         age=req.POST.get('age')
#         date=req.POST.get('date')
#         user_obj=mymodel()
#         user_obj.user_id=id
#         user_obj.user_name=name
#         user_obj.user_age=age
#         user_obj.date=date
#         user_obj.save()
#     return render(req,'user.html')

# def bk(req):
#     books = book.objects.all()
#     return render (req,'b.html',{'bks':books})

# def display(req):
#     if req.method == 'POST':
#         id=req.POST.get('id')
#         name=req.POST.get('name')
#         author=req.POST.get('author')
#         date=req.POST.get('date')
#         isbn=req.POST.get('isbn')
#         user_obj=book()
#         user_obj.book_id=id
#         user_obj.title=name
#         user_obj.author=author
#         user_obj.pub_date=date
#         user_obj.isbn=isbn
#         user_obj.save()
#     return render(req,'disp.html')

# def empp(req):
#     empdata = emp.objects.all()
#     return render(req,'emp.html',{'data':empdata})

# def deletee(req,id):
#     user=emp.objects.get(emp_id=id)
#     user.delete()
#     return redirect('x')

# def updatee(req,id):
#     user =emp.objects.filter(emp_id=id)
#     if req.method =='POST':
#         id=req.POST.get('id')
#         name=req.POST.get('name')
#         age=req.POST.get('age')
#         salary=req.POST.get('salary')
#         ep=emp()
#         ep.emp_id=id
#         ep.emp_name=name
#         ep.age=age
#         ep.salary=salary
#         ep.save()
#         return redirect('x')
#     return render(req,'upd.html',{'usr':user})

# def add(req):
#     if req.method == 'POST':
#         id=req.POST.get('id')
#         name=req.POST.get('name')
#         age=req.POST.get('age')
#         salary=req.POST.get('salary')
#         user_obj=emp()
#         user_obj.emp_id=id
#         user_obj.emp_name=name
#         user_obj.age=age
#         user_obj.salary=salary
#         user_obj.save()
#         return redirect('x')
#     return render(req,'add.html')
    

# def product(req):
#    p_data = products.objects.all()
#    return render(req,'prod.html',{'data':p_data})

# def add_pr(req):
#     if req.method == 'POST':
#         name=req.POST.get('name')
#         decs=req.POST.get('decs')
#         price=req.POST.get('price')
#         stock=req.POST.get('stock')

#         user_obj=products()
#         user_obj.name=name
#         user_obj.decsr=decs
#         user_obj.price=price
#         user_obj.stock=stock
#         user_obj.save()
#         return redirect('p')
#     return render(req,'p_add.html')

# def view_cust(req):
#     cus_data=custmor.objects.all()
#     return render(req,'viewcus.html',{'data':cus_data})

# def delt(req,id):
#     user=custmor.objects.get(id=id)
#     user.delete()
#     return redirect('t')

# def adcus(req):
#     if req.method == 'POST':
#         name=req.POST.get('fname')
#         lnamee=req.POST.get('lname')
#         email=req.POST.get('email')
#         address=req.POST.get('adress')
#         dob=req.POST.get('dob')

#         user_obj=custmor()
#         user_obj.fname=name
#         user_obj.lname=lnamee
#         user_obj.email=email
#         user_obj.address=address
#         user_obj.dob=dob
#         user_obj.save()
#         return redirect('t')
#     return render(req,'addcus.html')

# # def updt(req,id):
# #     user =custmor.objects.get(id=id)
# #     if req.method == 'POST':
# #         name=req.POST.get('fname')
# #         lnamee=req.POST.get('lname')
# #         email=req.POST.get('email')
# #         address=req.POST.get('adress')
# #         dob=req.POST.get('dob')
# #         user.fname=name
# #         user.lname=lnamee
# #         user.email=email
# #         user.address=address
# #         user.dob=dob
# #         user.save()
# #         return redirect('t')
# #     return render(req,'updtt.html',{'user':user})


# def vpost(req):
#     view_post=post.objects.all()
#     return render(req,'viewpost.html',{'data':view_post})

# def dpost(req,id):
#     bk=post.objects.get(id=id)
#     bk.delete()
#     return redirect('m')
 
 
# def apost(req):
#     if req.method == 'POST':
#         title=req.POST.get('title')
#         contant=req.POST.get('contant')
#         author=req.POST.get('author')
#         created=req.POST.get('createdd')
#         updated=req.POST.get('updatedd')

#         bkpost=post()
#         bkpost.title=title
#         bkpost.contant=contant
#         bkpost.author=author
#         bkpost.created_at=created
#         bkpost.updated_at=updated
#         bkpost.save()
#         return redirect('m')
#     return render(req,'adpost.html')


# # def upost(req,id):
# #     user =post.objects.get(id=id)
# #     if req.method == 'POST':
# #         title=req.POST.get('title')
# #         contant=req.POST.get('contant')
# #         author=req.POST.get('author')
# #         created=req.POST.get('createdd')
# #         updated=req.POST.get('updatedd')
# #         user.title=title
# #         user.contant=contant
# #         user.author=author
# #         user.created_at=created
# #         user.updated_at=updated
# #         user.save()
# #         return redirect('m')
# #     return render(req,'upost.html',{'user':user})


# def vi_pro(req):
#     vipr=product_user.objects.all()
#     return render(req,'vipro.html',{'data1':vipr})

# def vi_add(req):
#     data=mymodel.objects.all()
#     if req.method=='POST':
#         prid=req.POST.get('prid')
#         prname=req.POST.get('prname')

#         prad=product_user()

#         prad.pr_id=prid
#         prad.pr_name=prname
#         prad.usep=mymodel.objects.get(user_id=req.POST.get('user_id'))
#         prad.save()
#         return redirect('f')
#     return render(req,'praddd.html',{'dats':data})






# def vi_bk(req):
#     v_bk=bookmodel.objects.all()
#     return render(req,'vibk.html',{'dat':v_bk})


# def adbk(req):
#     data=publisher.objects.all()
#     if req.method=='POST':
#         title=req.POST.get('title')
#         isbn=req.POST.get('isbn')
#         pubdate=req.POST.get('pubdate')
#         bkad=bookmodel()
#         bkad.title=title
#         bkad.isbn=isbn
#         bkad.pub_date=pubdate
#         bkad.pub=publisher.objects.get(id=req.POST.get('id'))
#         bkad.save()
#         return redirect('s')
#     return render(req,'adbk.html',{'datas':data})

# def dbk(req,id):
#     user=bookmodel.objects.get(id=id)
#     user.delete()
#     return redirect('s')

# def ubk(req,id):
#     up=publisher.objects.all()
#     data3=bookmodel.objects.get(id=id)
#     if req.method == 'POST':
#         title=req.POST.get('title')
#         isbn=req.POST.get('isbn')
#         pubdate=req.POST.get('pubdate')
#         data3.title=title
#         data3.isbn=isbn
#         data3.pub_date=pubdate
#         data3.pub=publisher.objects.get(id=req.POST.get('id'))
#         data3.save()
#         return redirect('s')
#     return render(req,'ubk.html',{'uptd':up,'das':data3})


# def add_student(req):
#     std=course_model.objects.all()
#     if req.method == 'POST':
#         fname=req.POST.get('fname')
#         lname=req.POST.get('lname')
#         email=req.POST.get('email')
#         phn=req.POST.get('phn')

#         add=student_model()
#         add.first_name=fname
#         add.last_name=lname
#         add.email=email
#         add.phn=phn
#         add.course=course_model.objects.get(id=req.POST.get('id'))
#         add.save()
#         return redirect('v_std')
#     return render(req,'addstd.html',{'data':std})


# def view_student(req):
#     view=student_model.objects.all()
#     return render(req,'vistd.html',{'data1':view})

# def delt_student(req,id):
#     dlt=student_model.objects.get(id=id)
#     dlt.delete()
#     return redirect('v_std')
# def update_stu(request,id):
#     data=course_model.objects.all()
#     data1=student_model.objects.get(id=id)
#     if request.method == 'POST':
#         fname=request.POST.get('fname')
#         lname=request.POST.get('lname')
#         email=request.POST.get('email')
#         phone=request.POST.get('phn')
#         data1.first_name=fname
#         data1.last_name=lname
#         data1.email=email
#         data1.phn=phone
#         data1.course=course_model.objects.get(id=request.POST.get('id'))
#         data1.save()
#         return redirect('v_std')
#     return render(request,"updtstd.html",{'value':data,'value1':data1})

# def course_disp(req,id):
#     co=course_model.objects.get(id=id)
#     data3=student_model.objects.filter(course_model=co)
#     return render(req,'codisplay.html',{'value':data3,'value1':co})


def view_organizer(req):
    data=organizer.objects.all()
    return render(req,'vieworg.html',{'view':data})

def delt_organizer(req,id):
    dlt=organizer.objects.get(id=id)
    dlt.delete()
    return redirect('z')

def add_organizer(req):
    if req.method =='POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        add=organizer()
        add.name = name
        add.email = email
        add.phone = phone
        add.save()
        return redirect('z')
    return render(req,'addorg.html')


def update_organizer(req,id):
    user=organizer.objects.get(id=id)
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')

        user.name = name
        user.email = email
        user.phone = phone
        user.save()
        return redirect('z')
    return render(req,'uptdorg.html',{'uptd':user})


def view_event(req):
    data=event.objects.all()
    return render(req,'viewevent.html',{'value':data})

def delt_event(req,id):
    dltt=event.objects.get(id=id)
    dltt.delete()
    return redirect('x')

def add_event(req):
    data=organizer.objects.all()
    if req.method == 'POST':
        title = req.POST.get('title')
        date = req.POST.get('date')
        location = req.POST.get('location')
        ade = event()
        ade.title = title
        ade.date = date
        ade.location = location
        ade.organizer=organizer.objects.get(id=req.POST.get('id'))
        ade.save()
        return redirect('x')
    return render(req,'adevent.html',{'value':data})

def uptd_event(req,id):
    data=organizer.objects.all()
    data1=event.objects.get(id=id)
    if req.method =='POST':
        title = req.POST.get('title')
        date = req.POST.get('date')
        location = req.POST.get('location')

        data1.title = title
        data1.date = date
        data1 = location
        data1.organizer = organizer.objects.get(id=req.POST.get('id'))
        data1.save()
        return redirect('x')
    return render(req,'updtevent.html',{'value':data,'value2':data1})










