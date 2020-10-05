from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DocumentForm

# Create your views here.

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('successful')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload.html', {'form':form})
