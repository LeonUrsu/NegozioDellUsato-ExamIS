
**1 DESCRIZIONE IN LINGUAGGIO NATUREALE**


Il progetto proposto consiste nella realizzazione di un sistema informativo per la gestione di un Negozio dell'usato.

REGISTRAZIONE UTENTE

Il cliente-proprietario arrivato al negozio, in caso non sia già stata effettuata la registrazione precedentemente, dovrà registrarsi insieme all’amministratore. Fornendo i propri dati personali, la propria e-mail e la password concordata con l’amministratore; gli verrà assegnato un codice cliente. A registrazione effettuata, il sistema invierà un’e-mail di registrazione effettuata con successo, dove verranno indicati i rispettivi dati di registrazione per l’accesso locale al sistema.

ACCETTAZIONE OGGETTO

Solo se già registrato, il cliente-proprietario consegnerà l'oggetto destinato alla vendita, al cassiere(amministratore), il quale provvederà ad inserirlo nel sistema, compilando i dati dell'oggetto: nome categoria, id cliente-proprietario, data di registrazione e il prezzo iniziale che verrà concordato da ambo le parti (il cassiere e il cliente-proprietario). 

L'oggetto rimarrà in vendita per un massimo di 5 mesi:
\- Al secondo mese dalla data di registrazione il prezzo iniziale del prodotto subirà un decremento del 30%.
\- Al terzo mese dalla data di registrazione il prezzo iniziale del prodotto subirà un decremento del 40%.
\- Al quarto mese dalla data di registrazione il prezzo iniziale del prodotto subirà un decremento del 50%.
\- Al quinto mese dalla data di registrazione il prodotto verrà eliminato dalla lista di oggetti disponibili.

VENDITA OGGETTO

Al momento della vendita l’amministratore effettuerà la ricerca dell’oggetto nel sistema effettua la vendita dell’oggetto con il prezzo di vendita. La data e ora di vendita viene acquisita automaticamente. L’oggetto venduto viene rimosso dalla lista degli oggetti disponibili e viene archiviato. Inoltre, verrà inoltrata un’e-mail per notificare la vendita del prodotto al corrispettivo cliente-proprietario.

ALTRE FUNZIONALITA’

Il cliente-acquirente, non sarà vincolato dalla registrazione, potrà visualizzare l'intera lista di prodotti disponibili ed avrà a disposizione strumenti per effettuare filtraggio in base alle proprie preferenze (categoria, prezzo, data).

L’amministratore avrà a disposizione degli strumenti per visualizzare delle statistiche sui prodotti venduti e sul numero di clienti avendo modo così di analizzare l’andamento della propria attività commerciale. Inoltre, avrà anche la possibilità di effettuare un backup manualmente.

Alla fine della giornata lavorativa il sistema dovrà essere chiuso per effettuare la creazione delle statistiche e un backup dei dati, e che consisterà nel copiare tutti i dati che
costituiscono il database, sul disco, al fine di riparare a eventuali perdite di dati o anomalie.

1. **GLOSSARIO DEI TERMINI**

**2 ANALISI DEI REQUISITI**

Dall’analisi della documentazione prodotta durante le interviste con gli stakeholder, sono stati individuati dei requisiti che fungeranno come vincoli da rispettare durante la progettazione del sistema. Essi sono suddivisi in *requisiti funzionali* e *requisiti non funzionali.* I primi sono delle caratteristiche che il sistema deve garantire all’utilizzatore mentre i secondi sono dei vincoli imposti dal sistema.

**2.1 REQUISITI DEL SISTEMA**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.001.png)

Figura NUMERO: Distribuzione dei package dei requisiti

**2.1.1 REQUISITI FUNZIONALI**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.002.png)

Figura NUMERO: Diagramma dei requisiti funzionali


**RF1 –** Genera Statistiche

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

*Il sistema dovrà effettuare un backup dei dati* 

**RF2 -** Backup

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà gestire la scadenza dei prodotti non venduti

**RF3 –** Scadenza Prodotto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà gestire la scadenza dei prodotti non venduti

