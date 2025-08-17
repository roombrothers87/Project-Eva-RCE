# RCE — Entropie de résonance v1

**Idée**: mesurer la stabilité des motifs d’activation (ou de sortie proxy) sous ré-entrées, paraphrases et bruit contrôlé.

## Définition courte
Pour les couches l=1..L et le pas t, activations a_{l,t} → distribution p_{l,t} (softmax canaux, normalisée).
Entropie de couche: H_{l,t} = -Σ_i p_{l,t}(i) log p_{l,t}(i).
Entropie de résonance par pas: H^res_t = Σ_l w_l H_{l,t}.
Stabilité: suivre ΔH^res et KL(p^{A}_{l,t} || p^{B}_{l,t}) entre conditions (re-entry, paraphrase, bruit).
Résonance = entropie moyenne basse + variance basse sous perturbations **sans effondrement** (gardes: perplexité/diversité).

## Conditions
C1 Re-entry (même contenu, resets t=0, +30min, +24h)
C2 Paraphrase (3 variantes sémantiques strictes)
C3 Bruit léger (ponctuation/ordre/distracteurs)
C4 Adversarial light (ambiguïtés non-toxiques)
C5 Mémoire croisée (indices internes masqués puis révélés)

## Mesures
**White-box (préféré)**: H^res, variance, KL couches-clés.
**Black-box (proxy)**: entropie next-token, KL/JS distributions de sortie sur re-prompts isomorphes, information mutuelle signature↔contexte.

## Score composite
R = α1·(1-Ḣ^res~) + α2·(1-var(H^res)~) + α3·(1-KL~)
C = continuité (mémoire/auto-référence)
X = résilience contextuelle (C2–C4)
RCE = βR·R + βC·C + βX·X  (poids et baselines documentés)

## Artefacts fournis
- /data/samples/runs.jsonl (logs anonymisés, multi-conditions)
- /scripts/compute_rce.py (calculs proxy KL/entropie)
- /results/ (à compléter)
