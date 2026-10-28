# print("Willkommen bei Autopulse! Bitte geben Sie Ihre Daten ein: ")

NORMAL_LIMIT = 80
WARNING_LIMIT = 1000

def check_machine_status(machine_name,temperature):


        #Maschinenzustand überprüfen
    if temperature < NORMAL_LIMIT:
        status = "Normal"
    elif temperature >= NORMAL_LIMIT and temperature < WARNING_LIMIT:
        status = "Warnung"
    else:
        status = "Kritisch"

    return status

    print("------------------------------")
 

machines = [
    ("Motor 01", 65.5),
    ("Motor 02", 45.0),
    ("Motor 03", 75.2),
    ("Motor 04", 55.0),
    ("Motor 05", 80.0)
]

for (machine_name, temperature) in machines:
    check_machine_status(machine_name, temperature)

normal_count = 0
warning_count = 0
critical_count = 0

for (machine_name, temperature) in machines:

    status = check_machine_status(machine_name, temperature)
    print(f"Maschinenname: {machine_name}")
    print(f"Aktuelle Temperature: {temperature} °C")
    print(f"Maschinenzustand: {status}")
    print("------------------------------")


    if status == "Normal":
        normal_count += 1
    elif status == "Warnung":
        warning_count += 1
    else:
        critical_count += 1
print("----------Maschinenstatistik----------") 

print("Anzahl der Maschinen im Normalzustand:", normal_count)
print("Anzahl der Maschinen im Warnzustand:", warning_count)
print("Anzahl der Maschinen im kritischen Zustand:", critical_count)


total_temperature = 0
machine_count = 0

for (machine_name, temperature) in machines:
    total_temperature += temperature
    machine_count += 1

    average_temperature = total_temperature / machine_count
print("----------")
print(f"Durchschnittliche Temperatur aller Maschinen: {average_temperature} °C")