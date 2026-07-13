#Component caluclations for the PSFB DC/DC converter

import math

# Input:

Vin_min=455
Vin_max=600

# Output:

Vout=24
D_max=0.8
#Vout_2=20
Iout=25
Pout=Vout*Iout

# Other:

fs=100e3 #100kHz
T=1/fs #10us
Iout_ripple=Iout*0.2 #20%
Vout_ripple=Vout*0.02 #2%
Vin_ripple=2

# Ratio

N=math.floor((Vin_min*D_max)/Vout) # lefelé kerekítünk
print(N)

D_max=Vout / (Vin_min/N)# Ez az érték Vmin-nél
D_min=Vout / (Vin_max/N) # Ez az érték Vmax-nál

D_min=0.5
D_max=0.8

t_min=D_min*T # Max tbe idő
t_max=D_max*T # Min tbe idő
print(Iout_ripple)

# Kimeneti fojtó: itt a legrosszabb eset, amikor Vin_max -> itt a legkisebb a duty cycle -> itt a legnagyobb az áramhullámosság (=t_off hosszabb idő)
# Induktivitás képlete: U = L*(Δi/Δt) -> Δi= (U*Δt)/L -> Δi= (0-Uki)*(1-Dmin) / (L*2*fs) = (Uszek-Uki)*Dmin / (L*2*fs)
# Szekunder oldalon a frekvencia a duplája fs-nek egyenirányítás miatt: 

L=(Vout*(1-D_min)) / (2*fs*Iout_ripple)
print(L)

# Kimeneti tekercs: C=Q/U

C=(Iout_ripple*T*2)/(8*Vout_ripple)
print(C)