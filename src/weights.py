def weight(eigvec, diff): # eigvec : eigenvector
    sum = 0
    for i in range (len(eigvec)):
        sum = sum + (eigvec[i][0])**2
    scal = sum**0.5

    norm = [0 for i in range(len(eigvec))]
    for i in range(len(eigvec)):
        norm[i] = eigvec[i][0]/scal

    # norm x diff
    weight = 0
    for i in range(len(norm)):
        weight = weight + norm[i]*diff[i][0]

    return weight