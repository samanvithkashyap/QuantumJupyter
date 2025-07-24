# qjupyter/magics.py

from IPython.core.magic import register_line_magic
from qjupyter.visualizer import build_qnn_circuit, draw_circuit, plot_bloch_vector
import numpy as np


@register_line_magic
def qmlrun(line):
    """
    Run a sample quantum circuit with given input.
    Usage: %qmlrun 1.0 0.5
    """
    try:
        x = np.array([float(i) for i in line.strip().split()])
        weights = np.random.uniform(0, np.pi, size=(2, len(x)))
        circuit = build_qnn_circuit(weights)
        output = circuit(x=x)
        print("Circuit Output:", output)
    except Exception as e:
        print("[qmlrun error]:", str(e))


@register_line_magic
def draw_qnn(line):
    """
    Draw a quantum circuit.
    Usage: %draw_qnn
    """
    try:
        weights = np.random.uniform(0, np.pi, size=(2, 3))
        circuit = build_qnn_circuit(weights)
        draw_circuit(circuit)
    except Exception as e:
        print("[draw_qnn error]:", str(e))


@register_line_magic
def plot_bloch(line):
    """
    Plot Bloch sphere of a 1-qubit state.
    Usage: %plot_bloch 0.707+0j 0.707+0j
    """
    try:
        tokens = line.strip().split()
        state = np.array([complex(tok) for tok in tokens])
        if len(state) != 2:
            raise ValueError("Expected 2 complex amplitudes.")
        plot_bloch_vector(state)
    except Exception as e:
        print("[plot_bloch error]:", str(e))
