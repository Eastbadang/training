import matplotlib.pyplot as plt
# 주석
# a="한글입력이 어떤가요?"
# print(a)

x=range(0,100)
y=[v*v for v in x]
plt.plot(x,y,'ro')
plt.show()


