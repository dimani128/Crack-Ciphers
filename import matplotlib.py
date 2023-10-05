import matplotlib.pyplot as plt
import random

plt.plot([i ** random.randint(2, 3) for i in range(100)])
plt.ylabel('some numbers')
plt.show()
