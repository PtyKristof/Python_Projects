#import kagglehub

#path = kagglehub.dataset_download("atechnohazard/battery-and-heating-data-in-real-driving-cycles")
#print("Path to dataset files:", path)
import matplotlib.pyplot as plt
import pandas as pd

csv_path = r"C:\Users\Kristóf\.cache\kagglehub\datasets\atechnohazard\battery-and-heating-data-in-real-driving-cycles\versions\1\TripB01.csv"

df = pd.read_csv(csv_path, encoding="latin1", sep=";") #nem utf8 és spe azért kell, mert az adatok ; vel vannak elválasztva

# Alap adatok kiírása:

#print(df.shape)        #hány sor, hány oszlop
#print(df.columns)      #oszlopnevek
#print(df.head())       #első 5 sor
#print(df.dtypes)       #oszlopok típusai


# Fontosabb értékek listázása:
print(df[["Battery Voltage [V]", "Battery Current [A]", "Battery Temperature [°C]", "SoC [%]"]].describe())


# Matlab plot szerű kirajzolás
#df.plot(x="Time [s]", y="Velocity [km/h]", title="Sebesség az idő függvényében")
#plt.show()

#df.plot(x="Time [s]", y="Battery Temperature [°C]", title="Akkumulátor hőmérséklet")
#plt.show()

df.plot(x="Time [s]", y=["Battery Current [A]", "Battery Temperature [°C]"], 
        title="Áram és hőmérséklet együtt", secondary_y="Battery Temperature [°C]")
plt.show()

