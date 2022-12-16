from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from  django.shortcuts  import  render    
from  django.http  import  HttpResponse, HttpResponseRedirect    
from  .functions  import  handle_uploaded_file    
from  account.forms  import UploadFileForm   


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



# Create your views here.
def upload_file(request):
     #render the upload_file.html template
    return render(request, "file_upload/upload_file.html")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            form.save()
            return HttpResponse('''
            <h1>File uploaded successfully</h1>
            <a href="/account/upload_file/">Upload another file</a>
            ''')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload_file.html', {'form': form})