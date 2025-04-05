def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def usd_to_euro(usd, exchange_rate=0.85):
    return usd * exchange_rate

def mph_to_kph(mph):
    return mph * 1.60934

def liters_to_gallons(liters):
    return liters * 0.264172

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    # Temperature Conversion
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")

    # Distance Conversion
    kilometers = float(input("\nEnter distance in Kilometers: "))
    miles = kilometers_to_miles(kilometers)
    print(f"{kilometers} Kilometers is {miles} Miles")

    # Weight Conversion
    pounds = float(input("\nEnter weight in Pounds: "))
    kilograms = pounds_to_kilograms(pounds)
    print(f"{pounds} Pounds is {kilograms} Kilograms")

    # Currency Conversion
    usd = float(input("\nEnter amount in USD: "))
    exchange_rate = float(input("Enter exchange rate (default is 0.85): ") or 0.85)
    euros = usd_to_euro(usd, exchange_rate)
    print(f"{usd} USD is {euros} Euros")

    # Speed Conversion
    mph = float(input("\nEnter speed in Miles per Hour: "))
    kph = mph_to_kph(mph)
    print(f"{mph} Miles per Hour is {kph} Kilometers per Hour")

    # Volume Conversion
    liters = float(input("\nEnter volume in Liters: "))
    gallons = liters_to_gallons(liters)
    print(f"{liters} Liters is {gallons} Gallons")

    # BMI Calculation
    weight = float(input("\nEnter weight in Kilograms: "))
    height = float(input("Enter height in Meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"BMI is {bmi}")

if __name__ == "__main__":
    main()