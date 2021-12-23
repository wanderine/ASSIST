conda create --prefix /proj/assist/users/x_anekl/MITPGAN3DCUDA11_env python=3.9

# Get latest cuda toolkit
conda install cudatoolkit

# Get latest tensorflow
pip install tensorflow-gpu

# Download CUDNN from Nvidia developer
wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.2.1.32/11.3_06072021/cudnn-11.3-linux-x64-v8.2.1.32.tgz

tar -xf cudnn-11.3-linux-x64-v8.2.1.32.tar 

# Copy .so files to anaconda environment
cp cuda/lib64/* /proj/assist/users/x_anekl/MITPGAN3DCUDA11_env/lib/

conda install -c conda-forge nibabel

conda install pillow



