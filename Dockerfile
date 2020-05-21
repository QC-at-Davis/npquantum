FROM debian:buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev python3-setuptools gcc\
    libblas-dev liblapack-dev \
    && pip3 install --upgrade pip \
    && pip install wheel\ 
    jupyterlab \
    qiskit \
    cirq \
    strawberryfields \
    minorminer dwave-ocean-sdk \
    pytket pytket-qiskit pytket-cirq pytket-pyquil pytket-projectq pytket-aqt pytket-honeywell pytket-pyzx

# install curl bzip2 FIRST
# WIP Rigetti
## curl -O http://downloads.rigetti.com/qcs-sdk/forest-sdk-2.20.0-linux-deb.tar.bz2
## tar -jxvf forest-sdk-2.20.0-linux-deb.tar.bz2 && rm forest-sdk-2.20.0-linux-deb.tar.bz2
##cd forest-sdk-2.20.0-linux-deb 

