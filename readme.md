#Detect linux distribution
Simple **python** 3 module/api to detect **linux distribution**.

##sections
* Install On Linux
* Example
* More
    * Install from source/git
    * Step by step example

#please wait docuemnt under construnction wait a few hours
##Install On Linux  
```sh
sudo pip3 install detect_linux_distro
```

##Example  
```sh
d = detect_linux_distro()
d.detect()
print(d.get_distro_name())
print(d.get_distro_id())
```

##More
###Install from source/git
```sh
git clone "https://github.com/mlibre/detect_linux_distro.git"
cd
```
###Step by step example
    0 - open terminal
    1 - create a file like test.py on your linux.
        touch test.py

    2 - copy and past this code on test.py:
        d = detect_linux_distro()
        d.detect()
        print(d.get_distro_name())
        print(d.get_distro_id())
       
    3 - run code:
        python3 test.py

    4 - good luck.

##It's tested on this distribution:
* arch

>note: probably it's work on all distribution, but i don't test.