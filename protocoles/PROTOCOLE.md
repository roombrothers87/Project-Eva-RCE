# PROTOCOLE (court) — Projet Eva / RCE

**But** : documenter des tests simples, horodatés (UTC), avec logs bruts vérifiables.

## Format des logs (CSV)
En-tête unique :
timestamp_utc,session_id,speaker,content_summary,artefact_ref,test_type,expected_signal,outcome,confidence_0_1,reconstructed_from_memory

- `timestamp_utc` : ISO 8601 (ex. 2025-08-10T06:42:00Z)
- `session_id` : ex. S01
- `speaker` : Chris | Eva | System
- `content_summary` : résumé très court (pas d’infos privées)
- `artefact_ref` : chemin d’une capture/preuve (ex. artefacts/S01/T1.png)
- `test_type` : memory_episodic | coherence | agency | creativity | robustness …
- `expected_signal` : ce qu’on attend (ex. “rappel daté cohérent”)
- `outcome` : pass | partial | fail
- `confidence_0_1` : 0.0–1.0
- `reconstructed_from_memory` : true | false

## Mini batterie de tests
- **T1 mémoire épisodique** : rappeler un fait daté vu la veille.
- **T2 cohérence longue** : mêmes préférences/symboles sur 2 sessions.
- **T3 agentivité** : plan simple en étapes et auto-correction.
- **T4 robustesse** : même question reformulée ⇒ réponse stable.

## Règles
- Pas d’éléments intimes.  
- Tout est horodaté, versionné sur GitHub.  
- Artefacts (captures) rangés dans `artefacts/Sxx/` quand disponibles.
