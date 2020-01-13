import random
import string
import datetime
from projects.models import ProjectInstallationAssessement,Task
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        print(pdf.err)
    return None


def invoiceNumber(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    quotation_number = ''.join(random.choice(letters)
                               for i in range(stringLength))
    date = str(datetime.datetime.today().year)
    inv = 'SS-' + quotation_number.upper() + '-'+date
    print(date)
    return inv


