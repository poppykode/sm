import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from enquiries.models import Enquiry
from .models import BankingDetail, Invoice, LineItem
from accounts.models import User

from service_management.utils import render_to_pdf, invoiceNumber

# Create your views here.
@login_required
def invoices_overview(request):
    template_name = 'invoices/invoices_list_main.html'
    qs = Invoice.objects.filter(type="quotation")
    type_ = 'Quotations'
    context = {
        'obj': qs,
        'type_': type_
    }
    return render(request, template_name, context)


@login_required
def quotations_overview(request):
    template_name = 'invoices/invoices_list_main.html'
    qs = Invoice.objects.filter(type="invoice")
    type_ = 'Invoices'
    context = {
        'obj': qs,
        'type_': type_
    }
    return render(request, template_name, context)


@login_required
def invoices_details(request, pk):
    template_name = 'invoices/invoice_details.html'
    qs = get_object_or_404(Invoice, pk=pk)
    context = {
        'obj': qs
    }
    return render(request, template_name, context)


@login_required
def invoices_delete(request, pk):
    template_name = 'invoices/invoice_delete.html'
    qs = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        qs.delete()
        messages.success(request, 'Invoice has been successfully Deleted!')
        return redirect('invoices:overview')
    return render(request, template_name, {'obj': qs})

# creating an quotation
@login_required
def invoice_create(request, pk):
    template_name = 'invoices/quotation_create.html'
    qs = Enquiry.objects.get(pk=pk)
    bd = BankingDetail.objects.all()
    if qs.attended_to == 'un-attended':
        messages.error(
            request, 'Enquiry status is un-attended, please attend to it before generating an invoice')
        return redirect('enquiries:enquiry_details', pk=pk)
    context = {
        'obj': qs,
        'bd': bd
    }
    return render(request, template_name, context)

# creating an invoice
@login_required
def quotation_create(request):
    template_name = 'invoices/invoice_create.html'
    bd = BankingDetail.objects.all()
    context = {
        'obj': bd,
    }
    return render(request, template_name, context)


