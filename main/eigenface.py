import os
import numpy as np
from PIL import Image
import time
from feigen import *

IMAGE_DIR = 'training-images'
DEFAULT_SIZE = [256, 256] 

def read_images(image_path=IMAGE_DIR, default_size=DEFAULT_SIZE):
    images = []
    images_names = []
    image_dirs = [image for image in os.listdir(image_path) if not image.startswith('.')]
    for image_dir in image_dirs:
        dir_path = os.path.join(image_path, image_dir)
        image_names = [image for image in os.listdir(dir_path) if not image.startswith('.')]
        for image_name in image_names:
            image = Image.open (os.path.join(dir_path, image_name))
            image = image.convert ("L")
            if (default_size is not None ):
                image = image.resize (default_size , Image.Resampling.LANCZOS )
            images.append(np.asarray (image , dtype =np. uint8 ))
            images_names.append(image_dir)
    return [images,images_names]

def rowmatrix(X):
    if len(X) == 0:
        return np. array ([])
    mat = np. empty ((0 , X [0].size ), dtype =X [0]. dtype )
    for row in X:
        mat = np.vstack((mat,np.asarray(row).reshape(1,-1)))
    return mat


def NComp(eigenvalues, variance=.95):
    for i, eigen_value_cumsum in enumerate(np.cumsum(eigenvalues)/np.sum(eigenvalues)):
        if eigen_value_cumsum > variance:
            return i

def pca(X,y,jComp =0):
    [n,d] = X.shape
    if (jComp<=0) or (jComp>n):
        jComp = n
        m = X.mean(axis=0)
        X = X-m
    if n>d:
        C = np.dot(X.T,X)
        [eigenvalues,eigenvectors] = np.linalg.eig(C)
    else :
        C = np.dot(X,X.T)
        [eigenvalues,eigenvectors] = np.linalg.eig(C)
        eigenvectors = np.dot(X.T,eigenvectors)
        for i in range (n):
            eigenvectors [:,i] = eigenvectors [:,i]/ np.linalg.norm(eigenvectors [:,i])
    idx = np.argsort(- eigenvalues )
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors [:,idx]
    jComp = NComp(eigenvalues)
    eigenvalues = eigenvalues [0:jComp].copy ()
    eigenvectors = eigenvectors [:,0:jComp].copy ()
    return [eigenvalues,eigenvectors,m]


def project(W,X,m):
    return np.dot(X-m ,W)

def eucDist(p,q):
    p = np.asarray(p).flatten()
    q = np.asarray (q).flatten()
    return np.sqrt(np.sum(np.power((p-q),2)))

def predict(W,m,projections,y,X):
    minDist = float("inf")
    minClass = -1
    Q = project(W,X.reshape(1,-1),m)
    for i in range(len(projections)):
        dist = eucDist(projections[i],Q)
        if dist < minDist:
            minDist = dist
            minClass = i

    if minDist < 0.05 :
        return minClass
    else:
        return -1

## RUN SEMENTARA
