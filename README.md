# NegozioDellUsato-ExamIS
Progetto per l'attività didattica: Ingegneria del Software 2021/2022 UNIVPM 

WINDOWS INSTALLATION ##################################################################

L'intallazione su windows può essere effettuata facilmente.

Premi il segno WIN sulla tastiera e digita "cmd", ti si apre il "promt dei comandi".

Posizionati nella cartella dove hai scaricato il file seguendo il percorso, ...\UsatoBeatoFiles\UsatoBeatoPython, nel mio caso risulta cosi:
![percorso dove laciare pyin windows](https://user-images.githubusercontent.com/95302292/217619795-9410c31d-2464-42e8-a56e-a96f2aac93a7.png)

Tramite il comando:
> pip list

verifica che hai presente tutte le seguente librerie e se mancano installe tramite il comando:

> pip install NOMELIBRERIA

![librerienecessarie](https://user-images.githubusercontent.com/95302292/217621016-6d8da044-1c86-4a1f-a2a8-1329b887e9e9.png)

Lancia il comando:

> pip intall pyinstaller

Ora se il pyinstaller è stato installato correttamente e se non mancano le librerie necessarie, per generare l'eseguibile lancia il comando:

> pyinstaller UsatoBeato.py --onefile

Lanciato il comando del pyinstaller, taglia la cartella chiamata "resourcesForUsatoBeato" che si trova nella cartella "UsatoBeatoFiles"e incollala nella cartella "UsatoBeatoPython\dist". 
La cartella "dist" è stata generata con un eseguibile all'interno chiamato "UsatoBeato.exe", tale eseguibile ha bisogno della cartella "resourcesForUsatoBeato" per
funzionare
