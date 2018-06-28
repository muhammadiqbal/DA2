import numpy as np 
import matplotlib.pyplot as plt  
from sklearn.svm import SVR
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm

url = "test4D.csv"

# Assign colum names to the dataset
colnames = ['x1', 'x2', 'x2', 'x3', 'Val']

# Read dataset to pandas dataframe
X12 = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(0,1))
X23 = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(2,3))
Z = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(3,4))
X = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(0,1,2,3))
y = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=4)

# print (x1)
# print (x2)
# print (x3)
# print (x4)
# print (Val)

#svr
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_poly = SVR(kernel='poly', C=1e3, degree=5)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)

print(X)
print(y)
print(y_rbf)
print(y_poly)
print(X.size)
print(y.size)

# lw = 2
# # plt.scatter(X, y, color='darkorange', label='data')
# plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
# plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
# plt.xlabel('data')
# plt.ylabel('target')
# plt.title('Support Vector Regression')
# plt.legend()
# plt.show()

fig = plt.figure()

ax = Axes3D(fig) #<-- Note the difference from your original code...


# Plot the surface.
surf = ax.plot_surface(X12, X23, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(0, 1)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
#print (data[4])