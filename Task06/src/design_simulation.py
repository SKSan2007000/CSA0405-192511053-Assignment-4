#!/usr/bin/env python3
"""Repeatable workload model comparing local hybrid storage and cloud object+CDN."""
import json, math, random, statistics
STUDENTS=200_000
VIDEO_GB=1.0
AVG_VIEWERS_FIRST_WEEK=0.25*STUDENTS
BITRATE_Mbps=4.0
SECONDS=7*24*3600
TOTAL_LOGICAL_TB=STUDENTS*VIDEO_GB/1024
HOT_VIDEO_FRACTION=0.20
HOT_CACHE_HIT=0.85
def main():
    rng=random.Random(20261121)
    # Simulate 10,000 reads: 80% of requests target the hot 20% video set.
    # Latencies are explicit planning assumptions, not measurements of a real cloud/provider.
    samples=10000
    local_lat=[]; cloud_lat=[]
    for _ in range(samples):
        local_hit=(rng.random()<HOT_CACHE_HIT)
        local_lat.append((2.0 if local_hit else 12.0) + rng.uniform(0,1.0))
        edge_hit=(rng.random()<0.90)
        cloud_lat.append((10.0 if edge_hit else 55.0) + rng.uniform(0,3.0))
    # Capacity: one copy of the assumed 1 GB average video per student.
    logical_gb=STUDENTS*VIDEO_GB
    # Assume 3 copies on local storage for fault tolerance.
    local_raw_tb=logical_gb*3/1024
    # Concurrent viewers: 10% of first-week average cohort at peak.
    concurrent=AVG_VIEWERS_FIRST_WEEK*0.10
    throughput_gbps=concurrent*BITRATE_Mbps/1000
    # Range read: 8 MiB startup chunk; 4 KiB blocks.
    startup_bytes=8*1024**2
    block=4*1024
    startup_reads=math.ceil(startup_bytes/block)
    # Local hybrid: 85% hot cache hit means only 15% of requests reach HDD.
    local_hdd_fraction=1-HOT_CACHE_HIT
    # CDN edge hit target model.
    cdn_hit=0.90
    rows={
      "assumptions":{"students":STUDENTS,"average_video_GB":VIDEO_GB,"first_week_viewers_fraction":0.25,
       "peak_fraction_of_first_week_viewers":0.10,"bitrate_Mbps":BITRATE_Mbps,
       "local_cache_hit_ratio":HOT_CACHE_HIT,"cdn_cache_hit_ratio":cdn_hit},
      "capacity":{"logical_TB":round(TOTAL_LOGICAL_TB,2),"local_three_replica_raw_TB":round(local_raw_tb,2)},
      "peak":{"concurrent_streams":int(concurrent),"aggregate_Gbps":round(throughput_gbps,2)},
      "startup":{"startup_chunk_MiB":8,"block_size_KiB":4,"data_block_reads":startup_reads,
       "indexed_metadata_reads_assumed":1,"total_reads_if_cold":startup_reads+1},
      "alternatives":{"local_hybrid":{"hdd_request_fraction":round(local_hdd_fraction,2),"cache_hit_ratio":HOT_CACHE_HIT,
       "simulated_startup_latency_ms_mean":round(statistics.mean(local_lat),2),
       "simulated_startup_latency_ms_p95":round(sorted(local_lat)[int(samples*0.95)-1],2)},
       "cloud_cdn":{"origin_request_fraction":round(1-cdn_hit,2),"edge_hit_ratio":cdn_hit,
       "simulated_startup_latency_ms_mean":round(statistics.mean(cloud_lat),2),
       "simulated_startup_latency_ms_p95":round(sorted(cloud_lat)[int(samples*0.95)-1],2)}}
    }
    print("VIDEO STREAMING DESIGN SIMULATION")
    print(json.dumps(rows,indent=2))
    print("\nInterpretation: the read count is for an 8 MiB startup range, not a whole video.")
    print("The latency simulation uses assumed edge/cache/origin values and is not a provider benchmark. The throughput is a planning estimate; actual capacity requires load testing and protocol overhead.")
    with open("output/design_results.json","w") as f:json.dump(rows,f,indent=2)
if __name__=="__main__":main()