**RF4 -** Notifica Registrazione Cliente

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà notificare al cliente la propria registrazione

**RF5 -** Notifica Vendita Prodotto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà notificare al cliente la vendita del proprio oggetto

**RF6 -** Vendita Prodotto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneAmministratore*

Il sistema dovrà notificare al cliente la vendita del proprio oggetto

**RF5 -** Notifica Prodotto Scaduto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà notificare al cliente la scadenza dell’oggetto

**RF6 -** Vendita Prodotto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneAmministratore*

Il sistema dovrà permettere all’Amministratore di vendere un prodotto

**RF7 -** CRUD Prodotto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneAmministratore*

Il sistema dovrà essere in grado di effettuare operazioni CRUD sul prodotto

**RF8 -** CRUD Ricevuta

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà essere in grado di effetturare operazioni CRUD sulla ricevuta

**RF9 -** CRUD Cliente-Proprietario

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneAmministratore*

Il sistema dovrà effettuare operazioni CRUD sul Cliente-Proprietario

**RF10 -** Visualizza Statistiche

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneAmministratore*

Il sistema dovrà poter visualizzare statististiche sul prodotto

**RF11 -** Filtraggio Prodotto Per Data

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneUser*

Il sistema dovrà effettuare il filtraggio dei prodotti con la data di inserimento

**RF12 -** Filtraggio Prodotto Per Prezzo

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneUser*

Il sistema dovrà effettuare il filtraggio dei prodotti con il loro prezzo corrente

**RF13 -** Filtraggio Prodotto Per Categoria

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneUser*

Il sistema dovrà effettuare il filtraggio dei prodotti con la loro categoria

**RF14 -** Login

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneUser*

Il sistema dovrà permettere di effettuare il login

**RF15 -** Notifica Prodotto Scaduto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà notificare al cliente che il suo prodotto è scaduto

**RF16 -** Statistiche Prodotti Venduti

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà effettuare statistiche su prodotti venduti

**RF17 –** Visualizza Info Account

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneCliente-proprietario*

Il sistema dovrà permettere di visualizzare le info del proprio account

**RF18 –** Visualizza Prodotti Propri

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneCliente-proprietario*

Il sistema dovrà permettere di visualizzare i propri prodotti presenti nel sistema

**RF19 –** Backup Manuale

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneAmministratore*

Il sistema dovrà permettere all’Amministratore di effettuare un backup manuale

**RF20 -** Visualizza Prodotto

*Type:* **Requirement**

*Status:* proposed

*Package: GestioneSistema*

Il sistema dovrà permettere di visualizzare e info di un prodotto


**2.1.2 REQUISITI NON FUNZIONALI**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.003.png)

Figura NUMERO: Diagramma dei requisiti non funzionali


**RNF1 -** Usare Python 3

*Type:* **Requirement**

*Status:* proposed

*Package:* Requisiti non funzionali

Il sistema dovrà essere implementato in Python 3

**RNF2 -** Password

*Type:* **Requirement**

*Status:* proposed

*Package:* Requisiti non funzionali* 

Il sistema dovrà poter gestire una password

**RNF3 -** Convalida Password

*Type:* **Requirement**

*Status:* proposed

*Package:* Requisiti non funzionali

Il sistema dovrà effettuare la convalida della password

**2.2 DIAGRAMMI DEI CASI D’USO**

Casi d’uso del sistema, scenari che si possono verificare durante l’esecuzione del sistema.

I seguenti diagrammi sono stati suddivisi in base alle varie aree di interazione da parte degli attori con il sistema in uso, in modo da rendere indipendenti dove è possibile le interazioni dei vari attori con il sistema.

**2.2.1 ATTORI**

Nella figura NUMERO vi è il diagramma con gli attori individuati durante l’analisi, gli attori: Amministratore e Cliente-Proprietario sono delle generalizzazioni dell’attore User, ciò significa che potranno trovarsi nelle situazioni dell’attore User.

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.004.png)

Figura NUMERO: Diagramma degli attori

