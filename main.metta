!(register-module! ../MeTTaProject) ;initialize the imports
!(import! &self main)
!(import! &self MeTTaProject:gene)

(= (h) (match &self 
       (gene_type (gene $gen) $type) 
       (match &self (chr (gene $gen) $chr) 
       (match &self (start (gene $gen) $start) 
       (match &self (end (gene $gen) $end)
       (match &self (gene_name (gene $gen) $name) 
       (match &self (synonyms (gene $gen) $synonyms) 
       ((summarize $gen (gene $gen $type $chr $start $end $name $synonyms))))))))
)) ; matching function defined recursively for multiple variable matched

!(h) ; function called