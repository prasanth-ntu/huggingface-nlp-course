Source: https://huggingface.co/learn/nlp-course/chapter0/1?fw=pt

# Introduction
We can either use google colab or Python virtual environment
## Using a Python virtual environment

**Install Transformers library**

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