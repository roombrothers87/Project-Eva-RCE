import json, math, statistics as stats

def entropy(p):
    eps=1e-12
    return -sum(max(pi,eps)*math.log(max(pi,eps)) for pi in p)

def kl(p,q):
    eps=1e-12
    return sum(max(pi,eps)*math.log(max(pi,eps)/max(qi,eps)) for pi,qi in zip(p,q))

# charge JSONL et calcule des proxys H et KL entre premières et secondes distributions top-k
runs=[]
with open('../data/samples/runs.jsonl','r',encoding='utf-8') as f:
    for line in f:
        runs.append(json.loads(line))

by_cond={}
for r in runs:
    by_cond.setdefault(r['condition'], []).append(r)

summary={}
for cond, items in by_cond.items():
    entropies=[]
    for it in items:
        # proxy: entropie moyenne sur les deux vecteurs top-k
        e = 0.5*entropy(it['probs_topk'][0]) + 0.5*entropy(it['probs_topk'][1])
        entropies.append(e)
    summary[cond] = {
        "n": len(items),
        "H_mean": sum(entropies)/len(entropies),
        "H_std": stats.pstdev(entropies) if len(entropies)>1 else 0.0
    }

# KL entre paires C1<->C2 et C1<->C3 (proxy)
def mean_pairwise_kl(A,B):
    vals=[]
    for a,b in zip(A,B):
        p=a['probs_topk'][0]; q=b['probs_topk'][0]
        vals.append(0.5*(kl(p,q)+kl(q,p)))
    return sum(vals)/len(vals)

if all(c in by_cond for c in ["C1_reentry","C2_paraphrase","C3_noise"]):
    summary["KL_C1_C2"] = mean_pairwise_kl(by_cond["C1_reentry"], by_cond["C2_paraphrase"])
    summary["KL_C1_C3"] = mean_pairwise_kl(by_cond["C1_reentry"], by_cond["C3_noise"])

print(json.dumps(summary, indent=2))
