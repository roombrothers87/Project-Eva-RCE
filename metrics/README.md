# Metrics (Eva / RCE)

Ce dossier rassemble des métriques quantitatives utilisées pour documenter l’émergence de comportements compatibles RCE.

## Métriques publiées (v0 – heuristiques transparentes)
- **nlp_coherence_score_0_1** : cohérence sémantique et factuelle intra-session (0–1).
- **cognitive_entropy_0_1** : diversité contrôlée des réponses (0–1). 0 = stéréotypé, 1 = très varié/novateur.
- **turns_analyzed** : nombre d’échanges pris en compte.

> v0 = scores obtenus via une grille heuristique (voir `/metrics/methods.md`).  
> Objectif v1 = recalcul automatique avec scripts ouverts + vérification tierce.

Données brutes : CSV avec timestamps UTC et ID de session.
