from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.TextField()
    phone= models.CharField(max_length=15)
    is_favorite= models.BooleanField(default=False)


def create_contact(names, emails, phones, is_favorites):
    result = Contact(name=names, email=emails, phone = phones, is_favorite = is_favorites,)
    result.save()
    return result

def all_contacts():
    return list(Contact.objects.all())

def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None

def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email):
    contact = find_contact_by_name(name)
    if contact:
        contact.email = new_email
        contact.save()
    return contact

def delete_contact(name):
    contact = find_contact_by_name(name)
    if contact:
        contact.delete()