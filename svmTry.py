import time
import numpy as np 
# import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.kernel_ridge import KernelRidge
# from mpl_toolkits.mplot3d import axes3d, Axes3D
# from matplotlib import cm


train_size = 90
url = "realData4D.csv"

# Assign colum names to the dataset
colnames = ['x1', 'x2', 'x2', 'x3', 'Val']

# Read dataset
X = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(0,1,2,3))
X1 = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(0))
X2 = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(1))
X3 = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(2))
X4 = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=(3))
y = np.loadtxt('test4D.csv', dtype=float,delimiter=';',skiprows=1, usecols=4)

print(X)
y.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

kr = GridSearchCV(KernelRidge(kernel='rbf', gamma=0.1), cv=5,param_grid={"alpha": [1e0, 0.1, 1e-2, 1e-3],"gamma": np.logspace(-2, 2, 5)})

svr_rbf = GridSearchCV(SVR(kernel='rbf', C=0.7), cv=5,param_grid={"C": [0.5, 0.6, 0.7],"gamma": np.logspace(-2, 2, 5)})

svr_poly = GridSearchCV(SVR(kernel='poly', C=0.7, degree=4), cv=5,param_grid={"C": [0.5, 0.6, 0.7],"gamma": np.logspace(-2, 2, 5)})


t0 = time.time()
svr_rbf.fit(X_train, y_train)
svr_rbf_fit = time.time() - t0
print("SVR rbf complexity and bandwidth selected and model fitted in %.3f s"
      % svr_rbf_fit)

#t0 = time.time()
#svr_poly.fit(X_train, y_train)
#svr_poly_fit = time.time() - t0
#print("SVR poly complexity and bandwidth selected and model fitted in %.3f s"
#      % svr_poly_fit)

t0 = time.time()
kr.fit(X_train, y_train)
kr_fit = time.time() - t0
print("KRR complexity and bandwidth selected and model fitted in %.3f s"
      % kr_fit)

sv_rbf_ratio = svr_rbf.best_estimator_.support_.shape[0] / train_size
print("Support vector with rbf kernel ratio: %.3f" % sv_rbf_ratio)

#sv_poly_ratio = svr_poly.best_estimator_.support_.shape[0] / train_size
#print("Support vector with polynomial kernel ratio: %.3f" % sv_poly_ratio)

t0 = time.time()
y_svr_rbf = svr_rbf.predict(X_test)
svr_rbf_predict = time.time() - t0
print("SVR rbf prediction for %d inputs in %.3f s"
      % (X_test.shape[0], svr_rbf_predict))

#t0 = time.time()
#y_svr_poly = svr_poly.predict(X_test)
#svr_poly_predict = time.time() - t0
#print("SVR rbf prediction for %d inputs in %.3f s"
#      % (X_test.shape[0], svr_poly_predict))

print(svr_rbf.cv_results_)
print(svr_poly.cv_results_)



t0 = time.time()
y_kr = kr.predict(X_test)
kr_predict = time.time() - t0
print("KRR prediction for %d inputs in %.3f s"
      % (X_test.shape[0], kr_predict))




# #create model using rbf kernel
# model_rbf = svr_rbf.fit(X_train, y_train)
# #create predictions using rbf model
# predictions_rbf = model_rbf.predict(X_test)

# #create model using polynomial kernel
# model_poly = svr_poly.fit(X_train, y_train)
# #create predictions usng plynomial model
# predictions_poly= model_poly.predict(X_test)

# X_all = np.append(X,y)


# #np.savetxt('foo1.csv',np.c_[X1,X2,X3,X4,y, y_rbf, y_poly],delimiter=";",fmt='%1.10f')
# #np.savetxt("foo.csv", complete_data, delimiter=';', header=header, comments="")

# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# scores_poly = cross_val_score(model_poly, X_test, predictions_poly, cv=5)
# scores_rbf = cross_val_score(model_rbf, X_test, predictions_rbf, cv=5)
# print(scores_poly)
# print(scores_rbf)
# print(np.amin(y))
# print(np.amin(predictions_poly))
# print(np.amin(predictions_rbf))
