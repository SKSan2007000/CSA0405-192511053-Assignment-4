# CSA0405 – Assignment 4 (CO4)
**Student:** B. Santhosh Kumar  
**Register Number:** 192511053  
**Department:** CSE  
**Course:** Operating Systems  
**Environment:** Debian GNU/Linux 13 (trixie), x86_64; Linux 6.18.57; GCC 14.2.0; Python 3.13.5.

## Repository structure
- `Task01/` – file-system design review, proposed directory hierarchy and defence.
- `Task02/` – completed C allocation program, allocation calculations and boundary tests.
- `Task03/` – modern filesystem comparison and Linux command evidence.
- `Task04/` – completed SSTF C program, six-algorithm deterministic simulation, fairness discussion and scheduler inspection.
- `Task05/` – distributed/cloud storage comparison, replication and device-management calculations.
- `Task06/` – video-streaming architecture and two-alternative latency simulation.
- `docs/` – final report.

Each task contains `input/`, `src/` where applicable, `output/`, `evidence/` and task notes. The evidence PNGs are rendered from the recorded execution outputs; the text output files are retained for verification.

## Run instructions
Run each command from the repository root:

```sh
cd Task02 && sh run.sh && sh run_calculations.sh && sh run_tests.sh
cd ../Task03 && sh filesystem_commands.sh
cd ../Task04 && sh run.sh && sh run_simulation.sh && sh run_tests.sh && sh check_scheduler.sh
cd ../Task05 && sh run.sh
cd ../Task06 && sh run.sh
```

Compile the supplied C programs using:
```sh
gcc -std=c11 -Wall -Wextra src/allocation.c -o output/allocation
gcc -std=c11 -Wall -Wextra src/sstf.c -o output/sstf
```

## Notes and limitations
- Task 3 command evidence was captured in a container backed by `overlayfs`. `tune2fs` and `dumpe2fs` are not installed and no ext4 block device is exposed, so no ext4 superblock output is claimed. Run the requested ext4 command on the actual Linux ext4 partition before final submission if faculty requires it.
- Task 4's exposed virtual block devices report the `none` scheduler. This is container evidence, not a physical SSD benchmark.
- Task 4 and Task 6 simulations are deterministic models. Task 6 latency values are based on stated assumptions and must not be presented as provider or hardware measurements.
- Create the required GitHub repository `CSA0405-192511053-Assignment4`, add faculty access, commit each task progressively, and paste the working URL into the report cover page. No GitHub repository is created by this package.
