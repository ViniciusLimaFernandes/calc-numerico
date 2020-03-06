import logging

def inputInteger():
  try:
    x = input("Insert a number: ")
    return int(x)
  except:
    logging.error("Invalid input, expected: Number")
    return
  