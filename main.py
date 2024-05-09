def heating_cooling(actual_temp, desired_temp, actual_unit="C", desired_unit="C"):
    # Convert temperatures to Celsius
    actual_temp_celsius = convert_temp(actual_temp, actual_unit)
    desired_temp_celsius = convert_temp(desired_temp, desired_unit)

    if actual_temp_celsius < desired_temp_celsius:
        print("Run heat")
    elif actual_temp_celsius > desired_temp_celsius:
        print("Run A/C")
    else:
        print("Standby")

def convert_temp(temp, unit):
    if unit == "C":
        return temp
    elif unit == "F":
        return (temp - 32) * 5/9
    elif unit == "K":
        return temp + 273.15
    else:
        return "Invalid unit"

# Testing the thermostat function with temperature units specified
heating_cooling(20, 25, "C", "C")  # Should print "Run heat"
heating_cooling(77, 60, "F", "F")  # Should print "Run A/C"
heating_cooling(293.15, 293.15, "K", "K")  # Should print "Standby"

# Prompting the user for actual and desired temperatures with units
actual_temp = float(input("Enter the actual temperature: "))
actual_unit = input("Enter the unit of the actual temperature (C, F, or K): ")
desired_temp = float(input("Enter the desired temperature: "))
desired_unit = input("Enter the unit of the desired temperature (C, F, or K): ")
heating_cooling(actual_temp, desired_temp, actual_unit.upper(), desired_unit.upper())
