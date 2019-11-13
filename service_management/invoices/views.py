import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from enquiries.models import Enquiry
from .models import BankingDetail, Invoice, LineItem
from accounts.models import User

from service_management.utils import render_to_pdf,invoiceNumber

# Create your views here.
@login_required
def invoices_overview(request):
    template_name = 'invoices/invoices_list_main.html'
    qs = Invoice.objects.all()
    print(qs)

    context = {
        'obj':qs
    }
    return render(request,template_name,context)

@login_required
def invoices_details(request,pk):
    template_name = 'invoices/invoice_details.html'
    qs = get_object_or_404(Invoice,pk=pk)
    context = {
        'obj':qs
    }
    return render(request,template_name,context)

@login_required
def invoices_delete(request,pk):
    template_name = 'invoices/invoice_delete.html'
    qs = get_object_or_404(Invoice,pk=pk)    
    if request.method=='POST':
        qs.delete()
        messages.success(request,'Invoice has been successfully Deleted!')
        return redirect('invoices:overview')
    return render(request,template_name,{'obj':qs})


@login_required
def invoice_create(request,pk):
    template_name = 'invoices/invoice_create.html'
    qs = Enquiry.objects.get(pk=pk)
    bd = BankingDetail.objects.all()
    if qs.attended_to == 'un-attended':
        messages.error(request,'Enquiry status is un-attended, please attend to it before generating an invoice')
        return redirect('enquiries:enquiry_details',pk=pk)
    context ={
        'obj':qs,
        'bd':bd
    }
    return render(request,template_name,context)

@login_required
def invoice_save(request):
    if request.method=='POST':
        pk = request.POST.get('id')
        user = request.POST.get('assigned_to')
        sales_person = request.POST.get('assigned_to')
        banking_details_id = request.POST.get('banking_details')
        address = request.POST.get('address')
        title = request.POST.getlist('title')
        description = request.POST.getlist('description')
        unit_price = request.POST.getlist('unit_price')
        quantity = request.POST.getlist('quantity')
        company_name = request.POST.get('company_name')
        sales_person_ =get_object_or_404(User,username=user)
        enquiry = get_object_or_404(Enquiry,pk=pk)
        if title: 
            invoice_number =str(datetime.datetime.today()),          
            ic=Invoice.objects.create(
                enquiry=enquiry,
                sale_person=sales_person_,
                invoice_number =invoiceNumber(),
                total=400,
                company_name = company_name,
                address = address,
            )     
            if ic:
                c = min([len(title), len(description), len(unit_price), len(quantity)])
                id = ic.id
                invoice_number_ = ic.invoice_number[0]
                invoice_inst = get_object_or_404(Invoice,pk=id)
                lc_id = 0
                for i in range(c):
                    lc = LineItem.objects.create(
                        invoice = invoice_inst,
                        title = title[i],
                        quantity = quantity[i],
                        description = description[i],
                        unit_price = unit_price[i],
                        line_item_total = float(unit_price[i]) * float(quantity[i])
                    ) 
                    lc_id=lc.id
                if lc_id > 0:
                    line_items = LineItem.objects.filter(invoice=id)
                    total =0.0
                    for t in line_items:
                        total+= float(t.line_item_total)

                    data = {
                        'today': datetime.date.today(), 
                        'enquiry':enquiry,
                        'sale_person':sales_person_.first_name +' '+ sales_person_.last_name,
                        'invoice_number' :invoice_number_,
                        'company_name' :company_name,
                        'address' : address,
                        'line_items':line_items,  
                        'total' :total
                        }
                    pdf = render_to_pdf('invoices/quotation_template.html', data)
                    return HttpResponse(pdf, content_type='application/pdf')
                messages.error(request,'Line items not created please try again later or contact support.')
                return redirect('enquiries:enquiry_details',pk=pk)
            messages.error(request,'Quotation not created please try again later or contact support.')
            return redirect('enquiries:enquiry_details',pk=pk)
        messages.error(request,'Please add line item/s')
        return redirect('invoices:invoice_create',pk=pk)
    messages.error(request,'Not a Post method.')
    return redirect('dashboard:sales')



@login_required
def generate_pdf(request):
    data = {
        'today': datetime.date.today(), 
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
        }
    pdf = render_to_pdf('invoices/invoice_template.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
