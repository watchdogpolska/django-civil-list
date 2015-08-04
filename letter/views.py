from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.translation import ugettext as _

from .forms import SendLetter
from .models import Letter


def detail(request, pk):
    context = {}
    print request.POST
    object = get_object_or_404(Letter)
    if request.method == "POST":
        form = SendLetter(request.POST, instance=object)
        if form.is_valid():
            messages.success(request, _('Letter sent :-)'))
            form.send_mails()
        else:
            messages.warning(request, _('Letter warning :-)'))

    else:
        form = SendLetter(instance=object)
    context['form'] = form
    return render(request, 'letter/form.html', context)


def list(request):
    context = {}
    context['object_list'] = Letter.objects.all()

    return render(request, 'letter/list.html', context)
