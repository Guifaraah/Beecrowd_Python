A = float(input(""))
B = float(input(""))
C = float(input(""))

if 0 <= A and B and C <= 10.0:
    Media = (A * 2 + B * 3 + C * 5) / 10
    print("MEDIA = {:.1f}".format(Media))