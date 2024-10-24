from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(mymodel)
# admin.site.register(book)
# admin.site.register(emp)
# admin.site.register(products)

# class cusadmin(admin.ModelAdmin):
#     list_display=('fname','lname','address','email')
#     search_fields=('fname',)
#     list_filter=('id',)
# admin.site.register(custmor,cusadmin)
# admin.site.site_header='voex'
# admin.site.site_title='django site'



# class postadmin(admin.ModelAdmin):
#     list_display=('title','author','created_at',)
#     search_fields=('title',)
#     list_filter=('author',)
# admin.site.register(post,postadmin)

# admin.site.register(product_user)

# admin.site.register(publisher)

# class bookadmin(admin.ModelAdmin):
#     list_display=('title','isbn','pub',)
#     search_fields=('title','isbn',)
#     list_filter=('pub_date',)
# admin.site.register(bookmodel,bookadmin)


# class courseadmin(admin.ModelAdmin):
#     list_display=('course_name','course_code','date',)
#     search_fields=('course_name',)
# admin.site.register(course_model,courseadmin)

# class studentadmin(admin.ModelAdmin):
#     list_display=('first_name','last_name','email','phn','course',)
#     search_fields=('first_name',)
# admin.site.register(student_model,studentadmin)


class organiseradmin(admin.ModelAdmin):
    list_display = ('name','email','phone',)
    search_fields = ('name',)
admin.site.register(organizer,organiseradmin)

class eventadmin(admin.ModelAdmin):
    list_display = ('title','date','location','organizer',)
    search_fields = ('title',)
admin.site.register(event,eventadmin)