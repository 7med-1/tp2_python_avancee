import matplotlib.pyplot as plt

#donnees d'entrer
jours = [1, 2, 3, 4, 5, 6, 7] # Lun a Dim
débit = [85, 92, 78, 95, 88, 60, 45] # en Mb/s
latence = [12, 10, 18, 9, 11, 20, 28] # en ms

#premiere subplot  | debit | blue caree  
plt.subplot(1, 2, 1)
plt.plot(débit,color='blue', marker='s')
plt.title("debit") 
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.grid(True)
plt.legend(title='Legend Title')

#deuxeme  subplot  | latence | rouge triangle 
plt.subplot(1, 2, 2)
plt.plot(latence,color='red', marker='^')
plt.title("Title") 
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.grid(True)
plt.legend(title='Legend Title')

plt.show()

#suavegarder sou form de png 
plt.savefig("reseau.png", dpi=150)