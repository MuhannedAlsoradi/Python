# Q.19
yearOfBirth = 1980
age = 0
for year in range(yearOfBirth+1, 2026):
    age += 1
print(f'Person will be {age} in the year {year}')
# Q.20
population = 7e9
growth_rate = 0.011
targetPopulation = 8e9
for year in range(2011, 2100):
    population *= (1+growth_rate)
    if population >= targetPopulation:
        print(f"The population will reach 8 billion in {year}.")
        break

