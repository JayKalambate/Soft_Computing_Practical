print("Practical 3(A)Performed by Jay_Kalambate")
X=[[1,1],[1,-1],[-1,1],[-1,-1]]
print("input")
for x in X:
    print(x)
Y = [1,-1,-1,-1]
print("Target = ",Y)
W = [0,0]
print("Intial weight values = ",W)
for i in range(len(X)):
    for j in range(len(W)):
        W[j]=W[j]+X[i][j]*Y[i]
        print(i,"Iteration, weights value = ",W)