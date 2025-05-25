"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin# Importa il modulo admin di Django per gestire l'interfaccia di amministrazione
from django.urls import path# Importa la funzione path per definire le URL del progetto
from todo import views# Importa le viste dal modulo corrente (todo_list/todo/views.py)
from django.urls import path, include# Importa la funzione include per includere altri URLconf nel progetto

urlpatterns = [
    path('admin/', admin.site.urls),# Questa riga definisce l'URL per l'interfaccia di amministrazione di Django
    # Quando un utente visita l'URL 'admin/', viene reindirizzato all'interfaccia di amministrazione
    # admin.site.urls è l'URL predefinito per l'interfaccia di amministrazione di Django
    # Per accedere all'interfaccia di amministrazione, l'utente deve essere autenticato come superuser
    # e avere i permessi necessari per gestire il sito.

    path('', views.task_list, name='task_list'),# Questa riga definisce l'URL per la vista della lista dei task
    # Quando un utente visita l'URL '', viene reindirizzato alla vista task_list
    # views.task_list è la funzione che gestisce la visualizzazione della lista dei task
    # name='task_list' è il nome dell'URL, che può essere utilizzato per fare riferimento a questa vista in altre parti del codice
    # come nei template o nei redirect. Questo nome può essere utilizzato per creare link dinamici
    # all'interno del progetto Django, ad esempio con il tag {% url 'task_list' %} nei template.
    # In questo caso, l'URL vuoto ('') corrisponde alla radice del sito web, quindi quando un utente visita il sito,
    # verrà visualizzata la lista dei task.

    path('delete/<int:pk>/', views.delete_task, name='delete_task'),# Questa riga definisce l'URL per eliminare un task specifico
    # <int:pk> indica che l'URL accetta un parametro intero chiamato 'pk' (primary key) per identificare il task da eliminare
    # Quando un utente visita l'URL 'delete/<int:pk>/', viene reindirizzato alla vista delete_task
    # views.delete_task è la funzione che gestisce l'eliminazione del task specifico
    # name='delete_task' è il nome dell'URL, che può essere utilizzato per fare riferimento a questa vista in altre parti del codice
    # come nei template o nei redirect. Questo nome può essere utilizzato per creare link dinamici
    # all'interno del progetto Django, ad esempio con il tag {% url 'delete_task' pk=task.id %} nei template.

    path('complete/<int:pk>/', views.complete_task, name='complete_task'),# Questa riga definisce l'URL per completare un task specifico
    # <int:pk> indica che l'URL accetta un parametro intero chiamato 'pk' (primary key) per identificare il task da completare
    # Quando un utente visita l'URL 'complete/<int:pk>/', viene reindirizzato alla vista complete_task
    # views.complete_task è la funzione che gestisce la marcatura del task come completato

    #path('', include('todo.urls')),#include l'URLconf del modulo todo, che contiene le URL specifiche per l'applicazione todo
    # 'todo.urls' è il modulo che contiene le URL specifiche per l'applicazione todo,
    #ma non è necessario specificare il percorso completo, poiché Django sa cercare le URL relative al modulo corrente
    #ma in questo progetto non è necessario includere 'todo.urls' poiché le URL sono già definite qui
    
    path('accounts/', include('django.contrib.auth.urls')), # # Include le URL per la gestione dell'autenticazione degli utenti
    # # Queste URL consentono agli utenti di registrarsi, effettuare il login, il logout e reimpostare la password
    # # Queste URL sono fornite da Django e possono essere utilizzate per gestire l'autenticazione degli utenti
    #tra queste URL ci sono:
    # 'login/', 'logout/', 'password_change/', 'password_change_done/', 'password_reset/', 'password_reset_done/', 'password_reset_confirm/', 'password_reset_complete/
    # 'password_reset_complete/ e 'password_reset_confirm/' sono le URL per la gestione della reimpostazione della password
    # 'password_change/' e 'password_change_done/' sono le URL per la gestione del cambio della password
    # # 'login/' e 'logout/' sono le URL per la gestione del login e del logout degli utenti
    # Queste URL sono utili per gestire l'autenticazione degli utenti e consentire loro di accedere alle funzionalità protette del sito
    # 'todo.urls' è il modulo che contiene le URL specifiche per l'applicazione todo,

    path('signup/', views.signup, name='signup'),  # ← ← ← AJOUT ICI
]


