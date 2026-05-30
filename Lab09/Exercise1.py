# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:09:28 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def plotKMeans(centroids, labels):
    plt.plot(X[labels==0,0],X[labels==0,1],'r.', label='cluster 1')
    plt.plot(X[labels==1,0],X[labels==1,1],'b.', label='cluster 2')
    plt.plot(X[labels==2,0],X[labels==2,1],'g.', label='cluster 3')

    plt.plot(centroids[:,0],centroids[:,1],'mo',markersize=8, label='centroids')

    plt.legend(loc='best')
    plt.show() 
    plt.figure()
    return


def createRandomSample():
    np.random.seed(7)
    x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2))
    x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
    x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
    return np.concatenate((x1,x2,x3),axis=0)
    


def kmeans(X, centroids):
    
    #assign points to the centroids
    labels = np.zeros(len(X))
    d = np.zeros(len(centroids))
    for i in range(len(X)):
        for j in range(len(centroids)):
            d[j] = (X[i,0]-centroids[j,0])**2 + (X[i,1]-centroids[j,1])**2
            
        labels[i] = np.argmin(d)
        
    plotKMeans(centroids,labels)
    
    #reallocate centroid    
    for i in range(len(centroids)):
        centroids[i,0] = np.mean(X[labels==i, 0])
        centroids[i,1] = np.mean(X[labels==i, 1])
        
    plotKMeans(centroids,labels)

    return centroids





X = createRandomSample()
centroids = np.random.rand(3,2)
minX = np.min(X[:,0])
maxX = np.max(X[:,0])
minY = np.min(X[:,1])
maxY = np.max(X[:,1])
centroids[:,0] = minX + centroids[:,0] * ( maxX - minX)
centroids[:,1] = minY + centroids[:,1] * ( maxY - minY)

plt.plot(X[:,0],X[:,1],'k.')
plt.plot(centroids[:,0],centroids[:,1],'mo',markersize=8, label='centroids')
plt.title("Initial centroids")
plt.show()
plt.figure()



for i in range(6):
    print("***********   iteration ", i)
    centroids = kmeans(X, centroids)
    

