**2.2.2 GESTIONE AMMINISTRATORE** 

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.005.png)

Figura NUMERO: Diagramma Gestione Amministratore



|Caso d’uso: CreateRicevuta|
| :- |
|ID: 1|
|Descrizione: Questo caso d’uso permette di effettuare operazioni di creazione di una ricevuta|
|Attori primari: Amministratore|
|Attori secondari: nessuno|
|Precondizioni: l’Amministratore ha venduto dei prodotti|
|<p>Sequenza eventi principali:</p><p>1. il caso d’uso inizia quando sono stati venduti dei prodotti</p><p>2. **il sistema crea la ricevuta**</p><p>3. il sistema aggiunge i prodotti nella ricevuta</p><p>4. il sistema stampa la ricevuta</p><p> </p>|
|<p>Postcondizioni: nessuna</p><p></p>|
|<p>Sequenza degli eventi alternativa: nessuna</p><p></p>|

























|Caso d’uso: CRUDClienteP|
| :- |
|ID: 2|
|Descrizione: Questo caso d’uso permette di effettuare operazioni CRUD sul ClienteProprietario|
|Attori primari: Amministratore|
|Attori secondari: ClienteProprietario|
|Precondizioni: l’amministratore del sistema desidera effettuare operazioni CRUD per un ClienteProprietario|
|<p>Sequenza eventi principali:</p><p>1. il caso d’uso inizia quando l’attore primario desidera effettuare un</p><p>operazione CRUD di un ClienteProprietario</p><p>2. **if** l’Amministratore vuole inserire nel database un ClienteP</p><p>2.1 **include** (:RicercaCliente)</p><p>2.2 **if** il cliente risulta esistente nel sistema</p><p>2.2.1 il sistema restituisce un errore</p><p>2.3 **else**</p><p>2.3.1 L’Amministratore inserisce i dati del ClienteP nel database</p><p>2.3.2 il sistema memorizza i dati del cliente nel database</p><p>2.3.3 il sistema manda una notifica</p><p>3. **else if** l’amministratore vuole visualizzare un ClienteP</p><p>3.1 **include** (:RicercaCliente)</p><p>3.2 **if** il cliente risulta inesistente nel database</p><p>3.2.1 il sistema restituisce un errore</p><p>3.3 **else** il sistema mostra il cliente</p><p>4. **else if** l'amministratore vuole aggiornare i dati relativi ad un ClienteP</p><p>4.1. **include** (:RicercaCliente);</p><p>4.2. **if** il cliente risulta esistente nel database</p><p>4.2.1 l’amministratore specifica i nuovi dati</p><p>4.2.2. Il sistema aggiorna i dati del cliente nel database</p><p>4.3. **else**</p><p>3.3.1. il sistema restituisce un errore</p><p>5. **else if** l’amministratore vuole cancellare un ClienteP dal database</p><p>5.1 **include** (:RicercaCliente)</p><p>5.2 **if** il cliente risulta esistente nel database</p><p>5.2.1 **include** (:RicercaProdotto)</p><p>5.2.2 **while** (esistono prodotti del ClienteP)</p><p>5.2.2.1 il sistema elimina il prodotto</p><p>5.2.3 il sistema elimina il ClienteP dal database</p><p>5.3. **else**</p><p>5.3.1. il sistema restituisce un errore</p>|
|Postcondizioni: il sistema si rende nuovamente disponibile per altre operazioni|
|Sequenza degli eventi alternativa: nessuna|






