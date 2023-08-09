FROM ubuntu:22.04


# Create temporary directory
RUN mkdir neo && cd neo

# Update packages
RUN apt update && apt upgrade -y

# Install commands
RUN apt install wget python3 pip clinfo -y

# Download all *.deb packages
RUN wget https://github.com/intel/intel-graphics-compiler/releases/download/igc-1.0.14062.11/intel-igc-core_1.0.14062.11_amd64.deb \
        https://github.com/intel/intel-graphics-compiler/releases/download/igc-1.0.14062.11/intel-igc-opencl_1.0.14062.11_amd64.deb \
        https://github.com/intel/compute-runtime/releases/download/23.22.26516.18/intel-level-zero-gpu-dbgsym_1.3.26516.18_amd64.ddeb \
        https://github.com/intel/compute-runtime/releases/download/23.22.26516.18/intel-level-zero-gpu_1.3.26516.18_amd64.deb \
        https://github.com/intel/compute-runtime/releases/download/23.22.26516.18/intel-opencl-icd-dbgsym_23.22.26516.18_amd64.ddeb \
        https://github.com/intel/compute-runtime/releases/download/23.22.26516.18/intel-opencl-icd_23.22.26516.18_amd64.deb \
        https://github.com/intel/compute-runtime/releases/download/23.22.26516.18/libigdgmm12_22.3.0_amd64.deb

# Verify sha256 sums for packages
RUN wget https://github.com/intel/compute-runtime/releases/download/23.22.26516.18/ww22.sum && \
    sha256sum -c ww22.sum

# Install required dependencies
RUN apt install -y \
    ocl-icd-libopencl1 \
    ocl-icd-opencl-dev \
    opencl-headers

# Install all packages as root
RUN dpkg -i *.deb

# Install python requirements
RUN pip install pyopencl

WORKDIR /app

ENTRYPOINT bash