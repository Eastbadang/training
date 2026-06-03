import time
from matplotlib import pyplot as plt
import Image

# https://matplotlib.org/gallery.html

plt.plot([1,2,3], [110,130,120])
plt.show()
time.sleep(1)
print("Good Bye")
plt.close()

plt.plot(["Seoul","Paris","Seattle"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.show()
plt.close()

y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show()
plt.close()