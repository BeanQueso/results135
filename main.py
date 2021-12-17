import matplotlib.pyplot as plt
import pandas as pd
import csv

data = []

solar_mass = []
solar_radius = []
solar_gravity = []
solar_distance = []
name = []

with open("new_merged.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

star_data_rows = data[1:]

for star_data in star_data_rows:
    if len(star_data) < 9:
        star_data_rows.remove(star_data)
    elif len(star_data) == 9:
        solar_mass.append(star_data[6])
        solar_radius.append(star_data[7])
        solar_gravity.append(star_data[8])
        solar_distance.append(star_data[5])
        name.append(star_data[0])

def mass():
    plt.bar(name, solar_mass)    
    plt.title('mass, name')
    plt.xlabel('names')
    plt.ylabel('mass')

    plt.show()

def radius():
    plt.bar(name, solar_radius)    
    plt.title('radius, name')
    plt.xlabel('names')
    plt.ylabel('radius')

    plt.show()

def gravity():
    plt.bar(name, solar_gravity)    
    plt.title('gravity, name')
    plt.xlabel('names')
    plt.ylabel('gravity')

    plt.show()

def distance():
    plt.bar(name, solar_distance)    
    plt.title('distance, name')
    plt.xlabel('names')
    plt.ylabel('distance')

    plt.show()

mass()
radius()
gravity()
distance()