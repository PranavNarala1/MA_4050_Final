import numpy as np

# And exponential equation of the form a*exp(bt) + c*exp(dt) + ... + y*exp(zt)
class Equation:
    def __init__(self, constants, exponents):
        self.constants = constants
        self.exponents = exponents
    
    def __call__(self, t):
        sum = 0

        for i in range(len(self.constants)):
            sum += self.constants[i] * np.exp(self.exponents[i] * t)
        
        return sum

# An exponential of the form ae^bx
class Exp:
    def __init__(self, constant, exponent):
        self.constant = constant
        self.exponent = exponent
    
    def __call__(self, t):
        return self.constant * np.exp(self.exponent * t)

# A sine function of the form a*sin(bx)
class Sin:
    def __init__(self, constant, inside):
        self.constant = constant
        self.inside = inside
    
    def __call__(self, t):
        return self.constant * np.sin(self.inside * t)

# A cosine function of the form a*cos(bx)
class Cos:
    def __init__(self, constant, inside):
        self.constant = constant
        self.inside = inside
    
    def __call__(self, t):
        return self.constant * np.cos(self.inside * t)

# Generate all functions to solve the system
def genLambdas(filename="coeffmat.csv"):
    # Read the matrix in
    mat = np.genfromtxt(filename, delimiter=" ")

    print(mat.dtype)
    
    # Calculate eigenvalues and eigenvectors
    eig_val, eig_vec = np.linalg.eig(mat)

    print(eig_val[0])
    print(eig_vec[0])

    # Init initial conditions
    init = np.zeros((len(eig_val),1))
    init[0][0] = 1
    
    # Inverse of the eigen vector matrix
    inv_eig_vec = np.linalg.inv(eig_vec)

    # Integration constants to fit inital conditions
    int_consts = np.matmul(inv_eig_vec, init)

    # A list of equations
    equs = []

    # Generate and print all equations
    for i in range(len(eig_val)):
        # Init term list
        #terms = []
        const_terms = []
        exp_terms = []

        # Generate each term and append
        for j in range(len(eig_val)):
            const_terms.append(int_consts[j][0] * eig_vec[i][j])
            if abs(eig_val[j]) > 1e-10:
                #terms.append(f"({int_consts[j][0]})({eig_vec[i][j]})e^{{{eig_val[j]}t}}")
                exp_terms.append(eig_val[j])
            else:
                #terms.append(f"({int_consts[j][0]})({eig_vec[i][j]})")
                exp_terms.append(0)

        # Print the equation
        #print(f"Q_{i}(t)=" + " + ".join(terms))

        equs.append(Equation(const_terms, exp_terms))
    
    return equs

if __name__ == "__main__":
    equs = genLambdas()
    #print(equs[0](0))