|Caso d’uso: CRUDProdotto|
| :- |
|ID: 3|
|Descrizione: Questo caso d’uso permette di effettuare operazioni CRUD sul prodotto|
|Attori primari: Amministratore|
|Attori secondari: Nessuno|
|Precondizioni: l’Amministratore vuole effettuare un’operazione CRUD su un prodotto|
|<p>Sequenza eventi principali:</p><p>1. **if** l’amministratore vuole creare un prodotto</p><p>1.1 il sistema chiede di inserire i dati del prodotto da creare</p><p>1.2 L’Amministratore inserisce i dati del prodotto nel sistema</p><p>1.3 il sistema memorizza i dati del prodotto nel database</p><p>1.4 **if** prodotto inserito correttamente</p><p>1.4.1 il sistema comunica il successo dell’operazione</p><p>1.5 **else**</p><p>1.5.1 il sistema restituisce un errore</p><p>2. **else if** l’Amministratore primario vuole visualizzare il prodotto</p><p>2.1 **include** (:RicercaProdotto)</p><p>2.2 **if** prodotto trovato nel database</p><p>2.2.1 il sistema restituisce l’oggetto trovato</p><p>2.3 **else**</p><p>2.3.1 il sistema restituisce un errore</p><p>3. **else if** l'Amministratore primario vuole aggiornare i dati relativi ad un prodotto</p><p>3.1. **include** (:RicercaProdotto);</p><p>3.2. **if** il prodotto risulta esistente nel database</p><p>3.2.1 l’attore primario specifica i nuovi dati</p><p>3.2.2. Il sistema aggiorna i dati del prodotto nel database</p><p>3.3. **else**</p><p>3.3.1. il sistema restituisce un errore</p><p>4. **else if** l’Amministratore vuole cancellare il prodotto dal database</p><p>4.1 **include** (:RicercaProdotto)</p><p>4.2 **if** il prodotto risulta esistente nel database</p><p>4.2.1 il sistema elimina il prodotto dal database</p><p>4.3. **else**</p><p>4.3.1. il sistema restituisce un errore</p>|
|Postcondizioni: nessuna|
|Sequenza degli eventi alternativa: nessuna|








|Caso d’uso: Notifica|
| :- |
|ID: 4|
|<p>Descrizione: Invia una notifica al cliente registrato</p><p></p>|
|Attori primari: Amministratore|
|<p>Attori secondari: Nessuno</p><p></p>|
|<p>Precondizioni Segmento 1: L’utente è stato creato</p><p>Precondizioni Segmento 2: Il prodotto è stato rimosso</p><p>Precondizioni Segmento 3: Il prodotto è stato venduto</p><p></p>|
|<p>Sequenza eventi Segmento 1:</p><p>1. il caso d’uso inizia quando l’amministratore crea un nuovo Cliente Proprietario</p><p>2. il sistema invia una email al Cliente Proprietario</p><p>Sequenza eventi Segmento 2:</p><p>1. il caso d’uso inizia quando il Sistema rimuove il prodotto di un Cliente Proprietario</p><p>2. **if** il prodotto è stato venduto</p><p>2.1 il sistema invia una email al cliente proprietario con l’esito                                 della vendita</p><p>3.**else if** il tempo di vendita del prodotto è scaduto</p><p>3.1 il sistema invia una email al cliente proprietario indicando la scadenza del prodotto registrato</p><p>Sequenza eventi Segmento 3:</p><p>1. Il caso d’uso inizia quando il prodotto viene venduto</p><p>2. il sistema invia un’email al ClienteProprietario </p>|
|<p>Postcondizioni: Nessuna</p><p></p>|
|<p>Sequenza degli eventi alternativa: Nessuna</p><p></p>|


















|Caso d’uso: RicercaCliente|
| :- |
|ID: 5|
|Descrizione: Questo caso d’uso permette di effettuare la ricerca di un cliente nel sistema|
|Attori primari: Amministratore|
|Attori secondari: Cliente|
|Precondizioni: l’attore primario desidera effettuare una ricerca del cliente nel database|
|<p>Sequenza eventi principali:</p><p>1.  il caso d’uso inizia quando l’attore primario desidera effettuare la ricerca di un Cliente nel database del sistema</p><p>2. l’attore primario specifica i dati di ricerca</p><p>3. il sistema effettua la ricerca con i dati forniti dall’attore primario</p><p>4. **if** il Cliente è stato trovato</p><p>4.1 il sistema restituisce i dati del Cliente</p><p>5. **else**</p><p>5.1 il sistema restituisce un errore</p>|
|<p>Postcondizioni:</p><p>1. il sistema ha restituito dei dati</p>|
|<p>Sequenza degli eventi alternativa: nessuna</p><p></p>|
































