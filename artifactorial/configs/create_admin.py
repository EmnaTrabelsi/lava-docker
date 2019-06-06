from django.contrib.auth.models import User

def run():
    if not User.objects.filter(username='emna').count():
        print "Creating user emna"
        user = User.objects.create_user('emna', 'emna@mail.com', 'emnaemna')
        user.is_staff = True
        user.is_superuser = True
        user.save()

