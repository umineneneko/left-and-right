from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import State
from .models import Comment
from .models import Side

# Create your views here.
def index(request):
    #list1 = State.objects#.order_by('-pub_date')[:1]
    # = loader.get_template('states/index.html')
    #context = RequestContext(request, {
    #     'list': list1,
    # })
    #return HttpResponse(template.render(context))
    list1 = State.objects.order_by('-pub_date')
    list2 = Comment.objects.order_by('-pub_date')
    context = {'list': list1, 'comments': list2}
    return render(request, 'states/index.html', context)
    
def create_comment(request):
    if 'c' in request.POST and request.POST['c']:
        state = get_object_or_404(State, pk=request.POST['id'])
        side = get_object_or_404(Side, pk=request.POST['t'])
        #TODO: move to model
        n = Comment(state = state, side = side, text = request.POST['c'], by = request.POST['by'])
        n.save(force_insert=True)
    return  index(request)
    
    
def create_state(request):
    if 's' in request.POST and request.POST['s']:
        #TODO: move to model
        n = State(text = request.POST['s'], by = request.POST['by'])
        n.save(force_insert=True)
    return  index(request)
    
