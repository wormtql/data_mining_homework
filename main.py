from dm.homework1 import run_homework_1
from dm.homework2 import run_homework_2
from dm.big_homework import big_homework
import sys


if len(sys.argv) == 1:
    arg = "homework1"
else:
    arg = sys.argv[1]

if arg == "homework1":
    run_homework_1()
elif arg == "homework2":
    run_homework_2()
elif arg == "big_homework":
    big_homework()
