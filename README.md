# npquantum 

A collection of mathematical tools for learning quantum circuits, built on `numpy`.

`npquantum` has been used in two workshops by Quantum Computing at Davis (QCaD), recorded on YouTube, with slides used for presentation linked in the description of each video:
* [QCaD-Circuits-I](https://www.youtube.com/watch?v=6TSlHTsKyrs)
* [QCaD-Circuits-II](https://www.youtube.com/watch?v=LpVAOK8rsM0)

## ⚠️⚠️ WARNING ⚠️⚠️

`npquantum` was developed mainly for __educational use ONLY__ and is not meant as a complete, let alone performant, quantum computer simulator. New features and feature-breaking additions are constantly being made.

## Contents

* `npquantum.py`
  * main library file that all other notebook files depend on. It *is* `npquantum`
* `QCaD-Circuits-I.ipynb` and `QCaD-Circuits-II ipynb`
  * notebooks used for QCaD' 2020 Spring Quarter workshops introducing quantum gates and circuits'
* `Dockerfile` and `Docker-compose.yml`
  * Launches the Docker environment to run everything in

### Development

* `bloch-sphere-tools.ipynb`
  * Development in `npquantum` utilities to piggy-back off of Qiskit's rich visualization libraries
* `dev.ipynb`
  * Miscellaneous function testing/prototyping
* `embed-matrix.ipynb`
  * Gate factory prototyping - testing the ability to generate arbitrary Control gates
* `npquantum-test.ipynb`
  * Direct library tests of gates, functions, etc.
* `Ion-Trap-Gates.ipynb`
  * Current prototyping involving the development of gates specific to Ion Trapping platforms
