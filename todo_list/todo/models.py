from django.db import models
from django.contrib.auth.models import User# per importare il modello User di Django già esistente. quindi non è necessario creare un modello User personalizzato


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)# questo campo crea una relazione tra il modello Task e il modello User, 
    #permettendo di associare ogni task a un utente specifico. 
    #on_delete=models.CASCADE significa che se l'utente viene eliminato, anche i task associati verranno eliminati.
    # il campo user è una chiave esterna che collega ogni task a un utente specifico.

    title = models.CharField(max_length=255) # titolo del task.

    completed = models.BooleanField(default=False)# indica se il task è completato o meno. Il valore predefinito è False, 
    #quindi i task sono incompleti per impostazione predefinita.

    created_at = models.DateTimeField(auto_now_add=True)# indica la data e l'ora in cui il task è stato creato.

    def __str__(self):
        return self.title