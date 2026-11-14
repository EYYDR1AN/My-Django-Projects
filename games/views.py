from django.shortcuts import render

def home(request):
    return render(request, 'games/home.html')

def blimp_jump(request):
    return render(request, 'games/blimp.html')

def automation_attack(request):
    return render(request, 'games/automation.html')

def whack_mole(request):
    return render(request, 'games/whack.html')

def memory_matching(request):
    return render(request, 'games/memory.html')