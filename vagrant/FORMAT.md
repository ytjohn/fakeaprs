

````
N3SNN-1>APK101,K3ARL-5*,WIDE2-1:!4128.8 NS07815.6 W#PHG7660 Whittimore Hl Hi-Level Digi Emporium PA<0x0d>
NU3S-7>APK102,W3EXW,K3ARL-6,WIDE2*:=4022.75N/08004.80W_000/002g008t037r   p   P035h98b10186KU2k<0x0d>
K3HPA-1>APU25N,W3YA-1,K3ARL-6,WIDE2*:@281838z4048.86N/07753.74W_267/003g003t044r000P000p000h81b10130State College WX {UIV32N}<0x0d>
````


[ftp://ftp.tapr.org/aprssig/aprsspec/spec/aprs101/APRS101.pdf]

All APRS transmissions use AX.25 UI-frames, with 9 fields of data:

* Flag — The flag field at each end of the frame is the bit sequence 0x7e
that separates each frame.
*  Destination Address — This field can contain an APRS destination
callsign or APRS data. APRS data is encoded to ensure that the field
conforms to the standard AX.25 callsign format (i.e. 6 alphanumeric
characters plus SSID). If the SSID is non-zero, it specifies a generic
APRS digipeater path.
* Source Address — This field contains the callsign and SSID of the
transmitting station. In some cases, if the SSID is non-zero, the SSID
may specify an APRS display Symbol Code.
* Digipeater Addresses — From zero to 8 digipeater callsigns may be
included in this field. Note: These digipeater addresses may be
overridden by a generic APRS digipeater path (specified in the
Destination Address SSID).
* Control Field — This field is set to 0x03 (UI-frame).
* Protocol ID — This field is set to 0xf0 (no layer 3 protocol).
* Information Field — This field contains more APRS data. The first
character of this field is the APRS Data Type Identifier that specifies the
nature of the data that follows.
* Frame Check Sequence — The FCS is a sequence of 16 bits used for
checking the integrity of a received frame.

### Timestamps

Per convention, most RF packets do NOT send a timestamp. All RF communication is considered to be
realtime. Most clients are expected to put a received timestamp im place, but the timestamp on the
transmitting system is considered untrustworthy.

    092345z is 2345 hours zulu time zulu on the 9th day of the month.
    281838z is 18 hours 38 minutes zulu on the 28th day of the month.
    10092345 is 23 hours 45 minutes zulu on October 9th.
    

## Exploded

`K3HPA-1>APU25N,W3YA-1,WIDE2-1:@281838z4048.86N/07753.74W_267/003g003t044r000P000p000h81b10130State College WX {UIV32N}<0x0d>`

Breakdown:

* `K3HPA-1>APU25N` = from K3HPA to APU25N
* `W3YA-1` = via W3YA-1
* `WIDE2-1` = Path 2 -1 (Two hops in all directions) http://info.aprs.net/index.php?title=Paths
* `:` split between header and body
* `@281838z` 18 hours, 38 minutes Zulu on 28th day of month. Timestamps are optional, and considered untrustworthy. All RF traffic is considered live, and received timestamp is more relevant.
* `4048.86N`  latitude (DDMM.SS) 40.81433333333333
* `07753.74W` = longitude (DDMM.SS)  -77.89566666666667
* `_267` = bearing 267 degrees
* `/003g003t044r000P000p000h81b10130`  http://www.aprs.net/vm/DOS/WX.HTM
  * `/003` background radiation level
  * `g003` rain gauge reading
  * `t044` 44F
  * `r000` = 0 hundredths of an inch of rain in the LAST HOUR
  * `P000` = 0 precip in last 24 hours
  * `h81` = 81% humidity
  * `b10130` = 10130 tenths of millibars
* State College WX {UIV32N}` = description: State College Weather Station running UI-View 32
* `<0x0d>` packet seperation field


## BEACONS


`FROMCALL->BEACON:FROMCALL COMMENT<0x0d)`

```
W3YA-1>BEACON:W3YA-1 Nittany Amateur Radio Club Digipeater<0x0d>
K3ARL-6>BEACON:K3ARL Ogletown APRS Digipeater<0x0d>
K3ARL-5>BEACON:K3ARL Brush Mountain APRS-RPTR<0x0d>
```

