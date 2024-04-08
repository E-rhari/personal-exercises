import numpy

funnyNumbers = numpy.array([69, 420, 101])

print(funnyNumbers)
print(type(funnyNumbers))
print(funnyNumbers.shape)

indices = [1,2]
print(funnyNumbers[indices])

mask = (funnyNumbers % 2 == 0)  # [False, True, False]
print(funnyNumbers[mask])       # [420]