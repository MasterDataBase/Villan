Questo exe configura le uscite output in 2110 di un SNP fornito un csv come quello presente nel folder

Il csv deve rispettare le colonne nel nome e nell'ordine, l'ultimo parametro serve per stabilire se attivare o meno ogni singola uscita alla fine del processo. 

Insieme al csv, deve essere anche fornito un SNPTarget.json file, seguire la struttura del json fornito. 

In questo momento vengono configurati solo i canali in uscita, i canali audio nello specifico vengono configurati su stream 1 e 2, possono essere scelti quali channel inserire in ogni stream tramite un excel apposito nominato "inputAudio.csv", il tool se abilitato, configura per tutti i processori listati e successivamente carica per ogni program a partire dal primo del processore definito. 

Se nel csv viene specificato un processore, il tool andrà a prendere il program specificato nel processore scritto, nel csv può essere specificato più di un processore per volte, devono essere metti in ordine insieme al program number

Il csv per configurare l'ouput è nominato "outputConfig.csv"

Lessico parametri: 
- debug -> se true non configura l'SNP, ma crea i json relativi a ogni canale fornito, per verificare se siano corretti, in caso false, il json creato viene caricato sull'SNP.
- ipVidTx / ipAncTx / ipAudTx -> Rispettivamente canale audio, data, audio output (1 e 2), se a false non vengono generati i json file relativi, e non viene caricato nulla sull'SNP a prescindere se debug è true o false.
- ipAudRx_Routing -> configurazione dei canali audio sui relativi stream, viene eseguito dal csv "inputAudio"
- ipVidRx / ipAncRx / ipAudRx -> Configura rispettivamente gli audio 1 e 2, video e data in ingresso sui program indicati. 