import matplotlib as mpl
import matplotlib.pyplot as plt
# mpl.use("WebAgg")

# plt.figure()
plt.plot([1,2,3], [2,4,7])
# plt.show() # super important!

plt.figure() # creates a new figure
x = [1,2,3,7]
y = [6,9,16,19]
plt.plot(x, y)
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
plt.title("Funny numbers")
# plt.show()

plt.figure()
x = list(map(lambda x: x**2, x))
y = list(map(lambda x: x**2, y))
plt.plot(x, y, label="idk lol")
x = list(map(lambda x: x**2, x))
y = list(map(lambda x: x**2, y))
plt.plot(x,y, label="haha big line lmao")
plt.legend()
# plt.show()


# ## bar chart ##
y = [101,  69, 420, 60, 61, 54, 84, 32, 65, 94, 78, 151, 454, 65, 1, 56, 87, 365, 85]
x = range(1,len(y)+1)
plt.figure()

plt.bar(x,y, color="orange", label="Some random numbers lmao")

y = [a/2 for a in y]
plt.bar(x,y, color="green", label="Same bullshit numbers but a half smaller")

plt.legend()

plt.figure()
plt.plot(x,y, color="orange", label="idk lol")
plt.bar(x,y, color="green", label="same but it's a line now")
plt.legend()


# ## Histogram ##
y = [1, 1, 1, 1, 3, 5, 6, 8, 1, 1, 2, 3, 4, 1, 2, 3, 2, 3, 4, 5, 2, 2, 2, 2]
x = range(1,len(y)+1)
plt.figure()
plt.hist(y, x, histtype="bar", rwidth=0.8)


plt.figure()
plt.hist(y, x, histtype="stepfilled", rwidth=0.8)


# ## scatter plot ##
plt.figure()
plt.scatter(x, y, label = "spotty spots", color="pink", marker="o")
plt.legend()

plt.figure()
plt.scatter(y, x, label = "spotty spots", color="cyan", marker="*")
plt.legend()


# ## stakplot ## 
a = [1,2,3,4,5]
b = [10-z for z in a]
c = [z**2 for z in a]
d = [(z*9)//2 for z in c]

x = range(1, len(a)+1)

plt.figure()
plt.stackplot(x, a, b, c, d, colors=['m', 'c', 'r', 'k', 'g'], labels=['a', 'b', 'c', 'd'])
plt.legend()


# ## https://www.youtube.com/watch?v=czTksCF6X8Y ##
plt.figure()
slices     = [2,        2,     19,     1]
activities = ['sleep', 'eat', 'game', 'repeat']
colors = ["olive", 'lime', 'violet', 'royalblue']
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0,0.2,0,0))
plt.show()







plt.show()