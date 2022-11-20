import os
import numpy as np
from PIL import Image


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

def as_row_matrix (X):
    if len (X) == 0:
        return np. array ([])
    mat = np. empty ((0 , X [0].size ), dtype =X [0]. dtype )
    for row in X:
        mat = np.vstack(( mat , np.asarray( row ).reshape(1 , -1))) # 1 x r*c 
    return mat


def NComp(eigenvalues, variance=.95):
    for i, eigen_value_cumsum in enumerate(np.cumsum(eigenvalues) / np.sum(eigenvalues)):
        if eigen_value_cumsum > variance:
            return i

def pca(X,y,num_components =0):
    [n,d] = X.shape
    if (num_components <= 0) or (num_components >n):
        num_components = n
        mu = X.mean( axis =0)
        X = X - mu
    if n>d:
        C = np.dot(X.T,X)
        [ eigenvalues , eigenvectors ] = np.linalg.eigh(C)
    else :
        C = np.dot (X,X.T)
        [ eigenvalues , eigenvectors ] = np.linalg.eigh(C)
        eigenvectors = np.dot(X.T, eigenvectors )
        for i in range (n):
            eigenvectors [:,i] = eigenvectors [:,i]/ np.linalg.norm(eigenvectors [:,i])
    idx = np.argsort (- eigenvalues )
    eigenvalues = eigenvalues [idx ]
    eigenvectors = eigenvectors [:, idx ]
    num_components = NComp(eigenvalues)
    eigenvalues = eigenvalues [0: num_components ].copy ()
    eigenvectors = eigenvectors [: ,0: num_components ].copy ()
    return [ eigenvalues , eigenvectors , mu]


def project(W,X,mu):
    return np.dot(X-mu ,W)

def distance(p,q):
    p = np.asarray(p).flatten()
    q = np.asarray (q).flatten()
    return np.sqrt (np.sum (np.power ((p-q) ,2)))

def predict (W, mu , projections, y, X):
    minDist = float("inf")
    minClass = -1
    Q = project(W, X.reshape (1 , -1) , mu)
    for i in range(len(projections)):
        dist = distance(projections[i], Q)
        if dist < minDist:
            minDist = dist
            minClass = i
    return minClass

## RUN SEMENTARA
[X,y] = read_images()

averageMat = np.reshape(as_row_matrix(X).mean(axis=0), X[0].shape)

[eigenval,eigenvec,mean] = pca(as_row_matrix(X),y)

T=[]

numb = eigenvec.shape[1]
for i in range (min(numb, 16)):
    e = eigenvec[:,i].reshape(X[0].shape )
    T.append(np.asarray(e))

projections = []
for xi in X:
    projections.append(project (eigenvec, xi.reshape(1 , -1) , mean))

image = Image.open("test.jpg")
image = image.convert ("L")
if (DEFAULT_SIZE is not None ):
    image = image.resize (DEFAULT_SIZE , Image.Resampling.LANCZOS )
test_image = np. asarray (image , dtype =np. uint8 )
predicted = predict(eigenvec, mean , projections, y, test_image)

print(y[predicted])