# NegozioDellUsato-ExamIS
Progetto per l'attività didattica: Ingegneria del Software 2021/2022 UNIVPM 

## WINDOWS INSTALLATION ##################################################################

L'intallazione su windows può essere effettuata facilmente.

Premi il segno WIN sulla tastiera e digita "cmd", ti si apre il "promt dei comandi".

Posizionati nella cartella dove hai scaricato il file seguendo il percorso, ...\UsatoBeatoFiles\UsatoBeatoPython, nel mio caso risulta cosi:
![percorso dove laciare pyin windows](https://user-images.githubusercontent.com/95302292/217619795-9410c31d-2464-42e8-a56e-a96f2aac93a7.png)

Tramite il comando:
> pip list

verifica che hai presente tutte le seguente librerie e se mancano installe tramite il comando:

> pip install NOMELIBRERIA

ATTENZIONE: 

installando la libreria "yagmail" si installano automaticamente anche: "lxml", "cssutils", "cssselect", "cachetools", "premailer"

installando la libreria "PySide6" si installano automaticamente anche: "shiboken6", "PySide6-Essentials", "PySide6-Addons"

![librerienecessarie](https://user-images.githubusercontent.com/95302292/217621016-6d8da044-1c86-4a1f-a2a8-1329b887e9e9.png)

Lancia il comando:

> pip install pyinstaller

Ora se il pyinstaller è stato installato correttamente e se non mancano le librerie necessarie, per generare l'eseguibile lancia il comando:

> pyinstaller UsatoBeato.py --onefile

Lanciato il comando del pyinstaller, taglia la cartella chiamata "resourcesForUsatoBeato" che si trova nella cartella "UsatoBeatoFiles"e incollala nella cartella "UsatoBeatoPython\dist". 
La cartella "dist" è stata generata con un eseguibile all'interno chiamato "UsatoBeato.exe", tale eseguibile necessita della cartella "resourcesForUsatoBeato" per
funzionare. Per me la cartella deve risultare così:

![image](https://user-images.githubusercontent.com/95302292/217758517-3e84b8af-b8c3-4caa-bb5d-427192be6bad.png)

Se non hai saltato passaggi intermedi ti basta digitare all'interno del cmd "UsatoBeato.exe" se ti trovi nella cartella "dist" con il cmd.

![image](https://user-images.githubusercontent.com/95302292/217758280-73b12525-7d28-4cbb-acb2-e5116e2b2c00.png)

ENJOY!


## LINUX INSTALLATION

L'intallazione su linux prevede la stessa sequenza di pocedure,

Digitando "cmd" in linux si apre il terminale.

Su linux abbiamo pip3 invece di pip

pyinstaller è una libreria cross-plaform perciò disponibile su linux

## macOS INSTALLATION

Purtroppo la guida per l'installazione su macOS non è stata possibile in quanto è stato impossibile reperire la macchina. Tendo a precisare che pyinstaller è disponibile anche su macOS e PySide6 è una libreria compatibile con tale SO, l'installazione dovrebbe essere, se non identica, simile all'installazione sugli altri SO.