|Caso d’uso: RicercaProdotto|
| :- |
|ID: 6|
|Descrizione: Questo caso d’uso permette di effettuare la ricerca di un prodotto nel sistema|
|<p>Attori primari: Amministratore, ClienteP, User</p><p></p>|
|Attori secondari: sistema|
|Precondizioni: l’attore primario desidera effettuare la ricerca di un prodotto|
|<p>Sequenza eventi principali:</p><p>1.  il caso d’uso inizia quando l’attore primario desidera effettuare la ricerca di un prodotto nel database del sistema</p><p>2. il sistema richiede all’attore primario di inserire i dati di ricerca</p><p>3. l’attore primario specifica i dati di ricerca</p><p>4. il sistema effettua la ricerca con i dati forniti dall’attore primario</p><p>5. **if** il prodotto è stato trovato</p><p>5.1 il sistema restituisce i dati del prodotto</p><p>6. **else**</p><p>6.1 il sistema restituisce un errore</p>|
|<p>Postcondizioni: nessuna</p><p></p>|
|<p>Sequenza degli eventi alternativa: nessuna</p><p></p>|



























|Caso d’uso: SpostaProdotto|
| :- |
|ID: 7|
|<p>Descrizione: Questo caso d’uso permette di effettuare lo spostamento di un prodotto nel sistema</p><p></p>|
|<p>Attori primari: Amministratore</p><p></p>|
|<p>Attori secondari: nessuno</p><p></p>|
|Precondizioni: è necessario lo spostamento di un prodotto|
|<p>Sequenza eventi principali:</p><p>1. Il caso d’uso inizia quando l’attore primario richiede di spostare un prodotto</p><p>2. Il sistema richiede all’attore primario un luogo di A e un luogo B</p><p>3. l’attore primario inserisce i dati richiesti</p><p>4. Il sistema richiede il prodotto o un suo riferimento da spostare dal luogo</p><p>A ad un luogo B</p><p>5. l’attore primario inserisce i dati richiesti</p><p>6. Il sistema sposta il prodotto dal luogo A ad un luogo B</p><p>7. **if** l’operazione è stata effettuata</p><p>7.1. il sistema comunica il successo dell’operazione</p><p>8. **else**</p><p>8.1 Il sistema restituisce un errore</p>|
|<p>Postcondizioni: Nessuna</p><p></p>|
|Sequenza degli eventi alternativa: Nessuna|











|Caso d’uso: VendiProdotto|
| :- |
|ID: 8|
|<p>Descrizione: Questo caso d’uso permette di effettuare la vendita di un prodotto</p><p></p>|
|<p>Attori primari: Amministratore</p><p></p>|
|<p>Attori secondari: Nessuno</p><p></p>|
|Precondizioni: l’amministratore desidera effettuare la vendita di un prodotto|
|<p>Sequenza eventi principali:</p><p>1. il caso d’uso inizia quando** l’Amministratore vuole vendere un prodotto</p><p>2. l’amministratore inserisce l’oggetto da vendere </p><p>3. **include** (:RicercaProdotto)</p><p>4. **include** (:CRicevuta)</p><p>5. **include** (:DProdotto)</p><p>6. **include** (:Notifica)</p>|
|Postcondizioni: il prodotto è stato venduto|
|Sequenza degli eventi alternativa: Nessuna|






































|Caso d’uso: VisualizzaStatistiche|
| :- |
|ID: 9|
|Descrizione: Questo caso d’uso permette di effettuare la visualizzazione delle statistiche disponibili|
|Attori primari: Amministratore|
|Attori secondari: Nessuno|
|Precondizioni: l’amministratore desidera visualizzare le statistiche|
|<p>Sequenza eventi principali: x</p><p>1. Il caso d’uso inizia quando l’attore primario seleziona “visualizzare le statistiche”</p><p>2. Il sistema preleva dal database le statistiche</p><p>3. **if** statistiche disponibili</p><p>4. Il sistema mostra le statistiche</p>|
|Postcondizioni: Nessuna|
|Sequenza degli eventi alternativa: Nessuna|



