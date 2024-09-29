from django.shortcuts import render
from .models import Question

def quiz_view(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        answers = request.POST
        personality = calculate_personality(answers)
        return render(request, 'quiz/result.html', {'personality': personality})
    
    return render(request, 'quiz/quiz.html', {'questions': questions})
    print(request.POST)

def calculate_personality(answers):
    personality_scores = {'introvert': 0, 'extrovert': 0, 'creative': 0, 'analytical': 0}

    for key, value in answers.items():
        if value == 'introvert':
            personality_scores['introvert'] += 1
        elif value == 'extrovert':
            personality_scores['extrovert'] += 1
        elif value == 'creative':
            personality_scores['creative'] += 1
        elif value == 'analytical':
            personality_scores['analytical'] += 1

    # Determine the dominant personality type
    return max(personality_scores, key=personality_scores.get)






