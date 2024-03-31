import csv
from collections import defaultdict


province_hospitals = defaultdict(int)


with open("hospitals.csv") as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        for year in range(2012, 2018):
            hospitals = row[str(year)]
            if hospitals.isdigit():
                province_hospitals[row['Hududlar']] += int(hospitals)


sorted_provinces = sorted(province_hospitals.items(), key=lambda x: x[1], reverse=True)


print("Hospitals built between 2012 and 2017:")
for province, count in sorted_provinces[:3]:
    print(f"{province}: {count} hospitals")
