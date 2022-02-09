from pdb import line_prefix
from xxlimited import Xxo
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as metrics 
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pandas as pd

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

def linear_regression(path,x,y):
    data = np.loadtxt(path)  # on lit les données dans un fichier txt
    X_data = data[:,x].reshape(len(data),1)  # première colonne (sans reshape, X_data serait un vecteur ligne)
    Y_data = data[:,y].reshape(len(data),1)  # deuxième colonne

    axismax = int(max(X_data))
    axismin = int(min(X_data))
    ordmax = int(max(Y_data))
    ordmin = int(min(Y_data))

    lr = lm.LinearRegression()
    lr.fit(X_data, Y_data)  
    X = np.linspace(axismin,axismax,num=30).reshape(30,1)
    Y_pred_lr = lr.predict(X)  

    plt.figure(figsize=(10,6))
    plt.plot(X_data, Y_data,'o')
    plt.plot(X, Y_pred_lr, '-g')
    plt.xlim(axismin, axismax)
    plt.ylim(ordmin, ordmax)
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.grid()
    plt.title('observations et régression linéaire')
    plt.legend(["observations","droite de régression"])
    plt.show()

def linearreg_csv(path,x,y):
    data = pd.read_csv(path)
    Xcol = list(data.columns)[x]
    Ycol = list(data.columns)[y]
    X_data = data[Xcol]
    Y_data = data[Ycol]

    axismax = int(max(X_data.values.tolist()))
    axismin = int(min(X_data.values.tolist()))
    ordmax = int(max(Y_data.values.tolist()))
    ordmin = int(min(Y_data.values.tolist()))

    X_data = data[Xcol].array.reshape(-1,1)


    lr = lm.LinearRegression()
    lr.fit(X_data, Y_data)  
    X = np.linspace(axismin,axismax,num=30).reshape(30,1)
    Y_pred_lr = lr.predict(X_data)  

    plt.figure(figsize=(10,6))
    plt.plot(X_data, Y_data,'o')
    plt.plot(X_data, Y_pred_lr, '-g')
    plt.xlim(axismin, axismax)
    plt.ylim(ordmin, ordmax)
    plt.xlabel("X : " + list(data.columns)[x])
    plt.ylabel("Y: " + list(data.columns)[y])
    plt.grid()
    plt.title('observations et régression linéaire')
    plt.legend(["observations","droite de régression"])
    plt.show()



def polynomial_regression(path,n,x,y):
    data = np.loadtxt(path)  # on lit les données dans un fichier txt
    X_data = data[:,x].reshape(len(data),1)  # première colonne (sans reshape, X_data serait un vecteur ligne)
    Y_data = data[:,y].reshape(len(data),1)  # deuxième colonne

    axismax = int(max(X_data))+10
    axismin = int(min(X_data))-10
    ordmax = int(max(Y_data))+10
    ordmin = int(min(Y_data))-10

    polynome = PolynomialFeatures(degree=n,include_bias=False)
    X_data_poly = polynome.fit_transform(X_data)

    lrp = lm.LinearRegression()
    lrp.fit(X_data_poly,Y_data)
    lrp.intercept_
    lrp.coef_

    X = np.linspace(axismin,axismax,num=30).reshape(30,1)
    Xpoly=polynome.fit_transform(X)
    Y_pred_lr=lrp.predict(Xpoly)  # prédiction du modèle sur les valeurs X définies plus haut, pour le graphique

    legend = "modèle de degré %d"%n

    plt.figure(figsize=(10,6))
    plt.plot(X_data, Y_data,'o')
    plt.plot(X, Y_pred_lr, '-g')
    plt.xlim(axismin, axismax)
    plt.ylim(ordmin, ordmax)
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.grid()
    plt.title('régression polynômiale')
    plt.legend(["observations",legend])
    plt.show()

def polynomial_reg_csv(path,n,x,y):
    data = pd.read_csv(path)
    Xcol = list(data.columns)[x]
    Ycol = list(data.columns)[y]
    X_data = data[Xcol]
    Y_data = data[Ycol]

    axismax = int(max(X_data.values.tolist()))
    axismin = int(min(X_data.values.tolist()))
    ordmax = int(max(Y_data.values.tolist()))
    ordmin = int(min(Y_data.values.tolist()))

    X_data = data[Xcol].array.reshape(-1,1)
    polynome = PolynomialFeatures(degree=n,include_bias=False)
    X_data_poly = polynome.fit_transform(X_data)

    lrp = lm.LinearRegression()
    lrp.fit(X_data_poly,Y_data)
    lrp.intercept_
    lrp.coef_

    X = np.linspace(axismin,axismax,num=30).reshape(30,1)
    Xpoly=polynome.fit_transform(X)
    Y_pred_lr=lrp.predict(Xpoly)  # prédiction du modèle sur les valeurs X définies plus haut, pour le graphique

    legend = "modèle de degré %d"%n

    plt.figure(figsize=(10,6))
    plt.plot(X_data, Y_data,'o')
    plt.plot(X, Y_pred_lr, '-g')
    plt.xlim(axismin, axismax)
    plt.ylim(ordmin, ordmax)
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.grid()
    plt.title('régression polynômiale')
    plt.legend(["observations",legend])
    plt.show()
