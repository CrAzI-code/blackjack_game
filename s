[1mdiff --cc birth_certificate/models.py[m
[1mindex cfd34e7,189c0e1..0000000[m
[1m--- a/birth_certificate/models.py[m
[1m+++ b/birth_certificate/models.py[m
[36m@@@ -4,7 -5,14 +5,17 @@@[m [mfrom django.contrib.auth.models import [m
  [m
  # Create your models here.[m
  [m
[32m+ class PaymentToken(models.Model):[m
[32m+     user = models.ForeignKey(User, on_delete=models.CASCADE)[m
[32m+     token = models.CharField(max_length=25, primary_key=True)[m
[32m+     created_at = models.DateTimeField(auto_now=True)[m
[32m+     payment_date = models.DateField()[m
[32m+ [m
  class PersonalData(models.Model):[m
[32m++<<<<<<< HEAD[m
[32m++=======[m
[32m+     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)[m
[32m++>>>>>>> 843fcef28edb867dfe5c824ce07e9cc2a8dadc08[m
      fullname = models.CharField(max_length=100)[m
      fathername = models.CharField(max_length=100)[m
      gender = models.CharField(max_length=100)[m
[36m@@@ -14,3 -22,6 +25,9 @@@[m
      time = models.TimeField(auto_now=False, auto_now_add=False,  blank=True)[m
      date = models.DateField(auto_now=False, auto_now_add=False, blank=True)[m
  [m
[32m++<<<<<<< HEAD[m
[32m++=======[m
[32m+ [m
[32m+     # def __str__(self):[m
[32m+     #     return self.user.username[m
[32m++>>>>>>> 843fcef28edb867dfe5c824ce07e9cc2a8dadc08[m
[1mdiff --cc db.sqlite3[m
[1mindex d0ef8fb,f7270a9..0000000[m
Binary files differ
