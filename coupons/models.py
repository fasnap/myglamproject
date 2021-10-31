from django.db import models

from accounts.models import Account

class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.CharField(max_length=3)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.code

class CouponCheck(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)