def generate_pdf(request,pk):
    qs = get_object_or_404(Invoice,pk=pk)
    if qs:
        line_items = LineItem.objects.filter(invoice=pk)
        total = 0.0
        for t in line_items:
            total += float(t.line_item_total)
        data = {
            'today': datetime.date.today(),
            'enquiry': qs.title,
            'sale_person': qs.sale_person.first_name + ' ' + qs.sale_person.last_name,
            'invoice_number': qs.invoice_number,
            'company_name': qs.company_name,
            'address': qs.address,
            'line_items': line_items,
            'type': qs.type,
            'total': total
        }
        pdf = render_to_pdf(
            'invoices/quotation_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


@login_required
def quotation_save(request):
    if request.method == 'POST':
        type_ = request.POST.get('type')
        address = request.POST.get('address')
        banking_details = request.POST.get('banking_details')
        assigned_to = request.POST.get('assigned_to')
        company_name = request.POST.get('company_name')
        title = request.POST.getlist('title')
        description = request.POST.getlist('description')
        unit_price = request.POST.getlist('unit_price')
        quantity = request.POST.getlist('quantity')
        Invoice_for_title = request.POST.get('Invoice_for_title')
        sales_person_ = get_object_or_404(User, username=assigned_to)
        invoice_number = invoiceNumber()
        if title:
            ic = Invoice.objects.create(
                sale_person=sales_person_,
                invoice_number=invoice_number,
                total=0,
                company_name=company_name,
                address=address,
                type=type_,
                title=Invoice_for_title,
            )
            if ic:
                c = min([len(title), len(description),
                         len(unit_price), len(quantity)])
                id = ic.id
                invoice_number_ = ic.invoice_number[0]
                invoice_inst = get_object_or_404(Invoice, pk=id)
                lc_id = 0
                for i in range(c):
                    lc = LineItem.objects.create(
                        invoice=invoice_inst,
                        title=title[i],
                        quantity=quantity[i],
                        description=description[i],
                        unit_price=unit_price[i],
                        line_item_total=float(
                            unit_price[i]) * float(quantity[i])
                    )
                    messages.success(request,'Invoice successfully created')
                    return redirect('invoices:quotations_overview')
                    # lc_id = lc.id
                # if lc_id > 0:
                #     line_items = LineItem.objects.filter(invoice=id)
                #     total = 0.0
                #     for t in line_items:
                #         total += float(t.line_item_total)
                #     print(ic.invoice_number)
                #     data = {
                #         'today': datetime.date.today(),
                #         'enquiry': 'n/a',
                #         'sale_person': sales_person_.first_name + ' ' + sales_person_.last_name,
                #         'invoice_number': invoice_number,
                #         'company_name': company_name,
                #         'address': address,
                #         'line_items': line_items,
                #         'type': type_,
                #         'total': total
                #     }
                #     pdf = render_to_pdf(
                #         'invoices/quotation_template.html', data)
                #     return HttpResponse(pdf, content_type='application/pdf')
                messages.error(
                    request, 'Line items not created please try again later or contact support.')
                return redirect('invoices:quotation_create')
            messages.error(
                request, 'Quotation not created please try again later or contact support.')
            return redirect('invoices:quotation_create')
        messages.error(request, 'Please add line item/s')
        return redirect('invoices:quotation_create')
    messages.error(
        request, 'Something went wrong please contact System Admin.')
    return redirect('invoices:quotation_create')


@login_required
def invoice_save(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        user = request.POST.get('assigned_to')
        banking_details_id = request.POST.get('banking_details')
        address = request.POST.get('address')
        title = request.POST.getlist('title')
        description = request.POST.getlist('description')
        unit_price = request.POST.getlist('unit_price')
        quantity = request.POST.getlist('quantity')
        company_name = request.POST.get('company_name')
        type_ = request.POST.get('type')
        sales_person_ = get_object_or_404(User, username=user)
        enquiry = get_object_or_404(Enquiry, pk=pk)
        if title:
            ic = Invoice.objects.create(
                enquiry=enquiry,
                sale_person=sales_person_,
                invoice_number=invoiceNumber(),
                total=400,
                company_name=company_name,
                address=address,
                type=type_,
            )
            if ic:
                c = min([len(title), len(description),
                         len(unit_price), len(quantity)])
                id = ic.id
                invoice_number_ = ic.invoice_number[0]
                invoice_inst = get_object_or_404(Invoice, pk=id)
                lc_id = 0
                for i in range(c):
                    lc = LineItem.objects.create(
                        invoice=invoice_inst,
                        title=title[i],
                        quantity=quantity[i],
                        description=description[i],
                        unit_price=unit_price[i],
                        line_item_total=float(
                            unit_price[i]) * float(quantity[i])
                    )
                    lc_id = lc.id
                if lc_id > 0:
                    line_items = LineItem.objects.filter(invoice=id)
                    total = 0.0
                    for t in line_items:
                        total += float(t.line_item_total)

                    data = {
                        'today': datetime.date.today(),
                        'enquiry': enquiry,
                        'sale_person': sales_person_.first_name + ' ' + sales_person_.last_name,
                        'invoice_number': invoice_number_,
                        'company_name': company_name,
                        'address': address,
                        'line_items': line_items,
                        'type': type_,
                        'total': total
                    }
                    pdf = render_to_pdf(
                        'invoices/quotation_template.html', data)
                    return HttpResponse(pdf, content_type='application/pdf')
                messages.error(
                    request, 'Line items not created please try again later or contact support.')
                return redirect('enquiries:enquiry_details', pk=pk)
            messages.error(
                request, 'Quotation not created please try again later or contact support.')
            return redirect('enquiries:enquiry_details', pk=pk)
        messages.error(request, 'Please add line item/s')
        return redirect('invoices:invoice_create', pk=pk)
    messages.error(request, 'Not a Post method.')
    return redirect('dashboard:sales')

