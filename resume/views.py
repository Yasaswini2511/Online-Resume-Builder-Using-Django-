from django.shortcuts import render
from .forms import ResumeForm

def resume_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            return render(request, 'resume_template.html', {'form_data': form.cleaned_data})
    else:
        form = ResumeForm()

    return render(request, 'resume_form.html', {'form': form})

