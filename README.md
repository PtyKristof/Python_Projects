# Projects:

## EV_Test:
    Data source: https://www.kaggle.com/datasets/atechnohazard/battery-and-heating-data-in-real-driving-cycles

### Battery_&_Heating_data_BMWi3: 
The program reads battery measurement data from a BMW i3 (60Ah) electric vehicle stored in a CSV file, generates descriptive statistics for the main battery parameters, and plots the battery current and temperature as functions of time on a shared graph.

### Battery_&_Heating_data_BMWi3_v2:
The program analyzes BMW i3 (60Ah) battery data from a real driving cycle by calculating the regenerative braking ratio, visualizing the state of charge (SoC) decrease over time, evaluating the correlation between vehicle speed and battery current, and detecting abnormal current peaks using statistical analysis.

## Temperature_test:

### Test
Our sensor generates five temperature values between 20 and 60°C, which are averaged and compared to determine the maximum value. The calculated results are displayed at the end.


### Budapest_temp_API
The program retrieves real-time weather data from the internet and displays the temperature of Budapest (latitude = 47.484734, longitude = 19.02533). It receives a 24-element array containing hourly temperatures for the current day, where past and current hours contain actual measurements and future hours contain forecasted values.
    Data source: https://api.open-meteo.com/v1/forecast


## PSFB_Calculations:
This code contains the component sizing calculations required for the design of my DC/DC converter, allowing all parameters to be easily recalculated if the input specifications change.


## CAN:
Data source: https://www.kaggle.com/datasets/pranavjha24/car-hacking-dataset
### CAN_DoS
The program reads the DoS_dataset.csv file, counts the number of normal (R) and attack (T) messages, identifies the CAN ID most frequently targeted by the attack, and calculates the average time interval between messages for both the entire dataset and the attack messages only.

### CAN_Fuzzy
The program reads the Fuzzy_dataset.csv file, counts the number and proportion of normal (R) and attack (T) messages, determines the number of unique CAN IDs present, and identifies the CAN IDs most frequently injected during the fuzzing attack.

### CAN_Geardata
The program reads the gear_dataset.csv file, analyzes the distribution of normal (R) and attack (T) messages, identifies the most frequently targeted CAN ID, and compares the payload patterns of normal and spoofed messages to highlight differences introduced by the gear spoofing attack.