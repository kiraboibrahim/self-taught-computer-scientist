import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.absolute()))

from Chapter3.binary_search import binary_search

names = sorted(["Kirabo", "Ibrahim", "Muniirah", "Bushirah", "Mutoni", "Rashibah"])

print(binary_search(names, "Mutoni"))
