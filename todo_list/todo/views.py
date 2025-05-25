from django.shortcuts import render, redirect # Importa le funzioni render e redirect per gestire le richieste HTTP
from .models import Task # Importa il modello Task per interagire con il database
from .forms import TaskForm # Importa il form TaskForm per gestire la creazione e la modifica dei task
from django.contrib.auth.decorators import login_required # Importa il decoratore login_required per proteggere le viste che richiedono l'autenticazione dell'utente 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


"""quindi questa vista è protetta e solo gli utenti autenticati possono accedervi.
Questa vista gestisce la visualizzazione della lista dei task e la creazione di nuovi task.
La vista task_list recupera tutti i task associati all'utente autenticato e li passa al template 'todo/task_list.html'.
Se la richiesta è di tipo POST, significa che l'utente sta cercando di creare un nuovo task."""
@login_required # Decoratore che richiede che l'utente sia autenticato per accedere alla vista
def task_list(request):
    # Recupera tutti i task associati all'utente autenticato
    #request.user è l'utente autenticato che ha effettuato il login
    #request contiene le informazioni sulla richiesta HTTP corrente come l'utente che ha effettuato la richiesta e molti altri dettagli. 
    # come il metodo della richiesta (GET, POST, etc.), i dati inviati, le intestazioni, ecc.
    tasks = Task.objects.filter(user=request.user) 
    # Crea un'istanza del form TaskForm
    # Il form viene utilizzato per creare nuovi task
    form = TaskForm()

    # Se la richiesta è di tipo POST, significa che l'utente sta cercando di creare un nuovo task
    # Se il metodo della richiesta è POST, significa che l'utente sta inviando dati per creare un nuovo task
    if request.method == 'POST':
        # Crea un'istanza del form con i dati inviati nella richiesta POST
        # request.POST contiene i dati inviati dal form
        # form.is_valid() verifica se i dati del form sono validi
        # Se il form è valido, salva il nuovo task associato all'utente autenticato
        # commit=False significa che non salviamo ancora il task nel database, ma lo prepariamo per ulteriori modifiche
        # Se il form non è valido, il task non viene salvato e l'utente rimane sulla stessa pagina con gli errori del form
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)# questo crea un'istanza del task ma non lo salva ancora nel database. ritorna un oggetto Task che non è ancora salvato.
            task.user = request.user# questo associa il task all'utente autenticato
            task.save() # Salva il task nel database
            return redirect('task_list')# Dopo aver salvato il task, reindirizza l'utente alla lista dei task. il parametro 'task_list' è il nome 
            #della vista che mostra la lista dei task

    return render(request, 'todo/task_list.html', {'tasks': tasks, 'form': form})#Renderizza il template 'todo/task_list.html' con i task e 
    #il form se la richiesta è di tipo GET o se il form non è valido.
    #i parametri di render sono:
    #request: la richiesta HTTP corrente
    #'todo/task_list.html': il template da renderizzare
    #{'tasks': tasks, 'form': form}: un dizionario che contiene i task e il form da passare al template quindi insomma quello che viene passato al template

@login_required
def delete_task(request, pk):# Questa vista gestisce l'eliminazione di un task specifico da un utente autenticato.
    # pk è l'identificatore del task da eliminare
    task = Task.objects.get(id=pk, user=request.user)# Recupera il task specifico associato all'utente autenticato
    # Se il task esiste, lo elimina
    task.delete()
    return redirect('task_list')# Reindirizza l'utente alla lista dei task dopo l'eliminazione

@login_required
def complete_task(request, pk):# Questa vista gestisce la marcatura di un task come completato per un utente autenticato.
    # pk è l'identificatore del task da completare
    task = Task.objects.get(id=pk, user=request.user)# Recupera il task specifico associato all'utente autenticato
    # Se il task esiste, lo segna come completato
    task.completed = True
    task.save()# Salva le modifiche al task nel database
    return redirect('task_list')# Reindirizza l'utente alla lista dei task dopo aver completato il task


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur
            return redirect('task_list')  # Redirige vers la page des tâches
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
