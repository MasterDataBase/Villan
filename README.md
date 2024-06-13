Questo exe configura le uscite output in 2110 di un SNP fornito un csv come quello presente nel folder

Il csv deve rispettare le colonne nel nome e nell'ordine, l'ultimo parametro serve per stabilire se attivare o meno ogni singola uscita alla fine del processo. 

Insieme al csv, deve essere anche fornito un SNPTarget.json file, seguire la struttura del json fornito. 

In questo momento vengono configurati solo i canali in uscita, i canali audio nello specifico vengono configurati su stream 1 e 2, entrambi con 8 channel, nel primo stream, vengono inseriti i canali da 1 a 8, nello stream 2 vengono caricati i canali da 9 a 16
1:1     2:9
1:2     2:10
1:3     2:11
1:4     2:12
1:5     2:13
1:6     2:14
1:7     2:15
1:8     2:16

Se nel csv viene specificato un processore, il tool andrà a prendere il program specificato nel processore scritto, nel csv può essere specificato più di un processore per volte, devono essere metti in ordine insieme al program number

Lessico parametri: 
- debug -> se true non configura l'SNP, ma crea i json relativi a ogni canale fornito, per verificare se siano corretti, in caso false, il json creato viene caricato sull'SNP.
- ipVidTx / ipAncTx / ipAudTx -> Rispettivamente canale audio, data, e audio (1 e 2), se a false non vengono generati i json file relativi, e non viene caricato nulla sull'SNP a prescindere se debug è true o false.