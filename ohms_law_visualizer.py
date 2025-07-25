import matplotlib.pyplot as plt


voltage = 10  


resistances = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


currents = [voltage / r for r in resistances]


plt.figure(figsize=(8, 5))
plt.plot(resistances, currents, marker='o', linestyle='-', color='blue')
plt.title("Ohm's Law: Current vs Resistance")
plt.xlabel("Resistance (Ω)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.savefig("graph-screenshot.png")  
plt.show()
