import myTemperature as t

c = int(input("Enter your temp in C and we will provide the Feh temp"))
print(c,"celcius is equivlent to", t.CelToFeh(c))

f = int(input("Enter your temp in Feh and we will provide the C temp"))
print(f,"Farenheit is equivalent to", t.FehToCel(f))

