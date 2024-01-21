import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate sample data
n_samples = 1000
n_components = 2

X, y = make_blobs(n_samples=n_samples,
                       centers=n_components,
                       cluster_std=1,
                       random_state=100)

X1 = X[:, 0]*10 + 50
X2 = X[:, 1]*10 + 100

for i in range(1000):
	print(int(X1[i]))

fig, ax = plt.subplots(dpi=140,figsize=(4,4))
ax.axis("equal")

#plt.scatter(X1, X2, c=y, marker='o',alpha=0.5,s=55,linewidths=.1,edgecolor="k",cmap="turbo")
plt.scatter(X1, X2, c=y, marker='o')

ax.set(xlabel="HP",ylabel="MP")
plt.show()

#for i in range(1000):
#	print(int(X1[i]))

#comstr = "update character set MP = " + str(MP) + " where character_id = " + str(characterID_src) + ";"
#cur = conn.cursor()
#cur.execute(comstr)
#conn.commit()