import timeit
import pycipher

print(timeit.timeit('pycipher.Caesar(12).encipher("hi")'))
print(timeit.timeit('pycipher.Caesar(12).decipher("hi")'))