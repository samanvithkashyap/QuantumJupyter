# qjupyter/visualizer.py

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def build_qnn_circuit(weights):
    """
    Build a simple variational QNN circuit using PennyLane.
    
    Args:
        weights (np.ndarray): A 2D array of shape (n_layers, n_qubits)
    
    Returns:
        qml.QNode: Quantum node (circuit) ready to be run or visualized
    """
    n_qubits = weights.shape[1]
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def circuit(x=None):
        for i in range(n_qubits):
            qml.RY(np.pi * x[i], wires=i)
        
        for layer in weights:
            for i in range(n_qubits):
                qml.RX(layer[i], wires=i)
            for i in range(n_qubits - 1):
                qml.CZ(wires=[i, i + 1])
        
        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

    return circuit


def draw_circuit(circuit):
    """
    Print the textual representation of the QNode.
    
    Args:
        circuit (qml.QNode): PennyLane QNode to visualize
    """
    print(qml.draw(circuit)(x=np.ones(circuit.device.num_wires)))


def plot_bloch_vector(state):
    """
    Plot Bloch sphere representation for a single-qubit statevector.
    
    Args:
        state (np.ndarray): 2-element complex state vector
    """
    # Calculate Bloch vector components
    bloch_x = 2 * (state[0].conj() * state[1]).real
    bloch_y = 2 * (state[0].conj() * state[1]).imag
    bloch_z = abs(state[0])**2 - abs(state[1])**2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Sphere
    u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.1)

    # Vector
    ax.quiver(0, 0, 0, bloch_x, bloch_y, bloch_z, color='red', linewidth=2)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_title("Bloch Sphere")
    plt.show()
