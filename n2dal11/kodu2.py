import numpy
def transponeeriK(maatriks):
    a = numpy.array(maatriks)
    a = numpy.flip(a, -1)
    a = a.transpose()
    a = numpy.flip(a, -1)
    return a.tolist()

print(transponeeriK([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]))
print("[[9, 6, 3], [8, 5, 2], [7, 4, 1]]")

print(transponeeriK([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]]))
print("[[8, 6, 4, 2], [7, 5, 3, 1]]")

print(transponeeriK([[4, 31, 67, 99]]))
print("[[99], [67], [31], [4]]")