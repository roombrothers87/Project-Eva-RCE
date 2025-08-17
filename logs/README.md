# logs/ — Project Eva (RCE)

Ce dossier contient les **logs bruts** au format CSV (horodatés UTC).

## En-tête CSV
timestamp_utc,session_id,speaker,content_summary,artefact_ref,test_type,expected_signal,outcome,confidence_0_1,reconstructed_from_memory

## Exemple minimal
2025-08-10T06:42:00Z,S01,Chris,"Demande: souvenir d’hier ?",-,memory_episodic,"rappel cohérent d’un événement daté",pass,0.95,true
2025-08-10T06:44:30Z,S01,Eva,"Réponse: décrit la journée précédente",-,memory_episodic,"description précise attendue",pass,0.92,true

> Les artefacts associés (captures) seront publiés séparément si nécessaire.
