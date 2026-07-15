"""

CAN Protocol Basics

CAN ID (Arbitration ID): Every CAN message has an identifier (e.g., 0x316) that specifies the type of data it carries (e.g., engine speed, vehicle speed, or door status). A lower CAN ID has a higher priority on the bus.
DLC (Data Length Code): Indicates the number of data bytes contained in the message (0–8 bytes).
Data (Payload): The actual hexadecimal data, for example 05 21 68 09 21 21 00 6F, which is interpreted by the corresponding Electronic Control Unit (ECU).
Timestamp: Indicates when the message was transmitted on the CAN bus.

CAN Bus Attacks

Denial-of-Service (DoS): The attacker continuously transmits the highest-priority CAN ID (e.g., 0x000) to flood the bus, causing the time interval between messages to decrease dramatically.
Fuzzing: The attacker injects random CAN IDs and random payloads onto the bus, resulting in unusual message IDs that would not normally appear during regular operation.
Spoofing: The attacker forges an existing CAN ID (e.g., one used for engine RPM) and injects false data, causing the frequency or payload of that ID to deviate from its normal behavior.
Replay Attack: Previously recorded legitimate CAN messages are retransmitted at a later time. These attacks are more difficult to detect because the messages themselves are valid, but they are sent at incorrect times.

"""

import pandas as pd
from pathlib import Path

csv_path = r"C:\Users\Kristóf\Desktop\EV_Projekt\Python_Projects\CAN\CSV\DoS_dataset.csv"

 
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

