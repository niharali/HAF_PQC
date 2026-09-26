
from pathlib import Path
import matplotlib.pyplot as plt
import csv

def generate_figures(csv_file, outdir):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    names=[]
    with open(csv_file) as f:
        r=csv.DictReader(f)
        data=list(r)

    alg=[x['algorithm'] for x in data]
    val=[float(x['latency_ms']) for x in data]

    plt.figure(figsize=(8,5))
    plt.bar(alg,val)
    plt.xticks(rotation=45)
    plt.ylabel('Latency (ms)')
    plt.title('Primitive Latency Comparison')
    p=Path(outdir)/'Fig1_Primitive_Latency.png'
    plt.tight_layout()
    plt.savefig(p,dpi=300)
    plt.close()
    names.append(str(p))
    return names