**2.2.3 GESTIONE CLIENTE-PROPRIETARIO**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.006.png)

Figura NUMERO: Diagramma Gestione Cliente-Proprietario





|Caso d’uso: ControllaStatoProdotti|
| :- |
|ID: 10|
|Descrizione: Questo caso d’uso permette di effettuare in controllo dello stato dei prodotti di un ClienteP|
|Attori primari: ClienteP|
|<p>Attori secondari: Nessuno</p><p></p>|
|Precondizioni: L’attore primario deve aver effettuato il login|
|<p>Sequenza eventi principali: </p><p>1. Il caso d’uso inizia quando l’attore primario desidera visualizzare lo</p><p>stato dei prodotti</p><p>2. Il sistema ricerca i prodotti associati all’attore primario</p><p>3. **if** esistono oggetti associati</p><p>3.1. il sistema preleva dal database gli oggetti associati all’attore</p><p>Primario</p><p>3.2 Il sistema mostra all’attore primario lo stato dei prodotti associati</p><p>4. **else** il sistema restituisce un errore</p>|
|Postcondizioni: Nessuna|




|Caso d’uso: DatiPersonali|
| :- |
|ID: 11|
|Descrizione: Questo caso d’uso permette di effettuare in controllo dei propri dati|
|Attori primari: ClienteP|
|<p>Attori secondari: Nessuno</p><p></p>|
|Precondizioni: L’attore primario deve aver effettuato il login|
|<p>Sequenza eventi principali: </p><p>1.Il caso d’uso inizia quando l’attore primario desidera visualizzare i propri dati</p><p>2. Il sistema ricerca l’account associato all’attore primario</p><p>3. **if** trovato account associato</p><p>3.1. il sistema preleva dal database i dati associati all’attore</p><p>primario</p><p>3.2 Il sistema mostra all’attore primario i propri dati</p><p>4. **else** il sistema restituisce un errore</p>|
|Postcondizioni: Nessuna|





**2.2.4 GESTIONE SISTEMA**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.007.png)

Figura NUMERO: Diagramma Gestione Sistema


|Caso d’uso: Backup|
| :- |
|ID: 12|
|<p>Descrizione: il sistema effettua il backup dei dati</p><p></p>|
|<p>Attori primari: Tempo</p><p></p>|
|<p>Attori secondari: Nessuno</p><p></p>|
|<p>Precondizioni: Nessuno il programma è stato chiuso</p><p></p>|
|<p>Sequenza eventi principali:</p><p>1. Il caso d’uso inizia quando il programma è stato chiuso</p><p>2. Il sistema preleva i dati dal database</p><p>3. Il sistema copia su disco i dati prelevati</p>|
|<p>Postcondizioni: I dati sono stati copiati.</p><p></p>|
|<p>Sequenza degli eventi alternativa: Nessuna</p><p></p>|






|Caso d’uso: GeneraStatistiche|
| :- |
|ID: 13|
|<p>Descrizione: Il sistema genera statistiche</p><p></p>|
|<p>Attori primari: Tempo</p><p></p>|
|<p>Attori secondari: Nessuno</p><p></p>|
|Precondizioni: Nessuna|
|<p>Sequenza eventi principali:</p><p>1. Il caso d’uso inizia quando il sistema viene chiuso</p><p>2. Il sistema preleva dati riguardanti i prodotti</p><p>3. Il sistema preleva dati riguardanti le ricevute</p><p>4. Il sistema preleva dati riguardanti i Clienti Proprietari</p><p>5. Il sistema genera statistiche</p><p>6. Il sistema salva i dati su disco</p>|
|<p>Postcondizioni: Le statistiche generate sono salvate su disco</p><p></p>|
|<p>Sequenza degli eventi alternativa: Nessuna</p><p></p>|
















