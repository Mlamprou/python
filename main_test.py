from city_explorer import *
from datetime import datetime, timedelta
import sys

flag = True

vma = sys.version_info.major
vmi = sys.version_info.minor

if vma>=3 and vmi >=4 :
    print("[OK] Python version {}.{}".format(vma,vmi))
else:
    print("[XX] Python version {}.{}".format(vma, vmi))
    flag = False

if 'googlemaps' in sys.modules :
    print("[OK] googlemaps installed")
else:
    print("[XX] googlemaps not installed")
    flag = False

if 'googleplaces' in sys.modules:
    print("[OK] python-google-places installed")
else:
    print("[XX] python-google-places not installed")
    flag = False

if 'wikipedia' in sys.modules:
    print("[OK] wikipedia installed")
else:
    print("[XX] wikipedia not installed")
    flag = False


if flag:
    print("\nEverything is OK !!!")
else:
    print("\nYou have a problem in your installation !!!")


def attraction():
    landmarks=str(input("For which landmarks are you interested in?", zoo, aquarium, art_gallery, museum, church))