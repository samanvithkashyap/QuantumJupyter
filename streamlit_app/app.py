# streamlit_app/app.py

import streamlit as st
import numpy as np
from qjupyter.visualizer import build_qnn_circuit, draw_circuit, plot_bloch_vector
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="QuantumJupyter", layout="centered")

st.title("🔮 QuantumJupyter Playground")
st.markdown("Welcome to the **interactive Streamlit version** of QuantumJupyter!")

# Sidebar options
option = st.sidebar.selectbox(
    "Choose a Module",
    ["QNN Circuit Visualizer", "Bloch Sphere Viewer"]
)

# --- QNN Circuit Visualizer ---
if option == "QNN Circuit Visualizer":
    st.header("🧱 QNN Circuit Visualizer")

    n_qubits = st.slider("Number of Qubits", 2, 4, 3)
    n_layers = st.slider("Number of Layers", 1, 3, 2)

    input_data = st.text_input("Enter input values (comma-separated)", "0.5,0.2,0.8")
    
    try:
        x = np.array([float(i) for i in input_data.split(",")])
        if len(x) != n_qubits:
            st.error("Input length must match number of qubits.")
        else:
            weights = np.random.uniform(0, np.pi, size=(n_layers, n_qubits))
            circuit = build_qnn_circuit(weights)
            st.subheader("Circuit Output:")
            st.code(circuit(x=x))

            st.subheader("Circuit Diagram:")
            diagram_str = draw_circuit(circuit)
            st.text(diagram_str)

    except Exception as e:
        st.error(f"Error: {str(e)}")


# --- Bloch Sphere Viewer ---
elif option == "Bloch Sphere Viewer":
    st.header("🌀 Bloch Sphere Viewer")

    a = st.text_input("Amplitude α (e.g., 0.707+0j)", "0.707+0j")
    b = st.text_input("Amplitude β (e.g., 0.707+0j)", "0.707+0j")

    try:
        state = np.array([complex(a), complex(b)])
        if len(state) != 2:
            st.error("State must have 2 amplitudes.")
        else:
            st.pyplot(plot_bloch_vector(state))
    except Exception as e:
        st.error(f"Invalid state vector: {e}")
