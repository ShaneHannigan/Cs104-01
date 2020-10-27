Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp = 0
while temp < 999:
    temp = int(input("Enter the current temperature: "))
    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Wear long sleeves")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a coat")
    else:
        print("Don't go out")