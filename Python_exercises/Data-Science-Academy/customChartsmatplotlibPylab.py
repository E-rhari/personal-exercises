import matplotlib.pyplot as plt
from pylab import *
# mpl.use("WebAgg")

x = linspace(0, 5, 10)
y = x**2

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.175, 0.5, 0.4, 0.3])

axes1.plot(x, y, 'r')
axes2.plot(y, x, 'g')

axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title("Big whatever")

axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title("small whatever")


fig, axMatrix = plt.subplots(nrows=3, ncols=2)

for axList in axMatrix:
    for ax in axList:
        ax.plot(x, y, 'r')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("idk lmao skull emoji")
# fig.tight_layout() # looks cramped and silly


fig, axList = plt.subplots(1,2, figsize=(10, 4))

axList[0].plot(x, x**2, x, exp(x))
axList[0].set_title("Standard Scale")

axList[1].plot(x, x**2, x, exp(x))
axList[1].set_yscale('log')
axList[1].set_title("Logartihmic Scale")


fig, axList = plt.subplots(1,2, figsize=(10, 4))

axList[0].plot(x, x**2, x, exp(x))
axList[0].grid(True)

axList[1].plot(x, x**2, x, exp(x))
axList[1].grid(color = 'b', alpha=0.7, linestyle='dashed', linewidth=0.8)


xx = np.linspace(-0.75, 1., 100)
n  = np.arange(6)

fig, axList = plt.subplots(1,4, figsize=(12,3))

axList[0].scatter(xx, xx + 0.25*rand(len(xx)), color='k')
axList[0].set_title("Scatter")

axList[1].step(n, n**2, lw=2, color='b')

axList[2].bar(n, n**2, align="center", width=0.5, alpha=0.5, color='magenta')
axList[2].set_title("Bar")

axList[3].fill_between(x, x**2, x**3, alpha=0.5, color='g')
axList[3].set_title("Fill Between")


n = np.random.randn(100000)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].hist(n)
axes[0].set_title("Standard Histogram")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative="True", bins=50)
axes[1].set_title("Cumulative Histogram")
axes[1].set_xlim((min(n), max(n)))

plt.show()