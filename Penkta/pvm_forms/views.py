from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Form, PvmForm
from .forms import PvmFormNewForm, MainFormNewForm
from django.shortcuts import redirect

from xhtml2pdf import pisa


@login_required
def index(request):
    forms_list = Form.objects.filter(atsakingas_darbuotojas=request.user).order_by('-formos_data')

    if request.method == 'POST':
        new_form = MainFormNewForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            return redirect('pvm_forms:index')
    else:
        new_form = MainFormNewForm()

    template = loader.get_template('pvm_forms/index.html')
    context = {
        'new_form': new_form,
        'forms_list': forms_list,
        'user': request.user
    }
    return HttpResponse(template.render(context, request))


@login_required
def form_detail(request, form_id):
    form = Form.objects.get(id=form_id)

    if request.method == 'POST':
        new_pvm_form = PvmFormNewForm(request.POST)
        if new_pvm_form.is_valid():
            temp_form = new_pvm_form.save(commit=False)
            temp_form.forma = form
            temp_form.kaina = temp_form.suma / temp_form.kiekis
            temp_form.save()
            return redirect('pvm_forms:form_detail', form_id=form_id)
    else:
        new_pvm_form = PvmFormNewForm()

    template = loader.get_template('pvm_forms/form.html')
    context = {
        'form': form,
        'new_pvm_form': new_pvm_form
    }
    return HttpResponse(template.render(context, request))

@login_required
def raw_table(request, form_id):
    form = Form.objects.get(id=form_id)

    sum = 0
    for pvmForm in form.pvmforms.all():
        sum += pvmForm.suma

    template = loader.get_template('pdfTemplate.html')
    context = {
        'form': form,
        'total_sum': sum
    }
    return HttpResponse(template.render(context, request))

@login_required
def form_pdf(request, form_id):
    form = Form.objects.get(id=form_id)

    sum = 0
    for pvmForm in form.pvmforms.all():
        sum += pvmForm.suma

    template = loader.get_template('pdfTemplate.html')
    context = {
        'form': form,
        'total_sum': sum
    }
    html = template.render(context, request)
    pdf_document = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), pdf_document)
    if not pdf.err:
        return HttpResponse(pdf_document.getvalue(), content_type='application/pdf')
    return None
