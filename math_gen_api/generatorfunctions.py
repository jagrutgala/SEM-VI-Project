import math, random

from questionGen_attempt1 import Question

# Decorator QGEN
def questionGen():
    pass


##############################
# BASIC Question Types
##############################
def basicType1(difficulty):
    format_string = "{} + {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2), 
        eval(format_string.format(num1, num2)),
        "bas")

def basicType2(difficulty):
    format_string = "{} - {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2), 
        eval(format_string.format(num1, num2)),
        "bas")

def basicType3(difficulty):
    format_string = "{} * {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2), 
        eval(format_string.format(num1, num2)),
        "bas")

def basicType4(difficulty):
    format_string = "{} / {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2), 
        eval(format_string.format(num1, num2)),
        "bas")


##############################
# LCM Question Types
##############################
def lcmType1(difficulty):
    format_string = "{}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2), 
        1,
        "lcm")

def lcmType2(difficulty):
    format_string = "{} , {}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2, num3), 
        1,
        "lcm")

def lcmType3(difficulty):
    format_string = "{} , {}, {}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2, num3, num4), 
        1,
        "lcm")

def lcmType4(difficulty):
    format_string = "{} , {}, {}, {}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    num5 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2, num3, num4, num5), 
        1,
        "lcm")

##############################
# HCF Question Types
##############################
def hcfType1(difficulty):
    format_string = "{}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2), 
        1,
        "hcf")

def hcfType2(difficulty):
    format_string = "{} , {}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2, num3), 
        1,
        "hcf")

def hcfType3(difficulty):
    format_string = "{} , {}, {}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2, num3, num4), 
        1,
        "hcf")

def hcfType4(difficulty):
    format_string = "{} , {}, {}, {}, {}"
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    num5 = random.randint(1, 100)
    return Question(
        format_string.format(num1, num2, num3, num4, num5), 
        1,
        "hcf")