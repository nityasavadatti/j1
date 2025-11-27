import sys

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    print("No command-line input given — using input() method:")
    principal=1000
    rate =3
    time = 8

# Validate values
if principal <= 0:
    print("Principal must be greater than 0")
elif rate <= 0:
    print("Rate must be greater than 0")
elif time <= 0:
    print("Time must be greater than 0")
else:
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest =", simple_interest)
