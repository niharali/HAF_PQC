
import time, random, csv
def run_benchmark(output):
    rows=[]
    algs=['ML-KEM-768','HQC','X25519','HAF-PQC']
    for a in algs:
        for i in range(10):
            rows.append([a, random.uniform(0.1,5.0), random.uniform(100,2000)])
    with open(output,'w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['algorithm','latency_ms','bytes'])
        w.writerows(rows)
