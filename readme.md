#Detect linux distribution
Simple **python** 3 module/api to detect **linux distribution**.

##Table Of contents
* Install On Linux
* Example
* More
    * Install from source/git
    * Step By Step example

##Install On Linux
~~~bash
sudo pip install detect_linux_distro
~~~
&nbsp;&nbsp;&nbsp;&nbsp;or
~~~bash
sudo pip3 install detect_linux_distro
~~~

##Example  
~~~python
from detect_linux_distro.dld import dld
my_linux_name = dld()
my_linux_name.detect()

my_linux_name.print_all_result()

#my_linux_name.get_distro_id()
#my_linux_name.print_all_result()
~~~

##More
###Install from source/git
~~~sh
git clone "https://github.com/mlibre/detect_linux_distro.git"
cd detect_linux_distro/
sudo python setup.py install
~~~

###Step by step example
1. open terminal
2. create a file like test.py on your linux
~~~bash
    touch test.py
~~~
&nbsp;&nbsp;&nbsp;&nbsp;3. copy and past this code in test.py
~~~python
    from detect_linux_distro.dld import dld
    my_linux_name = dld()
    my_linux_name.detect()
    
    my_linux_name.print_all_result()
    
    #my_linux_name.get_distro_id()
    #my_linux_name.print_all_result()
~~~
&nbsp;&nbsp;&nbsp;&nbsp;4. run code
~~~python
    python3 test.py
~~~
&nbsp;&nbsp;&nbsp;&nbsp;or
~~~python
    python test.py
~~~
##It's tested on these distributions:
* arch

>note: probably it's work on all distribution, but i don't test.