Source: https://huggingface.co/learn/nlp-course/chapter0/1?fw=pt

# Introduction
We can either use google colab or Python virtual environment

## Using a Python virtual environment
```
conda conda create --name hf_nlp_py3_10 python=3.10
conda activate hf_nlp_py3_10
```

## Install Transformers library

For light version
```
pip install transformers
```

Development version (with required dependencies)
```
pip install "transformers[sentencepiece]"
```

**Check python version**
```
python --version
```

**Testing the installation**
```
import transformers
```
```
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
```
The warning message above indicates that none of the deep learning frameworks (PyTorch, TensorFlow >= 2.0, or Flax) required by the transformers library have been found. To use the models provided by transformers, you need to install at least one of these frameworks.

## Installing PyTorch with CUDA Support
Visit the PyTorch Get Started page and select the appropriate options for your system. For example, if you have CUDA 12.1 installed, you can use the following command to install PyTorch with CUDA 12.1 support:
```
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
```
Replace cu113 with the appropriate version for your CUDA installation (e.g., cu121 for CUDA 12.1).

**Verify the installation**
```
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("Number of GPUs:", torch.cuda.device_count())
print("GPU Name:", torch.cuda.get_device_name(0))
```
```
PyTorch version: 2.4.0+cu121
CUDA available: True
CUDA version: 12.1
Number of GPUs: 2
GPU Name: NVIDIA A100-SXM4-80GB
```

## Additional helpers
Register this current conda env as a Jupyter Kernel
```
python -m ipykernel install --user --name conda_hf_nlp_py3_10 --display-name "conda_hf_nlp_py3_10"
```

Install ipywidgets to resolve the IProgress warning
```
pip install ipywidgets
```



