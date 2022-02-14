from django.shortcuts import render
from feedback_consulta.models import Feedback_consulta

def feedback_consulta(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        print(feedback)
        feedback_consulta = Feedback_consulta.objects.create(feedback=feedback)
        print(feedback_consulta)
        
        return render(request, 'feedback/feedback_consulta.html')
    else:
        return render(request, 'feedback/feedback_consulta.html')