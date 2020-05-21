import numpy as np

def ketgen(vals):
    array = []
    for c in vals:
        if c == '0':
            array.append([0])
        elif c == '1':
            array.append([1])
        else:
            print(f"INVALID VALUE:{c}")
            return
    return np.matrix(array)

def bragen(vals):
    return ketgen(vals).H
        
        
ket0 = np.matrix([[1],[0]])
bra0 = ket0.H
ket1 = np.matrix([[0],[1]])
bra1 = ket1.H
ketplus = 1/np.sqrt(2)*(ket0 + ket1)
ketminus = 1/np.sqrt(2)*(ket0 - ket1)
ket00 = np.kron(ket0,ket0)
ket01 = np.kron(ket0,ket1)
ket10 = np.kron(ket1,ket0)
ket11 = np.kron(ket1,ket1)

X = ket0 * bra1 + ket1 * bra0
Y = (-1j * ket0 * bra1) + (1j * ket1 * bra0)
Z = ket0 * bra0 - ket1 * bra1
H = 1/np.sqrt(2) * np.matrix([[1,1], [1,-1]])
I = np.matrix(np.eye(2)) # I gate

def R_phi(phi):
    return np.matrix([[1,0], [0, (np.e)**(1j*phi)]])

S = R_phi(np.pi/2)
S_dagger = R_phi(-np.pi/2)

T = R_phi(np.pi/4)
T_dagger = R_phi(-np.pi/4)

def U3(theta, phi, lamb):
    return np.matrix([[np.cos(theta/2),                -np.e**(1j*lamb)*np.sin(theta/2)], 
                      [np.e**(1j*phi)*np.sin(theta/2), np.e**(1j*lamb+1j*phi)*np.cos(theta/2)]])

# Second qubit is control, first qubit is target
## swap amplitudes of |01> and |11>
CNOT21 = np.matrix([[1,0,0,0], [0,0,0,1], [0,0,1,0], [0,1,0,0]])

# First qubit is control, second qubit is target
## swap amplitudes of |
CNOT12 = np.matrix([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])

def to_plot(ket):
    return np.squeeze(np.asarray(ket))