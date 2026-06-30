import matplotlib.pyplot as plt
import pandas as pd

csv_path = r"C:\Users\Kristóf\.cache\kagglehub\datasets\atechnohazard\battery-and-heating-data-in-real-driving-cycles\versions\1\TripB02.csv"

df = pd.read_csv(csv_path, encoding="latin1", sep=";") #nem utf8 és spe azért kell, mert az adatok ; vel vannak elválasztva


#regfék arány számítás
regen_points = df[df["Battery Current [A]"] < 0]
print(f"A mérési pontok {len(regen_points)/len(df)*100:.1f}%-ában történt regeneratív töltés")

#SoC ellenőrzése időben
df.plot(x="Time [s]", y="SoC [%]", title="Töltöttség csökkenése a menet során")
plt.show()

#korreláció a sebesség és az áram között
correlation = df["Velocity [km/h]"].corr(df["Battery Current [A]"])
print(f"Korreláció sebesség és áram között: {correlation:.3f}")

#anomália detektálás
threshold = df["Battery Current [A]"].mean() + 3 * df["Battery Current [A]"].std()
anomalies = df[df["Battery Current [A]"] > threshold]
print(f"{len(anomalies)} db szélsőséges áramcsúcs (3 szórásnál nagyobb)")
print(anomalies[["Time [s]", "Battery Current [A]", "Velocity [km/h]"]])