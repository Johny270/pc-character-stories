from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class CharacterCreate(LoginRequiredMixin, CreateView):
  model = Character
  fields = ['name', 'tv_show', 'description']
  success_url = '/characters/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CharacterUpdate(LoginRequiredMixin, UpdateView):
  model = Character
  fields = ['tv_show', 'description']

class CharacterDelete(LoginRequiredMixin, DeleteView):
  model = Character
  success_url = '/characters/'

class Home(LoginView):
  template_name = 'home.html'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def character_index(request):
  characters =  Character.objects.filter(user=request.user)
  return render(request, 'characters/index.html', { 'characters': characters })

@login_required
def character_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  return render(request, 'characters/detail.html', { 'character': character })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context ={'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)