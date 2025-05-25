from django import forms
from .models import Task

"""questo file contiene i form per il modello Task.
I form sono utilizzati per creare e modificare i task.
Il form TaskForm è un ModelForm che consente di creare un form basato sul modello Task.
Il form include solo il campo 'title', che è il titolo del task.
Il campo 'title' è un campo di tipo CharField, che consente di inserire una stringa di testo.
Il form TaskForm può essere utilizzato in una vista per gestire la creazione e la modifica dei task.
Il form TaskForm è una classe che eredita da forms.ModelForm,
e specifica il modello Task come modello di base.
"""
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']