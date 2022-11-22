import os
import numpy as np
from PIL import Image

DEFAULT_SIZE = [256, 256] 

def read_images(image_path, default_size=DEFAULT_SIZE):
    images = []
    img_nm = []
    img_dir = [image for image in os.listdir(image_path) if not image.startswith('.')]
    for image_dir in img_dir:
        dir_path = os.path.join(image_path, image_dir)
        image_names = [image for image in os.listdir(dir_path) if not image.startswith('.')]
        for image_name in image_names:
            image = Image.open(os.path.join(dir_path, image_name))
            image = image.convert ("L")
            if (default_size is not None ):
                image = image.resize (default_size,Image.Resampling.LANCZOS)
            images.append(np.asarray (image,dtype =np.uint8))
            img_nm.append(image_dir)
    return [images,img_nm]

def rowmatrix(X):
    if len(X)==0:
        return np. array ([])
    mat = np.empty((0,X[0].size),dtype=X[0].dtype)
    for row in X:
        mat = np.vstack((mat,np.asarray(row).reshape(1,-1)))
    return mat

def NComp(C, variance=.95):
    [eigvals,eigvecs] = np.linalg.eig(C)
    for i, eigvalcs in enumerate(np.cumsum(eigvals)/np.sum(eigvals)):
        if eigvalcs > variance:
            return i
def eigenvecs(A):
    N = len(A)
    Q = np.random.rand(N,N)
    Q,_ = np.linalg.qr(Q)

    for i in range(15):
        QR = np.matmul(A,Q)
        Q,_ = np.linalg.qr(QR)
    
    return [Q]

def pca(X,y,jComp =0):
    [n,d] = X.shape
    if (jComp<=0) or (jComp>n):
        jComp = n
        m = X.mean(axis=0)
        X = X-m
    if n>d:
        C = np.dot(X.T,X)
        [eigvecs] = eigenvecs(C)
    else :
        C = np.dot(X,X.T)
        [eigvecs] = eigenvecs(C)
        eigvecs = np.dot(X.T,eigvecs)
        for i in range (n):
            eigvecs[:,i]=eigvecs [:,i]/np.linalg.norm(eigvecs[:,i])
    jComp = NComp(C)
    eigvecs = eigvecs [:,0:jComp].copy ()
    return [eigvecs,m]

def project(Mat,X,m):
    return np.dot(X-m ,Mat)

def eucDist(p,q):
    p = np.asarray(p).flatten()
    q = np.asarray(q).flatten()
    return np.sqrt(np.sum(np.power((p-q),2)))

def predict(Mat,m,projections,y,V,X):
    minDist = float("inf")
    minClass = -1
    Q = project(Mat,V.reshape(1,-1),m)
    for i in range(len(projections)):
        dist = eucDist(projections[i],Q)
        if dist < minDist:
            minDist = dist
            minClass = i

    th = threshold(projections)

    if minDist < th:
        return minClass
    else:
        return -1

def threshold(projections) :
    maxDist = -1
    for i in range(len(projections)):
        for j in range(len(projections)):
            dist = eucDist(projections[i],projections[j])
            if (dist > maxDist and dist != 0):
                maxDist = dist
    return (maxDist/2)

