from django.shortcuts import render,redirect
from django.db.models import Count, Q
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Sum
from .models import Category,Enquiry1,Packagess
from .forms import EnquiryForm
from django.contrib.auth import views as auth_views
from django.http import JsonResponse

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def homepage(request):
	return render(request,"homepage.html",{})
def about(request):
	return render(request,"about.html",{})
def gallery(request):
	return render(request,"gallery.html",{})

def app_new(request):
	if request.method == "POST":
		form = EnquiryForm(request.POST)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('homepage')
			
	else:
		form = EnquiryForm()
	return render(request, 'post_edit.html', {'form': form})

def familytour(request):
	categoryf= Packagess.objects.filter(real_category='Family Tours')
	return render(request,'familytour.html',{'categoryf': categoryf})

def religioustour(request):
	categoryr= Packagess.objects.filter(real_category='Religious Tours')
	return render(request,'religioustour.html',{'categoryr': categoryr})

def solotrip(request):
	categorys= Packagess.objects.filter(real_category='Solo Trip')
	return render(request,'solotrip.html',{'categorys': categorys})

def adventuretour(request):
	categorya= Packagess.objects.filter(real_category='Adventure Tours')
	return render(request,'adventuretour.html',{'categorya': categorya})

def graph(request):
	return render(request, 'graph.html')

def column_chart(request):
	dataset = Enquiry1.objects.values('Category').annotate(survived_count=Count('Category', filter=Q(Gender='M')),not_survived_count=Count('Category', filter=Q(Gender='F')))
	return render(request, 'column_chart.html', {'dataset': dataset})
def card1(request):
    labels = []
    data = []

    queryset =  Packagess.objects.values('category__packagess').annotate(category_price=Sum('price')).order_by('-category_price')
    for entry in queryset:
        labels.append(entry['category__packagess'])
        data.append(entry['category_price'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
def pie_chart(request):
    return render(request, 'pie_chart.html')

CATEGORY_CHOICES = (('B','Family Tours'),('R','Religious Tours'),('S','Solo Trips'),('A','Adventure Trips'))

def chart_data(request):
    dataset = Enquiry1.objects.values('Category').exclude(Category='').annotate(total=Count('Category'))

    port_display_name = dict()
    for port_tuple in CATEGORY_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Enquiries received per Category'},
        'series': [{
            'name': 'Category',
            'data': list(map(lambda row: {'name': port_display_name[row['Category']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

"""def ticket_class_view(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'ticket_class.html', {'dataset': dataset})"""