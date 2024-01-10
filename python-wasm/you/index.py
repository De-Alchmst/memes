import argparse

# math.py is already taken
# this is more accurate anyways
from meth import *

###################
# H4X0R U! M46!Ck #
###################

# OOP shenanians
class CargP(argparse.ArgumentParser):
    def error(self, message):
        print("""
⠀⠀⠀⡀⠄⡀⡂⠔⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⡐⠔⡐⡐⡐⡐⡐⡐⡐⠔⡐⡐⠔⡐⠔⡐⠔⡐⡀⡂
⠀⠀⢂⠠⠐⡀⡂⢅⠂⢦⣆⠪⡐⣴⠨⣐⣬⣴⣬⡐⡐⠌⢔⢰⣬⣴⣔⢌⢰⣬⢐⠡⣦⢂⢮⡔⣨⣴⣬⣆⠊⢔⠡⡊⢌⢌⠪⡐⡐⠠
⠀⡈⠠⠐⠐⠠⠨⡂⢅⢻⡿⣷⡐⣿⠨⣾⡃⡢⢹⣷⠨⡊⢔⣿⢑⢄⣝⡃⣺⡷⡐⡡⣿⢐⢿⡇⠍⢅⣾⠟⡨⢂⠪⡨⢊⢢⠱⡐⠌⡂
⠀⠐⢈⠠⠁⠡⡑⢌⠢⣹⡧⡹⣷⣿⠡⢿⣆⢪⣸⡿⠨⠢⡑⣿⣆⢍⣽⡇⡺⣯⣂⢢⣿⢂⢿⡇⢅⢝⣃⠪⢐⠡⡑⡌⡪⠢⡑⢌⢌⢂
⠀⠡⠀⢂⠈⠌⡌⡢⢱⠸⡓⡔⠜⡛⢌⠪⡙⡫⡋⢌⠪⡨⠢⡩⡙⡫⡋⠕⢌⢍⢛⠫⡑⡐⢝⠣⡑⡘⡣⢡⠡⢅⠕⡌⢜⠌⡌⡢⠢⡡
⠀⡁⠈⡀⠠⢑⠔⡜⡌⡆⡣⡑⢌⢌⠢⡢⢱⠨⡊⡢⡑⢅⢢⢑⠌⢆⢕⠡⡑⢌⢢⠡⡑⢌⠢⡑⢌⠢⡑⢌⠌⡎⢜⠰⡡⡑⡱⢨⠪⠨
⠀⠠⠀⠄⠠⡡⡣⡪⡊⡢⡑⢌⢂⠆⠕⢜⢔⠱⡨⢢⢑⠕⡌⡢⢣⠱⡐⢕⡘⡌⡢⡑⡌⡢⡑⢌⠢⡑⢌⢢⠱⡘⡌⢎⠢⡱⡘⢔⠅⠅
⠀⠠⠁⠄⡱⡘⠔⢌⠢⡂⡪⡐⢔⠡⠣⡑⡌⢎⢜⠰⡡⡃⢎⢌⢆⠣⡱⢱⢘⢌⢆⢇⠪⡂⡪⠢⡑⡌⡢⡡⢣⢱⠸⡨⡊⢆⢎⢪⠨⢈
⠀⠂⡁⠰⡨⠢⠩⠢⡑⠌⡂⠌⠐⠨⠨⡂⠪⢢⢑⠕⡌⡊⢆⢕⠰⡑⢜⠰⡑⢕⢱⢑⢕⢕⢱⢑⠕⡌⡆⡣⡱⡡⡣⢱⢘⢔⠥⡁⡂⡂
⠀⢁⠐⠈⡀⠅⠡⠁⠄⠁⢀⠠⠡⡑⡑⢌⢌⠠⢑⢑⢌⠪⡂⢆⢕⢘⢌⢪⢘⠌⡆⡣⡱⡑⡅⡇⡣⡱⡸⡘⡌⡆⡣⡱⢨⢢⢃⠐⠄⡂
⠐⢀⠠⠁⠀⠀⠄⡐⡠⠨⡐⢌⠢⠪⡨⢂⠆⢕⠠⠀⠂⢑⠈⡂⠊⠔⢈⠂⠅⠕⢌⠢⠪⡘⡌⡎⡎⡎⡎⢎⢪⠨⡢⡊⡎⠢⢐⠨⠐⠀
⠐⠠⠐⠈⠠⠈⡐⢅⠪⠨⠢⡡⡑⡑⢌⠢⡡⡑⢌⠪⡐⡠⢀⠀⠂⠐⠀⠀⠂⢈⠠⢈⠪⠨⡪⡸⡸⡸⡸⡘⢔⢑⢌⠆⠅⠅⠂⠐⡀⠅
⠀⠡⠀⠅⠂⠁⡀⠂⠑⢅⠕⡐⠌⢌⠢⡑⢔⢌⠢⡑⢌⠢⡑⢌⠌⡂⡢⢈⢀⠀⠄⠀⠌⠌⡢⡱⡱⡱⡑⢌⠢⡱⠨⠀⠅⠐⠠⢁⢂⠡
⠀⠡⠐⠠⠈⡀⠄⢈⠀⠂⠑⡈⡈⠀⠅⢊⠢⠢⡑⡨⢐⠡⠨⡂⡑⡐⢌⠢⡑⠌⢔⠠⠂⠡⠨⡪⡪⡪⠨⠢⠑⠀⠂⠁⠠⠨⠈⠄⢂⠐
⠀⡁⠐⠀⠂⠀⠄⠀⠄⠂⢰⢕⠔⠀⠠⡀⠱⡑⡐⢌⢐⠡⠁⠂⠂⠈⠂⠅⡊⢌⠢⡡⡑⡡⠡⡣⡣⢪⠈⢄⠢⠂⠠⠈⠄⠡⠈⠌⠠⢈
⠀⠠⠈⢀⠁⠀⠂⠠⠀⢀⠕⡕⡀⡀⠁⠀⡸⠐⠌⠔⡐⠠⣑⠕⠠⠀⠄⠀⠀⡑⠨⡐⡐⢔⢱⢱⠡⠡⡈⢂⠁⠐⠀⠂⢁⠈⠄⡁⠅⠂
⠀⠂⠐⠀⢀⠈⠀⠀⠀⡢⢡⠨⠠⠐⠠⠡⡪⠨⢊⠢⠀⢕⢕⠁⠀⠜⠀⠀⢅⠀⡑⠔⡌⡢⡣⢑⠨⢈⠐⠀⠀⠀⠁⡈⠀⡐⠠⠐⢀⠁
⠀⠐⡀⠈⠀⠀⠀⠀⠀⡘⠔⢌⠢⡡⡱⡑⠅⠅⠅⠌⠄⡑⢕⠔⠠⠠⠀⢅⠕⠡⡌⡇⣇⢧⠣⠁⠊⠀⠀⠀⠀⠀⠀⠀⠠⠀⠐⠈⡀⠄
⠀⠀⠂⠌⠠⠀⠔⢈⠠⠈⢎⠢⡱⡸⢨⠨⢊⠌⡪⢈⠢⢐⠠⠨⠨⠠⡁⡂⡪⡸⡸⡸⡪⡊⠀⠐⠀⠐⠀⠐⠀⠐⠀⠀⠀⠀⠁⠠⠀⠄
⠀⠀⠀⠄⠈⠀⠂⠄⠂⠁⡱⢨⢢⠣⡑⡨⢐⠌⡐⠅⡊⢔⠨⡂⠕⡐⢔⢑⢜⠸⡘⡜⠌⢀⢈⠀⡈⠀⠐⠀⠠⠀⠄⠂⠀⠄⠀⠀⠀⠀
⠀⠀⠀⠄⠀⢀⠡⠐⢀⢂⢎⢎⢢⠱⡰⡘⡔⡑⡌⢌⠢⢑⠨⡐⠡⢊⠔⡐⠔⡑⢌⢊⠠⢐⠀⡂⠠⠈⢀⠐⠠⡀⢀⠀⡀⠀⡀⠀⠁⠀
⠀⠀⠂⠀⠐⠀⠠⠈⠄⡪⡢⡱⡸⡸⡸⡸⡸⡨⡊⡆⢕⠡⠨⢂⠅⢅⢂⠪⡨⣊⠊⢈⠢⠂⠔⠠⠡⢈⠀⠐⢐⠁⡀⠀⠀⡀⠀⠀⠄⠀
⠀⠀⠐⠈⠀⠐⠈⠠⡱⡱⡱⡸⡸⣜⢮⢫⢪⢪⠪⡊⠔⠨⡈⠢⠨⡂⡢⡱⡰⠊⠀⠀⠁⠈⠌⠨⠐⡀⠂⠌⡀⢂⠀⠄⠁⠀⠀⠄⠀⠀
⠀⠀⢁⠠⠈⢀⠨⢊⠎⡎⡮⡪⡏⡮⡪⡣⢣⢡⢱⢐⢅⢑⠨⠨⡊⢔⢜⢔⠅Life in python sucks⠄
⠀⠈⠀⢀⠠⠀⠀⠂⠕⡘⡸⡘⠜⢌⢪⢸⢸⢸⡸⡸⡰⡑⠌⡂⡪⢢⢣⠑⠀use -h to get help⠀⠂⠀
⠀⢀⠁⢀⠠⠀⠈⡀⠐⠀⡂⡊⠨⢐⠠⠡⡑⡕⣌⢊⠪⡪⡨⢂⠪⡊⡂⠀⠠⠀⠀⠀⠐⠈⠀⠀⠀⠐⠀⠀⠀⠐⠈⠀⠀⠄⠠⠐⠀⠁
⠀⢀⠠⠀⠀⠄⠂⠀⢀⠁⢔⢈⠀⠄⠨⠨⠐⠌⡂⡃⢇⢊⠄⢅⠣⠁⠄⡈⢀⠀⠁⠀⠄⠀⡀⠀⠀⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⡀⠀⠀
""")
        exit(420)

parser = CargP()

parser.add_argument('number', type=float, help="or is it");

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--factorial", action="store_true", help="calculate da factoriale")
group.add_argument("--fibonacci", action="store_true", help="calculate da fibonači")
group.add_argument("--circumference", action="store_true", help="calculates length of a circle")
group.add_argument("--circle-surface", action="store_true", help="calculates surface of a disk (a floppy one)")
group.add_argument("--sphere-volume", action="store_true", help="calculates volume of a sphere")
# who wants to write that?

# do some stuff, IDK
args = parser.parse_args()

if args.factorial:
    print(factorial(int(args.number)))

# ↓ whot is this word
elif args.fibonacci: # I'm scared
    print(fibonacci(int(args.number)));

elif args.circumference:
    print(round(circumference(args.number), 4))

elif args.circle_surface:
    print(round(circleSurface(args.number), 4))

elif args.sphere_volume:
    print(round(sphereVolume(args.number), 4))

# who would even pay for something like this?
