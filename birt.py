import time
import datetime  # fix the 12th month and days
sd = time.time()
df = int(datetime.datetime.fromtimestamp(sd).strftime('%Y'))
d0 = int(datetime.datetime.fromtimestamp(sd).strftime('%m'))
d2 = int(datetime.datetime.fromtimestamp(sd).strftime('%d'))
do = int(input("y"))
dn = int(input("M"))
dz = int(input("D"))
sg = True
gg = True
wrez = dn
stq = 0
ouui = 0
oad = 0
while sg == True:
    do += 1
    print(do)
    stq += 1
    if do == df:
        sg = False
if dn == d0:
    stq -= 1
    print(stq)
    print(12)
    daysa = True
    sesw = False
    bqw = False
else:
    while gg == True:

        if dn > d0:
            stq -= 1
            boi = True
            bqw = True
            sesw = False
            daysa = False
            while boi == True:
                ouui += 1
                wrez += 1
                if wrez == 13:
                    ouui += d0
                    ouui -= 1
                    print(stq)
                    print(wrez)
                    print(ouui)
                    boi = False
                    gg = False

        if dn < d0:
            bdaw = dn
            assss = True
            adw3 = 0
            while assss == True:
                bdaw += 1
                adw3 += 1
                if bdaw == d0:
                    #  print(stq)
                    #  print(adw3)
                    daysa = False
                    bqw = False
                    sesw = True
                    assss = False
                    gg = False
if daysa == True:
    tw = dz
    uis = 0
    q4r = True
    if d2 < dz:
        ert = True
        while ert == True:
            tw -= 1
            if tw == d2:
                print(stq)
                print(ouui - 1)
                print(tw + 14)
                ert = False
                daysa = False
    tw = dz
    uis = 0
    if d2 == dz:
        stq += 1
        print(stq)
        print(0)
        print(0)
    if d2 < dz:
        ert = True
        while ert == True:
            tw -= 1
            uis += 1
            if tw == d2:
                uis -= 1
                ert = False
        a34 = 30 - uis
        a34 += 1
        print(stq)
        print(11)
        print(a34)
    if d2 > dz:
        stq += 1
        qsr = True
        while qsr == True:
            tw += 1
            uis += 1
            if tw == d2:
                print(stq)
                print(0)
                print(uis)
                qsr = False
if bqw == True:  # somethin's wrong here
    tw = dz
    uis = 0
    q4r = True
    if d2 < dz:
        ert = True
        while ert == True:
            tw -= 1
            if tw == d2:
                print(stq)
                print(ouui - 1)
                print(tw + 14)
                ert = False
                q4r = False
    while q4r == True:
        tw += 1
        uis += 1
        if tw == d2:

            print(stq)
            print(ouui)
            print(uis)
            q4r = False
if sesw == True:
    tw = dz
    uis = 0
    q5r = True
    if d2 < dz:
        ert = True
        while ert == True:
            tw -= 1
            uis += 1
            if tw == d2:
                print(stq)
                print(adw3 - 1)
                print(uis + 14)
                ert = False
                q5r = False
    while q5r == True:
        tw += 1
        uis += 1
        if tw == d2:
            print(stq)
            print(adw3)
            print(uis)
            q5r = False
