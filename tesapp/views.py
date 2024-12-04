from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404

from django.core.exceptions import PermissionDenied

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .models import Photo,File,contact

from django.shortcuts import render


class PhotoListView(ListView):

    model = Photo     

    template_name = 'tesapp/list.html'

    context_object_name = 'photos'

from django.views.generic import ListView
from .models import File

class FileListView(ListView):
    model = File
    template_name = 'tesapp/articles.html'
    context_object_name = 'files'

def team_view(request):
    return render(request, 'tesapp/team.html')


class PhotoTagListView(PhotoListView):

    template_name = 'tesapp/taglist.html'

    # Custom method
    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context

# photoapp/views.py



class PhotoDetailView(DetailView):

    model = Photo

    template_name = 'tesapp/detail.html'

    context_object_name = 'photo'




class PhotoCreateView(LoginRequiredMixin, CreateView):

    model = Photo

    fields = ['title', 'description', 'image', 'tags']

    template_name = 'tesapp/create.html'

    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):

        form.instance.submitter = self.request.user

        return super().form_valid(form)


class UserIsSubmitter(UserPassesTestMixin):

    # Custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))

    def test_func(self):

        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')


class PhotoUpdateView(UserIsSubmitter, UpdateView):

    template_name = 'tesapp/update.html'

    model = Photo

    fields = ['title', 'description', 'tags']

    success_url = reverse_lazy('photo:list')

class PhotoDeleteView(UserIsSubmitter, DeleteView):

    template_name = 'tesapp/delete.html'

    model = Photo

    success_url = reverse_lazy('photo:list')  

from django.shortcuts import render
from .models import Photo

def homeview(request):
    # Retrieve all Photo objects
    photos = Photo.objects.all()
    files = File.objects.all()
    context = {'photos': photos, 'files': files}


    return render(request, 'tesapp/home.html' , context)







from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm,SubscriberForm  # Import the ContactForm class from forms.py

from .models import contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            
            # Save the data into the database
            new_contact = contact(name=name, message=message)
            new_contact.save()

            # Assuming you have sent a success message, you can use it like this:
            success_message = "Thank you for your message!"
            return render(request, 'tesapp/home.html', {'success_message': success_message})
    else:
        form = ContactForm()

    return render(request, 'tesapp/home.html', {'form': form})


from django.http import JsonResponse
from .models import Subscriber

def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from the form
        subscriber = Subscriber(email=email)
        subscriber.save()
        return JsonResponse({'message': 'Subscription successful'})

    return render(request, 'subscribe.html')  # Render the form initially





'tesapp/list.html' 
'tesapp/subscribe.html' 
'tesapp/home.html' 
'tesapp/articles.html' 
'tesapp/taglist.html' 
'tesapp/detail.html' 
'tesapp/create.html' 
'tesapp/update.html' 
'tesapp/delete.html'
'tesapp/success.html'