from django.shortcuts import render, redirect
from .models import NoteImage
from .forms import NoteImageForm


# Create your views here.
def image_list(request):
    images = NoteImage.objects.all()
    return render(request, 'upload_notes/image_list.html', {'images': images})

def image_upload(request):
    if request.method == 'POST':
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = NoteImageForm()
    return render(request, 'upload_notes/image_form.html', {'form': form})