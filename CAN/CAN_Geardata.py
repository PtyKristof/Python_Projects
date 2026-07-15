import pandas as pd
from pathlib import Path

csv_path = r"C:\Users\Kristóf\Desktop\CSV\CAN\gear_dataset.csv"


# Oszlopneveket mi adjuk meg, mert a fájlban nincs fejléc.
#    timestamp, can_id, dlc, majd 8 darab data oszlop, végül flag.
column_names = ["timestamp", "can_id", "dlc"] + [f"data{i}" for i in range(8)] + ["flag"] 
df = pd.read_csv(csv_path, header=None, names=column_names)



""" Unix timestamp = 1970. január 1. óta mennyi idő telt el

print(f"Beolvasott sorok száma: {len(df)}")
print("\nElső 5 sor:")
print(df.head())
 
print("\nOszlopok típusa:")
print(df.dtypes)

"""

# R = normál (regular), T = injektált (támadás) üzenet
print("\nR / T eloszlás:")
print(df["flag"].value_counts())
attack_ratio = (df["flag"] == "T").mean() * 100
print(f"Támadás-üzenetek aránya: {attack_ratio:.2f}%")
 
# Hány egyedi CAN ID fordul elő = Ennyi ECU van 
print(f"\nEgyedi CAN ID-k száma: {df['can_id'].nunique()}")
 
# A leggyakoribb CAN ID-k T (támadás) üzeneteknél -> melyik ID-t célozzák
attack_rows = df[df["flag"] == "T"]
if len(attack_rows) > 0:
    print("\nLeggyakoribb CAN ID a TÁMADÁS üzeneteknél:")
    print(attack_rows["can_id"].value_counts().head(5))



data_cols = [f"data{i}" for i in range(8)]

if len(attack_rows) > 0:
    # Melyik ID-t hamisítják legtöbbször? -> erre fókuszálunk
    target_id = attack_rows["can_id"].value_counts().idxmax()
    print(f"\n{'='*60}")
    print(f"PAYLOAD ÖSSZEHASONLÍTÁS - CAN ID: {target_id}")
    print(f"{'='*60}")

    # Ugyanezen ID normál (R) sorai, és a hamisított (T) sorai
    normal_on_id = df[(df["can_id"] == target_id) & (df["flag"] == "R")]
    attack_on_id = df[(df["can_id"] == target_id) & (df["flag"] == "T")]

    print(f"Normál (R) üzenetek ezen az ID-n: {len(normal_on_id):,}")
    print(f"Hamisított (T) üzenetek ezen az ID-n: {len(attack_on_id):,}")

    print("\nNormál üzenetek leggyakoribb payloadjai (top 3):")
    print(normal_on_id[data_cols].value_counts().head(3))

    print("\nHamisított üzenetek leggyakoribb payloadjai (top 3):")
    print(attack_on_id[data_cols].value_counts().head(3))

    # Hány EGYEDI payload-mintázat van a kétféle csoportban
    n_unique_normal = normal_on_id[data_cols].drop_duplicates().shape[0]
    n_unique_attack = attack_on_id[data_cols].drop_duplicates().shape[0]
    print(f"\nEgyedi payload-mintázatok száma: normál={n_unique_normal}, hamisított={n_unique_attack}")
