# selenium-termux

## Uninstall Ubuntu
```
wsl --list
wsl --unregister Ubuntu
```

## Install Ubuntu

```
Go to Windows Store and install or launch Ubuntu. 
```

## Update apt Repositories

```
sudo apt-get update
sudo apt-get upgrade
# This repository contains Python 3.7
sudo add-apt-repository ppa:deadsnakes/ppa
```

## Install Python
```
sudo apt-get install python3.7
sudo apt-get install python3.7-venv
sudo apt install python3-pip
```

## Create venv and Add Packages
```
cd /mnt/e/linux_venvs
sudo python3.7 -m venv venv001
cd bin
source activate
sudo ./python -m pip install --upgrade pip
sudo ./pip install selenium
```

## Check that Packages were Installed to venv
```
python
import os
os.getcwd()
quit()
```

## Work with Scraper
```
cd /mnt/e/linux_git/selenium-termux
cd daily_logins
```


```
(venv001) jquisenberry@jqhome03:/mnt/e/linux_git/selenium-termux/daily_logins$ python app3.py
XXXXXXXX
HEADLESS /mnt/e/linux_git/selenium-termux/daily_logins/bin2/headless-chromium
CHROMEDRIVER /mnt/e/linux_git/selenium-termux/daily_logins/bin2/chromedriver
app3.py:18: DeprecationWarning: use options instead of chrome_options
  driver = webdriver.Chrome(executable_path='./bin2/chromedriver',chrome_options=options)
Traceback (most recent call last):
  File "app3.py", line 35, in <module>
    hello()
  File "app3.py", line 18, in hello
    driver = webdriver.Chrome(executable_path='./bin2/chromedriver',chrome_options=options)
  File "/mnt/e/linux_venvs/venv001/lib/python3.7/site-packages/selenium/webdriver/chrome/webdriver.py", line 73, in __init__
    self.service.start()
  File "/mnt/e/linux_venvs/venv001/lib/python3.7/site-packages/selenium/webdriver/common/service.py", line 98, in start
    self.assert_process_still_running()
  File "/mnt/e/linux_venvs/venv001/lib/python3.7/site-packages/selenium/webdriver/common/service.py", line 111, in assert_process_still_running
    % (self.path, return_code)
selenium.common.exceptions.WebDriverException: Message: Service ./bin2/chromedriver unexpectedly exited. Status code was: 127
```

```
./chromedriver
./chromedriver: error while loading shared libraries: libnss3.so: cannot open shared object file: No such file or directory
```

## Dependencies

```
sudo apt install libnss3
```



## Run

```

python app3.py

```

## Alternative
```
sudo apt install chromium-chromedriver
```


## ???
```
sudo python3
subprocess.Popen('apt-get install -y libnss3', shell=True, stdin=None, stdout=None, stderr=None)
```

# Trying
```
apt install libglib2.0-bin
apt install chromium
```