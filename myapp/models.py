from django.db import models

# Create your models here.
# class mymodel(models.Model):
#     user_id = models.IntegerField(primary_key=True)
#     user_name = models.CharField(max_length=200)
#     user_age = models.IntegerField()
#     date = models.DateField()
#     def __str__(self):
#         return self.user_name

# class product_user(models.Model):
#     pr_id=models.IntegerField(primary_key=True)
#     pr_name=models.CharField(max_length=50)
#     usep=models.ForeignKey(mymodel,on_delete=models.CASCADE)


    
# class book(models.Model):
#     book_id =models.IntegerField(primary_key=True)
#     title =models.CharField(max_length=100)
#     author =models.CharField(max_length=100)
#     pub_date =models.DateField()
#     isbn =models.CharField(max_length=13)

# class emp(models.Model):
#     emp_id =models.IntegerField(primary_key=True)
#     emp_name =models.CharField(max_length=50)
#     age =models.IntegerField()
#     salary=models.FloatField()

# class products(models.Model):
#     name =models.CharField(max_length=50)
#     decsr=models.TextField(max_length=50)
#     price=models.FloatField()
#     stock=models.IntegerField()
#     date=models.DateTimeField(auto_now_add=True)

# class custmor(models.Model):
#     fname=models.CharField(max_length=50)
#     lname=models.CharField(max_length=50)
#     email=models.EmailField(unique=True)
#     address=models.CharField(max_length=50)
#     dob=models.DateField()

# class post(models.Model):
#     title=models.CharField(max_length=50)
#     contant=models.TextField()
#     author=models.CharField(max_length=50)
#     created_at=models.DateTimeField()
#     updated_at=models.DateTimeField()




# class publisher(models.Model):
#     name=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)
#     emai=models.EmailField()
#     def __str__(self):
#         return self.name
    
# class bookmodel(models.Model):
#     title=models.CharField(max_length=50)
#     pub_date=models.DateField()
#     isbn=models.CharField(max_length=50,unique=True)
#     pub=models.ForeignKey(publisher,on_delete=models.CASCADE)


# class course_model(models.Model):
    # course_name=models.CharField(max_length=50)
    # course_code=models.CharField(max_length=50,unique=True)
    # date=models.DateField()
    # def __str__(self):
    #     return self.course_name
    
# class student_model(models.Model):
    # first_name=models.CharField(max_length=50)
    # last_name=models.CharField(max_length=50)
    # email=models.EmailField(unique=True)
    # phn=models.CharField(max_length=10)
    # course=models.ForeignKey(course_model,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.first_name
    

class organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(organizer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    