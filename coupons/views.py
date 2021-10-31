#admin view all coupons
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from coupons.forms import CouponApplyForm
from .models import Coupon, CouponCheck

def checkCoupon(request, discount=0):

    if 'coupon_id' in request.session:
        del request.session['sub_total']
        del request.session['coupon_id']
        del request.session['discount_price']
        
    
    flag = 0
    discount_price = 0
    coupon = request.POST['coupon']
    total = float(request.POST['total'])

    if Coupon.objects.filter(code=coupon).exists():
        coup = Coupon.objects.get(code=coupon)
        if coup.status == True:
            flag = 1
            if not CouponCheck.objects.filter(user=request.user, coupon=coup):
                discount_price = total*int(coup.discount)/100
                total = total-(total*int(coup.discount)/100)
                
                flag = 2
                request.session['sub_total'] = total
                request.session['coupon_id'] = coup.id
                request.session['discount_price'] = discount_price

    data = {
        'total': total,
        'flag': flag,
        'discount_price': discount_price,

    }
    return JsonResponse(data)









def coupon_manage(request):
    coupons = Coupon.objects.all()
    return render(request,'admin/coupon_manage.html',{'coupons':coupons})

#admin delete coupon
def delete_coupon(request,id):
    print("DELETE")
    Coupon.objects.filter(id=id).delete()
    return redirect('coupon_manage')

#admin delete coupon
def edit_coupon(request,id):
    coupon=Coupon.objects.get(id=id)
    form=CouponApplyForm(request.POST,request.FILES,instance=coupon)
    if form.is_valid():
        form.save()
        return redirect('coupon_manage')
    else:
        form=CouponApplyForm(instance=coupon)
        return render(request,'admin/edit_coupon.html',{'coupon':coupon,'form':form})

#admin add coupon
def addCoupon(request): 
    if request.method=='POST': 
        print("if loop")
        form=CouponApplyForm(request.POST,request.FILES)
        if form.is_valid():
            print('working inner if')
            form.save()
            return redirect('coupon_manage')
        else:
            messages.info(request,'Coupon already exists')
            return redirect('addCoupon')
    else:
        print("else loop")
        form=CouponApplyForm()
        context={'form':form}
        return render(request,'admin/addCoupon.html',context)

