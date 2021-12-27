# Create empty environment with Python 3.9
conda create --prefix /proj/assist/users/x_anekl/MITPGAN3DCUDA11_env python=3.9

# Get latest cuda toolkit
conda install cudatoolkit

# Get latest tensorflow
pip install tensorflow-gpu

# Download CUDNN from Nvidia developer (you need to register as Nvidia developer, and download from their site)
wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.2.1.32/11.3_06072021/cudnn-11.3-linux-x64-v8.2.1.32.tgz

# Unpack CUDNN
tar -xf cudnn-11.3-linux-x64-v8.2.1.32.tar 

# Copy .so files to the created anaconda environment
cp cuda/lib64/* /proj/assist/users/x_anekl/MITPGAN3DCUDA11_env/lib/

# Install additional packages
conda install -c conda-forge nibabel
conda install pillow

# Set LD_LIBRARY_PATH when using the environment
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/proj/assist/users/x_anekl/MITPGAN3DCUDA11_env/lib




