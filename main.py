from calculations import calculate_average, find_max_temperature, find_min_temperature
temperatures=[18,20,22,19,21]
average= calculate_average(temperatures)
max_temperature= find_max_temperature(temperatures)
print(f"The average temperature is: {average}")
print(f"The maximum temperature is: {max_temperature}")
minimum = find_min_temperature(temperatures)

print("Minimum temperature:", minimum)
