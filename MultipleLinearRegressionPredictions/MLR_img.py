import sys
import numpy as np

def MLR(F: int, N: int)-> str:
    """
    -Args:
    F: number of features
    N: number of observations
    -Returns:
    The predictions of MLR model in a string-specific format
    Y = B0 + B1X1 + B2X2 + ... BFXF
    """
    X = []
    Y = []
    test_data = []
    lines = sys.stdin.readlines()
    reading_test = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not reading_test and len(line.split()) == 2:
            continue # Ignore first line
        # Detecting the beginning of test data    
        if len(line.split()) == 1:
            reading_test = True
            continue
        # If test data are being read
        if reading_test:
            test_data.append([float(x) for x in line.split()])
        else:
            # Training data
            Y.append(line.split()[-1])
            X.append(line.split()[:-1])
        
    Y = [float(y) for y in Y]
    X = [[float(x) for x in row] for row in X]
  
    
    # Converting lists -> arrays
    X = np.array(X) # shape=(N, F)
    Y = np.array(Y) # shape=(N,)

    
    # Adding bias column (B0 intercept)
    X_with_bias = np.column_stack([np.ones(X.shape[0]), X]) # shape=(N, F+1)
    
    # Building Normal equation: \theta = (X^T*X)^(-1)* X^T*Y
    # 1. X^T
    X_transpose = X_with_bias.T # shape=(F+1, N)
    
    # 2. X^T*X
    XTX = np.dot(X_transpose, X_with_bias) # shape=(F+1, F+1) -> feature matrix
    
    # 3. X^T*Y
    XTY = np.dot(X_transpose, Y) # shape=(F+1,)
    
    # Solving the system (X^T * X) * \theta = X^T * Y -> \theta = (X^T * X)^(-1) * X^T * Y using LU decomposition
    coefficients = np.linalg.solve(XTX, XTY) # shape=(F+1,)

    
    # Prediction for test data
    test_data = np.array(test_data) # shape=(num_test_samples, F)

    
    for test_features in test_data:
        # Adding bias at the beginning -> 1.0 
        features_with_bias = np.array([1.0] + test_features.tolist())
        # Prediction: Y = B0 + B1*X1 + B2*X2 + ... BF*XF
        predictions = np.dot(coefficients, features_with_bias)
        print(f'{predictions:.2f}')
    
    
first_line = input().strip().split()
F = int(first_line[0])
N = int(first_line[1])
MLR(F, N)