|Caso d’uso: ScontaProdotto|
| :- |
|ID: 14|
|<p>Descrizione: Il sistema sconta il prodotto</p><p></p>|
|<p>Attori primari: Tempo</p><p></p>|
|<p>Attori secondari: Nessuno</p><p></p>|
|<p>Precondizioni Segmento 1: Sono passati 60 giorni dalla registrazione del prodotto</p><p>Precondizioni Segmento 2: Sono passati 90 giorni dalla registrazione del prodotto</p><p>Precondizioni Segmento 3: Sono passati 120 giorni dalla registrazione del prodotto</p><p></p>|
|<p>Sequenza eventi Segmento 1:</p><p>1.Il caso d’uso inizia quando sono passati 60 giorni dalla registrazione del prodotto.</p><p>2.Il prodotto viene scontato del 30% rispetto al prezzo iniziale</p><p>Sequenza eventi Segmento 2:</p><p>1.Il caso d’uso inizia quando sono passati 90 giorni dalla registrazione del prodotto.</p><p>2.Il prodotto viene scontato del 40% rispetto al prezzo iniziale</p><p>Sequenza eventi Segmento 3:</p><p>1.Il caso d’uso inizia quando sono passati 120 giorni dalla registrazione del prodotto</p><p>2.Il prodotto viene scontato del 50% rispetto al prezzo iniziale</p><p></p>|
|<p>Postcondizioni: Il prodotto viene scontato</p><p></p>|
|<p>Sequenza degli eventi alternativa: Nessuna</p><p></p>|



**2.2.5 GESTIONE USER**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.008.png)

Figura NUMERO: Diagramma Gestione User

|Caso d’uso: FiltraggioVario|
| :- |
|ID: 15|
|Descrizione: Filtraggio dei prodotti in varie modalità|
|Attori primari: User|
|Attori secondari: Nessuno|
|Precondizioni: l’utente vuole effettuare il filtraggio dei prodotti|
|<p>Sequenza eventi principali:</p><p>1. il caso d’uso inizia quando l’utente vuole filtrare i prodotti disponibili</p><p>2. l’utente inserisce la modalità di filtraggio e preme invio</p><p>3. il sistema effettua il filtraggio con il filtro applicato</p><p>4. **if** ci sono oggetti nella categoria cercata</p><p>4.1. mostra all’utente la lista degli oggetti trovati</p><p>5. **else** mostra all’utente un messaggio indicando che non sono stati trovati</p><p>oggetti nella categoria</p><p></p>|
|Postcondizioni: Nessuna|
|Sequenza degli eventi alternativa: nessuna|














|Caso d’uso: Login|
| :- |
|ID: 16|
|<p>Descrizione: L’User accede al sistema</p><p></p>|
|Attori primari: User|
|Attori secondari: Nessuno|
|<p>Precondizioni: Nessuna</p><p></p>|
|<p>Sequenza eventi principali:</p><p>1. Il caso d’uso inizia quando l’User vuole accedere al sistema</p><p>2. L’User inserisce il nome utente e la password</p><p>3. Il Sistema controlla i dati inseriti</p><p>4. Login</p><p></p>|
|<p>Postcondizioni: L’user è loggato</p><p></p>|
|<p>Sequenza degli eventi alternativa:</p><p>La sequenza degli eventi alternativa inizia dal punto 3</p><p>4.Il nome utente e la password non esistono o sono errati</p><p>5.Il sistema restituisce un messaggio di errore</p><p></p>|

**3 DIAGRAMMI DI ANALISI**

**3.1 p DI ANALISI**


![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.009.png)

Figura NUMERO: Diagramma del package di analisi

**3.2 DIAGRAMMI DELLE CLASSI DI ANALISI**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.010.png)

Figura NUMERO: Diagramma di analisi delle classi di Attività





![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.011.png)

Figura NUMERO: Diagramma di analisi delle classi di Servizio

**3.3 DIAGRAMMI DI SEQUENZA**

**3.3.1 BACKUP**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.012.png)

Figura NUMERO: Diagramma di sequenza: Backup

**3.3.2 CONTROLLASTATOPRODOTTO**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.013.png)

Figura NUMERO: Diagramma di sequenza: ControllaStatoProdotto

