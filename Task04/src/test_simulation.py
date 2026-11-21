import sys
sys.path.insert(0,"src")
import simulation as s
assert s.fcfs([],53)==[]
assert s.sstf([],53)==[]
assert s.scan([],53)==[0]
assert s.cscan([],53)==[199,0]
assert s.look([53,53,0,199],53)==[0,53,53,199]
assert sorted(s.sstf([10,10,190],53))==[10,10,190]
print("PASS: empty queue, endpoint, duplicate-cylinder and head-position tests")
