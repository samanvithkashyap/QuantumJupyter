# QuantumJupyter: Interactive QML Playground

Welcome to **QuantumJupyter** — a visual, modular, and interactive open-source playground for **Quantum Machine Learning (QML)** models.  
Think of it as your **TensorBoard + Streamlit + Magic Commands** — but for **quantum circuits** ✨

> 🎯 Built for researchers, students, and open-source explorers  
> 🚀 GSSoC 2025 Project | Admin: [@silverballz](https://github.com/silverballz)

---

## 🧠 Why QuantumJupyter?

Quantum ML is powerful, but hard to visualize and debug.  
**QuantumJupyter** lets you:
- 🧱 Visualize quantum circuits and their evolution
- 📈 Track loss/fidelity of QNNs over training
- ⚖️ Compare classical vs quantum ML performance
- 🌀 Explore Bloch sphere visualizations
- 🔍 Use Jupyter magic commands for QML workflows
- 🌐 Launch a dashboard with Streamlit UI (coming soon)

---

## ✅ Current Status

### Completed
- [x] `visualizer.py`: Build and draw QNN circuits, plot Bloch spheres
- [x] `tracker.py`: Track and plot training metrics like loss/fidelity
- [x] `qdatasets.py`: Load toy datasets like Iris and XOR
- [x] `magics.py`: Jupyter magics `%qmlrun`, `%draw_qnn`, `%plot_bloch`
- [x] `__init__.py`: Package initializer
- [x] `requirements.txt`: Dependency list for install

### Up Next
- [ ] Demo notebooks (`demo_qsvm.ipynb`, `quantum_vs_classical.ipynb`)
- [ ] Streamlit dashboard (`streamlit_app/app.py`)
- [ ] CONTRIBUTING.md with guidelines
- [ ] First set of `good first issues`

---

## 📁 Project Structure

```bash
QuantumJupyter/
├── qjupyter/
│   ├── visualizer.py         # QNN circuit and Bloch rendering ✅
│   ├── tracker.py            # Live loss & metric plots ✅
│   ├── qdatasets.py          # Small quantum-ready datasets ✅
│   ├── magics.py             # Jupyter magic commands ✅
│   └── __init__.py ✅
├── notebooks/
│   ├── demo_qsvm.ipynb       # 🛠️ WIP
│   └── quantum_vs_classical.ipynb  # 🛠️ WIP
├── streamlit_app/
│   └── app.py                # 🛠️ WIP
├── LICENSE ✅
├── README.md ✅
├── CONTRIBUTING.md           # 🛠️ WIP
├── requirements.txt ✅
└── .gitignore
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/silverballz/QuantumJupyter.git
cd QuantumJupyter
pip install -r requirements.txt
```

### ▶️ Run Jupyter Demo (when ready)
```bash
jupyter notebook notebooks/demo_qsvm.ipynb
```

### 🌐 Launch Streamlit App (coming soon)
```bash
cd streamlit_app
streamlit run app.py
```

---

## 📚 Quantum Tools Used

- [PennyLane](https://pennylane.ai/)
- [Cirq](https://quantumai.google/cirq)
- [Qiskit](https://qiskit.org/) *(planned)*
- [Matplotlib](https://matplotlib.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)

---

## 🙋‍♀️ GSSoC Contributors

We are part of **GirlScript Summer of Code 2025** 🌸  
This project is beginner-friendly and has a dedicated mentor and admin team.

Join the community, explore quantum, and build with us! 🚀  
Let’s make QML accessible together.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/silverballz/QuantumJupyter/main/assets/quantum_wave.png" width="300px" alt="Quantum Jupyter Logo"/>
</p>