**3.3.3 CRUD PRODOTTO**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.014.png)

Figura NUMERO: Diagramma di sequenza: Aggiorna Prodotto

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.015.png)

Figura NUMERO: Diagramma di sequenza: Crea Prodotto

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.016.png)

Figura NUMERO: Diagramma di sequenza: Cancella Prodotto

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.017.png)

Figura NUMERO: Diagramma di sequenza: Visualizza Prodotto

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.018.png)

Figura NUMERO: Diagramma di sequenza: Visualizza Prodotto

**3.3.4 LOGIN**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.019.png)

Figura NUMERO: Diagramma di sequenza: Login

**3.3.5 NOTIFICA**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.020.png)

Figura NUMERO: Diagramma di sequenza: Notifica

**3.3.6 RICERCACLIENTE**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.021.png)

Figura NUMERO: Diagramma di sequenza: Ricerca Cliente

**3.3.7 RICERCAPRODOTTO**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.022.png)

Figura NUMERO: Diagramma di sequenza: RicercaProdotto

**3.3.8 VENDIPRODOTTO**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.023.png)

Figura NUMERO: Diagramma di sequenza: VendiProdotto

**3.3.9 VISUALIZZASTATISTICHE**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.024.png)

Figura NUMERO: Diagramma di sequenza: Visualizza Statistiche


**4 DIAGRAMMI DI PROGETTAZIONE**

**4.1 DIAGRAMMI DELLE CLASSI DI PROGETTAZIONE**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.025.png)

Figura NUMERO: Diagramma del package di Progettazione 

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.026.png)

Figura NUMERO: Diagramma di progettazione delle classi di Attività 

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.027.png)

Figura NUMERO: Diagramma di progettazione delle classi di Servizio

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.028.png)

Figura NUMERO: Diagramma di progettazione delle classi di SistemService

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.029.png)

Figura NUMERO: Diagramma di progettazione delle classi di View

**4.2 DIAGRAMMI DEI COMPONENTI**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.030.png)

Figura NUMERO: Diagramma dei componenti: Model

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.031.png)

Figura NUMERO: Diagramma dei componenti: MVC

**4.3 DIAGRAMMI DELLE MACCHINE A STATI**

**4.3.1 MACCHINE A STATI: BACKUP**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.032.png)

Figura NUMERO: Diagramma della macchina a stati: Backup

**4.3.2 MACCHINE A STATI: CATEGORIA**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.033.png)

Figura NUMERO: Diagramma della macchina a stati: Categoria

**4.3.3 MACCHINE A STATI: LOGIN**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.034.png)

Figura NUMERO: Diagramma della macchina a stati: Login

**4.3.4 MACCHINE A STATI: PRODOTTO**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.035.png)

Figura NUMERO: Diagramma della macchina a stati: Prodotto

**4.3.5 MACCHINE A STATI: RICEVUTA**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.036.png)

Figura NUMERO: Diagramma della macchina a stati: Ricevuta


**5 IMPLEMENTAZIONE**

**5.1 DIAGRAMMA DI DEPLOYMENT**

![](https://github.com/LeonUrsu/NegozioDellUsato-ExamIS/blob/master/README/Aspose.Words.ba09b7bf-aba0-4201-b306-d0a103687ce7.037.png)

Figura NUMERO: Diagramma di deployment 

**6 MOCKUP**

I segueti Mockup sono stati realizzati con il software: **Qt designer**

Il fine è stato rendere dinamica la progettazione delle interfacce grafiche e quindi evitare una struttura monolitica. Per questo motivo è stato utilizzato per la progettazione dei Mockup il suddetto software. Vi è la possibilità di compilare la progettazione grafica nel designer in un “NomeFile.ui” e di utilizzarlo come componente nella gestione delle interfacce grafiche. Il fatto di aver reso l’interfaccia grafica un componente permette di effettuare manutenzioni future in maniera estremamente efficiente.

La seguente versione dei Mockup è aggiornata alla versione di UsatoBeato citata in tale documento.

**7 PYUNIT**





