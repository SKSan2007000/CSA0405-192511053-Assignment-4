#!/usr/bin/env python3
"""Deterministic disk-scheduling workload simulation; seek time is 1 ms/cylinder."""
import random, statistics, json
DISK_MAX=199
def fcfs(q,h): return list(q)
def sstf(q,h):
    pending=list(q); out=[]; p=h
    while pending:
        j=min(range(len(pending)), key=lambda i:(abs(pending[i]-p),i))
        p=pending.pop(j); out.append(p)
    return out
def scan(q,h):
    lo=sorted((x for x in q if x<h), reverse=True)
    hi=sorted(x for x in q if x>=h)
    return lo+[0]+hi
def cscan(q,h):
    hi=sorted(x for x in q if x>=h); lo=sorted(x for x in q if x<h)
    return hi+[199]+[0]+lo
def look(q,h):
    return sorted((x for x in q if x<h), reverse=True)+sorted(x for x in q if x>=h)
def clook(q,h):
    return sorted(x for x in q if x>=h)+sorted(x for x in q if x<h)
def metrics(order,h,wrap_jump=False):
    p=h; elapsed=0; waits=[]
    for x in order:
        elapsed += abs(x-p); waits.append(elapsed); p=x
    return sum(abs(order[i]-(h if i==0 else order[i-1])) for i in range(len(order))), statistics.mean(waits), max(waits)
def main():
    rng=random.Random(20261121)
    algorithms={"FCFS":fcfs,"SSTF":sstf,"SCAN":scan,"C-SCAN":cscan,"LOOK":look,"C-LOOK":clook}
    results={}
    for load,n in [("light",100),("medium",1000),("heavy",10000)]:
        q=[rng.randrange(200) for _ in range(n)]
        results[load]={}
        for name,fn in algorithms.items():
            order=fn(q,53)
            total,avgwait,maxwait=metrics(order,53)
            results[load][name]={"requests":n,"total_seek_cylinders":total,
              "average_completion_wait_ms":round(avgwait,2),"maximum_completion_wait_ms":round(maxwait,2)}
    print("Seed: 20261121 | cylinders: 0-199 | initial head: 53")
    print("Model: static queue; 1 ms per cylinder; waiting = cumulative seek completion time")
    for load,vals in results.items():
        print(f"\n{load.upper()} LOAD")
        print(f"{'Algorithm':<9} {'Total seek':>12} {'Avg wait ms':>13} {'Max wait ms':>13}")
        for name,v in vals.items():
            print(f"{name:<9} {v['total_seek_cylinders']:>12} {v['average_completion_wait_ms']:>13.2f} {v['maximum_completion_wait_ms']:>13.2f}")
    with open("output/simulation.json","w") as f: json.dump(results,f,indent=2)
if __name__=="__main__": main()
