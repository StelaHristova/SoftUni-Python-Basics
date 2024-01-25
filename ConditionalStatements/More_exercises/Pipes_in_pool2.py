import math

volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

water = (pipe_1 + pipe_2) * hours
full = water / volume * 100
pipe1_procent = pipe_1 * hours / water * 100
pipe2_procent = pipe_2 * hours / water * 100

if water <= volume:
    print(f"The pool is {full:.2f}% full. Pipe 1: {pipe1_procent:.2f}%. Pipe 2: {pipe2_procent:.2f}")
else:
    print(f"For {hours:.2f} hours the pool overflows with {water - volume:.2f} liters.")