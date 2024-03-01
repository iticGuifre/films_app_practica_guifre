# 1. Què fan els mètodes get_configuracio i get_persistencies?
### get_configuracio s'encarrega de llegir el fitxer que tenim de configuració, get_persistencies s'encarrega de retornar la classe pertinent en funcio del parametre de configuracio de motor gràfic, és a dir et retorna una classe segons la base de dades que utilitzem.


# 2. Què fa lambda? Com es podria reescriure el codi sense utilitzar lambda? Quina utilitat hi trobeu a utilitzar lambda?
### Lambda és una funció anònima que permet emprar-la sense haver de declarar-la. 
### Es podrai escriure així: 
### def process_show_list(context):
###      mostra_llista(context['llistapelis'])
### 
###  def process_show_next(context):
###     mostra_llista(context['llistapelis'])
###
### És útil si necessites una funció que només es cridadrà un cop.

# 3. Penseu que s’ha desacoblat suficientment la lògica de negoci de la lògica d’aplicació? Raoneu la resposta i digueu si hi ha cap millora que es pugui fer. 
### Penso que la llògica que hem aplicat és robusta i permet la reutilització en gran part del codi. Si es necessités, es podria afegir més motors de base de dades i no hi hauria gran complicació al fer-ho.
