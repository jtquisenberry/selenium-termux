# Install Jupyter on Termux on Android

## Install Linux Packages
```
# Notice that there are no "-dev" packages. They have been merged into the
# remaining packages
apt install clang python fftw libzmq freetype libpng pkg-config

LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow

# Required for matplotlib
pkg install libjpeg-turbo
```

## Add scipy
```
# Add repository
curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh
pkg install scipy
```

## Install Python Packages
```
pip install wheel
pip install egg
pip install kiwisolver
pip install six
pip install cycler
pip install pyparsing
LDFLAGS=" -lm -lcompiler_rt" pip install numpy matplotlib pandas jupyter
```

## Run jupyter
```
jupyter notebook
```

## Run Remotely
```
# Consider setting remote password
jupyter notebook password

# Run remotely
jupyter notebook --no-mathjax --no-browser --ip 0.0.0.0 --port 8890
# The --no-mathjax improves loading over slow connections
```
