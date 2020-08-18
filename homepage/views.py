from django.shortcuts import render
from homepage.forms import CowsayForm
from homepage.models import CowsayText
import subprocess


def index_view(request):
    if request.method == 'POST':
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsayText.objects.create(
                text=data.get('cowsayify'),
            )
            process = subprocess.run(
                ['cowsay', data.get('cowsayify')],
                capture_output=True,
                universal_newlines=True
            )
            form = CowsayForm()
            return render(request, 'index.html', {
                'form': form,
                'cow': process.stdout
            })

    form = CowsayForm()
    return render(request, 'index.html', {'form': form})


def history_view(request):
    # https://stackoverflow.com/a/1133736
    latest_ten = CowsayText.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'history': latest_ten})
