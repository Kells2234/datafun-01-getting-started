"""
Complete the script
"""

print("NASCAR!")
print()
print("Enter the number of caution laps in the last seve Daytona 500 NASCAR Races")
print()
value1 = input('Enter 2015 race total: ')
value2 = input('Enter 2016 race total: ')
value3 = input('Enter 2017 race total: ')
value4 = input('Enter 2018 race total: ')
value5 = input('Enter 2019 race total: ')
value6 = input('Enter 2020 race total: ')
value7 = input('Enter 2021 race total: ')
value8 = input('Enter 2022 race total: ')
print()
lap_sum = int(value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8)
lap_average = int(lap_sum / 8)
# This information is to be to perform calculations for the sum and average number of caution laps
print("Here are the stats for the number of caution laps run")
print(f"The 2015 race={value1}, The 2016 race={value2}, The 2017 race={value3}, The 2018 race={value4}, The 2019 race={value5}, The 2020 race={value6}, The 2021 race={value7} and the 2022 race={value8}")
print()
print("The average number of caution laps")
print(lap_average)
print()
print("Total number of caution laps run")
print(lap_sum)
print()

