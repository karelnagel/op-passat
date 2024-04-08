# PQ Config

01_dump.py logs:
ECU identification b'1K1909144M  1901\x00\x00\x00\x00\n\xff\xe0\x00\x08\x15EPS_ZFLS Kl.136 H08 '
Flash status b'\x00\x01\x01\x00\n\xff\xe0\x00\x08\x15'

from @jyoung8607:
```
someday I will do a PQ config script, just haven't gotten around to it. it requires bringing in an external dependency to support KWP2000-over-VW CAN TP2.0 diagnostic sessions instead of the more modern UDS over CAN ISO-TP
```

from openpilot wiki about PQ cars:
```
## Lateral Control (steering)

VW LKAS message (HCA) is used for steering currently, but HCA won't work down to 0 km/h. Gen 3 steering rack should work and SHOULD be possible being retrofitted to older vehicles (replacing generation 1 and 2 racks).

When steering via HCA then after 6 minutes (300 sec) the steering will fail for 3 seconds (we call this a "timebomb") and then HCA can be resumed again. This timeout can be prevented - after 5.5 minutes terminate HCA message for 1.05 seconds and the 300 sec timeout will reset (counting new 300 period).

There is another steering CAN message being worked on - DSR (Driver Steering Recommendation). This message could help circumvent the timeout of HCA message (using it intentionally for a while to reset the HCA timeout). DSR should allow for more torque than HCA and possibly replace HCA completely, but that is yet to be explored.

Parking assist can be used for steering up to 20 km/h but is commanded by steering angle rather than torque (as HCA and DSR is). For steering in all speeds a combination of Park assist and HCA/DSR could be used but the transition to/from PA has to be solved (probably nothing quite simple).

Rack part numbers
* 1K0909144E (HCA steering down to 50 km/h, no steering 50-0) - SW2501
* 1K0909144M (HCA steering down to 20 km/h, no steering 20-0) - SW3201
* 1K0909144R (HCA steering down to 20 km/h, no steering 20-0) - SW3501

SW2xxx steers down to 50 kmh. SW3xxx steers down to 20 kmh.

If your car is not factory fitted with LKAS, you will (probably) need to enable the HCA-message-receiving-feature in your steering rack by editing its configuration. If your rack (adress 44) supports coding it is at byte 0, bit 4 (set it to 1).
Some of the racks dont support coding (e.g. 1K0909144M). In this case you need to do it via Adaptations. Select "Lane Assist" (Channel 06) from the dropdown in your software and enable it (set it to 1).

EEPROM of the racks can be accessed over OBD. Rack can be flashed to different ROM (partial FW updates only though). Any SW2XXX can be flashed to R SW3501. Contact Edgy#0385 on discord for flash files.

**Edit January 2022**: There is a new [steering rack firmware mod](https://blog.willemmelching.nl/carhacking/2022/01/02/vw-part1/) by Willem Melching (at the time comma employee) which removes both the timebomb and minimal steering speed issues. The delay with no steering after timebomb was shortened from 1 s to 0.01 s (effectively no delay) and the minimum steering speed set to 0 kmh. The blog demonstrated the mod for rack 1K0909144E with firmware 2501 but firmware 3501 was reported to work too. Willem wrote a [VW PQ35 EPS (firmware) flasher](//github.com/pd0wm/pq-flasher).
```


jyoung8607 — 07/25/2023 11:16 AM:
```
I'd be curious what UDS firmware feedback we get from the car, if any
decent chance your engine and trans controllers are too old
but sooner or later I'll pull the KWP2000 over VW CAN TP2.0 libraries in and hit stuff that way
we currently fingerprint on engine, transmission, SRS (airbag), EPS, and the ACC radar
of that set, 2016 and forward NMS supports UDS for everything except EPS, looks like no PQ ever has that
if you have a saved VCDS auto-scan, I'd like to know if you see an "ASAM Dataset" for addresses 01, 02, 13, 15, 44
(you won't on 44, 15 is iffy, rest are wildcards with your retrofit shenanigans)
```