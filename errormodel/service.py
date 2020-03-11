import logging
import math
from calculus.methods import *

def runApp(n):
  printEuler(n)
  n = rad(n)
  printSen(n)
  printCos(n)
  return


def printEuler(n):
  try:
    print(n)
    print("e: lib=", math.exp(n), " func=", exp(n), " var=", (math.exp(n)-exp(n)*100)/math.exp(n), " %")
  except:
    logging.error("Euler error")
    

def printSen(n):
  try:
    print("sen: lib=", math.sin(n)," func:", seno(n)," var=", ((math.sin(n)-seno(n))*100)/math.sin(n),"%")
  except:
    logging.error("Sen error")

def printCos(n):
  try:
    print("cos: ", math.cos(n), cosseno(n))
  except:
    logging.error("Cos error")