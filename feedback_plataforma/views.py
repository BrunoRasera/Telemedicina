from django.shortcuts import render
from feedback_plataforma.models import Feedback_plataforma

def feedback_plataforma(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        print(feedback)
        feedback_plataforma = Feedback_plataforma.objects.create(feedback=feedback)
        print(feedback_plataforma)
        
        return render(request, 'feedback/feedback_plataforma.html')
    else:
        return render(request, 'feedback/feedback_plataforma.html')