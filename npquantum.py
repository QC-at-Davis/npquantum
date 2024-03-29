import numpy as np

# |0>
ket0 = np.array([[1],[0]])
# <0|
bra0 = ket0.conjugate().T
# |1>
ket1 = np.array([[0],[1]])
# <1|
bra1 = ket1.conjugate().T
# |+>
ketplus = 1/np.sqrt(2)*(ket0 + ket1)
# <-|
ketminus = 1/np.sqrt(2)*(ket0 - ket1)
# |00>
ket00 = np.kron(ket0,ket0)
# |01>
ket01 = np.kron(ket0,ket1)
# |10>
ket10 = np.kron(ket1,ket0)
# |11>
ket11 = np.kron(ket1,ket1)

## Generate a ket given the theta and phi angles usually used for Bloch Sphere representation
# |psi> = cos(theta/2)|0> + e^(i*phi)*sin(theta/2)|1>
# 0 <= theta <= pi
# 0 <= phi <= 2*pi
def ket_from_angles(theta, phi):
    ket0_coeff = np.cos(theta/2)
    ket1_coeff = (np.e**(1j*phi))*np.sin(theta/2)
    return  ket0_coeff * ket0 + ket1_coeff * ket1

## Given a string of 0's and 1's, create a ket
def bin_ket_gen(vals):
    array = []
    for c in vals:
        if c == '0':
            array.append([0])
        elif c == '1':
            array.append([1])
        else:
            print(f"INVALID VALUE:{c}")
            return
    return np.array(array)

## given a string of 0's and 1's, create a bra
def bin_bra_gen(vals):
    return ketgen(vals).conjugate().T

### Single Qubit Gates
X = ket0 * bra1 + ket1 * bra0
Y = (-1j * ket0 * bra1) + (1j * ket1 * bra0)
Z = ket0 * bra0 - ket1 * bra1
H = 1/np.sqrt(2) * np.array([[1,1], [1,-1]])
I = np.identity(2)

# Rotation phi around Z-axis
# R_phi |0> = |0>
# R_phi |1> = e^(i*phi) |1>
def R_phi(phi):
    return np.array([[1,0], [0, (np.e)**(1j*phi)]])

# Sqrt(Z) gates, phi = pi/2, quarter rotations around bloch_sphere
S = R_phi(np.pi/2)
S_dagger = R_phi(-np.pi/2)

# pi/4 rotation
T = R_phi(np.pi/4)
T_dagger = R_phi(-np.pi/4)

def Rx(theta):
    return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)],
                      [-1j*np.sin(theta/2), np.cos(theta/2)]])

def Ry(theta):
    return np.array([[np.cos(theta/2), -np.sin(theta/2)],
                      [np.sin(theta/2), np.cos(theta/2)]])

def Rz(theta):
    return np.array([[np.e**(-1j*(theta/2)), 0],
                      [0, np.e**(1j*(theta/2))]])

## IBM Q Physical gates, all gates get compiled down to U1, U2, U3
# most universal U gate
def U3(theta, phi, lamb):
    return np.array([[np.cos(theta/2),                -np.e**(1j*lamb)*np.sin(theta/2)], 
                      [np.e**(1j*phi)*np.sin(theta/2), np.e**(1j*lamb+1j*phi)*np.cos(theta/2)]])

def U2(phi, lamb):
    return U3(np.pi/2, phi, lamb)

# equivalent to R-phi
def U1(lamb):
    return U3(0, 0, lamb)

# CX gate with two versions:
# CXtc - the first qubit is the target, the second is the control
# CXct - the second qubit is the target, the first is the control
CXtc = np.array([[1,0,0,0],
                  [0,0,0,1],
                  [0,0,1,0],
                  [0,1,0,0]])

CXct = np.array([[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,1],
                  [0,0,1,0]])

# SWAP gate for two qubits
SWAP = np.array([[1,0,0,0],
                  [0,0,1,0],
                  [0,1,0,0],
                  [0,0,0,1]])

# Controlled-Controlled NOT (CCX) gate
# This REQUIRES the first and second qubits are the control,
# while the third qubit is the target
CCX = np.identity(8)
CCX[[6,7]] = CCX[[7,6]]

def to_qiskit_plot(ket):
    return np.squeeze(np.asarray(ket))

class IonTrap:
    Rx = Rx 
    Ry = Ry
    Rz = Rz
    
    @staticmethod
    def R(theta, phi):
        return np.matrix([[np.cos(theta/2),                    -1j*np.e**(-1j*phi)*np.sin(theta/2)],
                          [-1j*np.e**(1j*phi)*np.sin(theta/2), np.cos(theta/2)]])
    

