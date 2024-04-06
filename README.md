# VW Passat B6


jyoung8607:
```
https://www.carsystems.eu/vw-passat-3c0-b6-park-assist-pla-1-5-upgrade,id2349.html
it appears to have EPS, and a smart enough EPS to do parallel park assist... I wouldn't call that confirmed, but it's a good omen 
aww yeah look at those login codes on that carsystems link... lane assist is in the cards
can't really confirm without verifying your EPS P/N with an Auto-Scan, but I'm liking it
```

-- see asi maksab 299 eur + kodeerimine

@kamold proovib toole saada

Passat B6 (2005 -) and B7 ( - 2015) (EU) are PQ46


@carlos_ddd My Passat is a B6 with factory ACC. I have coded Lane Assist in the steering rack. The EON display does not show any speed,  always stays on 0 and MAX N/A is static. The ACC stalk does not change anything on the EON.


We need a cabana log of your drive. Although B6 is PQ it is vastly different from B7 since ACC and lane assist are on powertrain CAN. There simply is no extended CAN as on B7


http://www.volkspage.net/technik/ssp/ssp/SSP_238.pdf


VW
A 2008 vw can run op :p
Kozuch — 12/02/2020 9:01 PM
@dkiiv He means stock car from 2010. Anyways probably a 2005 VW with few retrofits can run OP too... Maybe even earlier, dont really know when PQ35/46 started. VW has a lot of potential! 😉
dkiiv — 12/02/2020 9:03 PM
@Kozuch stock 2008-9 can run op
Kozuch — 12/02/2020 9:05 PM
@dkiiv which model exactly?
dkiiv — 12/02/2020 9:48 PM
any with a gen3 steering rack


https://www.youtube.com/watch?v=L1u6AkSpR98l


https://github.com/commaai/openpilot/wiki/Volkswagen-PQ



## Todo

- check if we have v3 steering rack
- enable LKAS over OBD 





I do have the J533 harness already installed. I wonder if I need to leave the original J533 connection in during these steps.

Would that make a difference? I figured that the harness was just acting as a passthrough device but maybe it's causing issues
jyoung8607 — 06/08/2023 9:47 AM
On PQ it's in Adaptations, not Coding
olid — 06/08/2023 10:12 AM
I'm so sorry for all of the questions, but do you know which adaptations to manipulate? Is there a guide for enabling LKAS functionality on PQ/NMS cars?

I have both Car Scanner and OBDEleven at my disposal 
jyoung8607 — 06/08/2023 10:12 AM
It's called either Lane Assist or Heading Control Assist
There aren't that many Adaptations in address 44, you'll figure it out


Okay 🙂 using obd11, it correctly recognizes my car as an NMS Passat

But when I go to control unit 44 (steering assistance) and select the adaptations option, it asks for a channel number (with 256 possible values). Since I don't know the channel to choose, I just select channel 0 and go through them all. I've cycled through them and nearly all of them are null (?) channels. Some of them say Not Available as their "value" and others just have an int as their value but they don't have any descriptions. Check out this video to see what I mean.

I'm kind of at a loss here. If there were channel/adaptations/coding manuals that I could reference then I could do more digging but I'm kind of ready to give up and return the comma.

@jyoung8607 do you have any plans to create a script like vw_mqb_config.py for NMS/PQ cars? I wouldn't mind testing it. No worries if not! That'll just be the end of my Comma journey until a future date 😢


@olid someday I will do a PQ config script, just haven't gotten around to it. it requires bringing in an external dependency to support KWP2000-over-VW CAN TP2.0 diagnostic sessions instead of the more modern UDS over CAN ISO-TP