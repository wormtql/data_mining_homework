from dm.homework1 import run_homework_1
import sys


if len(sys.argv) == 1:
    arg = "homework1"
else:
    arg = sys.argv[1]

if arg == "homework1":
    run_homework_1()