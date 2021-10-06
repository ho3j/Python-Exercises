"""
Python Language 
Rewriting and summarizing by Hossein Jalili
1400-6-14
---------------------------------------------------------------------------------------------------
1-Python Programming Language :

Below are some facts about Python Programming Language:
    Python is currently the most widely used multi-purpose, high-level programming language.
    Python allows programming in Object-Oriented and Procedural paradigms.
    Python programs generally are smaller than other programming languages like Java. Programmers have to type relatively less and indentation requirement of the language, makes them readable all the time.
    Python language is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.
        The biggest strength of Python is huge collection of standard library which can be used for the following:
        Machine Learning
        GUI Applications (like Kivy, Tkinter, PyQt etc. )
        Web frameworks like Django (used by YouTube, Instagram, Dropbox)
        Image processing (like OpenCV, Pillow)
        Web scraping (like Scrapy, BeautifulSoup, Selenium)
        Test frameworks
        Multimedia
        Scientific computing
        Text processing and many more..
---------------------------------------------------------------------------------------------------
2-Python Language Introduction :

Python is a widely used general-purpose, high level programming language.
It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.
It was designed with an emphasis on code readability,
and its syntax allows programmers to express their concepts in fewer lines of code.

Python is a programming language that lets you work quickly and integrate systems more efficiently.

There are two major Python versions:
Python 2 and Python 3. Both are quite different.


Before we start Python programming, we need to have an interpreter to interpret and run our programs.
There are certain online interpreters like https://ide.geeksforgeeks.org/, http://ideone.com/
or http://codepad.org/ that can be used to run Python programs without installing an interpreter.

Windows:
There are many interpreters available freely to run Python scripts like IDLE 
(Integrated Development Environment)that comes bundled with the Python software downloaded from http://python.org/.

Linux: 
Python comes preinstalled with popular Linux distros such as Ubuntu and Fedora.
To check which version of Python you’re running, type “python” in the terminal emulator.
The interpreter should start and print the version number.

macOS: 
Generally, Python 2.7 comes bundled with macOS.
You’ll have to manually install Python 3 from http://python.org/.


Writing our first program:
Just type in the following code after you start the interpreter.
"""
	
# Script Begins

print("GeeksQuiz")     #Output (in terminal) ----->  GeeksQuiz

# Scripts Ends

"""
Let’s analyze the script line by line :

Line 1: [# Script Begins] In Python, comments begin with a #. 
This statement is ignored by the interpreter and serves as documentation for our code.

Line 2: [print(“GeeksQuiz”)] To print something on the console, print() function is used.
This function also adds a newline after our message is printed(unlike in C). 
Note that in Python 2, “print” is not a function but a keyword and therefore can be used without parentheses. 
However, in Python 3, it is a function and must be invoked with parentheses.

Line 3: [# Script Ends] This is just another comment like in Line 1.

---------------------------------------------------------------------------------------------------
3-Python Language advantages and applications :

Python is a high-level, interpreted, and general-purpose dynamic programming language that focuses on code readability. 
It has fewer steps when compared to Java and C. It was founded in 1991 by developer Guido Van Rossum. 
Python ranks among the most popular and fastest-growing languages in the world. 
Python is a powerful, flexible, and easy-to-use language. In addition, the community is very active there. 
It is used in many organizations as it supports multiple programming paradigms. 
It also performs automatic memory management.


*Advantages : 
    Presence of third-party modules 
    Extensive support libraries(NumPy for numerical calculations, Pandas for data analytics etc) 
    Open source and community development 
    Versatile, Easy to read, learn and write
    User-friendly data structures 
    High-level language 
    Dynamically typed language(No need to mention data type based on the value assigned, it takes data type) 
    Object-oriented language 
    Portable and Interactive
    Ideal for prototypes – provide more functionality with less coding
    Highly Efficient(Python’s clean object-oriented design provides enhanced process control, and the language is equipped with excellent text processing and integration capabilities, as well as its own unit testing framework, which makes it more efficient.)
    (IoT)Internet of Things Opportunities
    Interpreted Language
    Portable across Operating systems 

*Applications : 
    GUI based desktop applications
    Graphic design, image processing applications, Games, and Scientific/ computational Applications
    Web frameworks and applications 
    Enterprise and Business applications 
    Operating Systems 
    Education
    Database Access
    Language Development 
    Prototyping 
    Software Development
 
*Organizations using Python : 
    Google(Components of Google spider and Search Engine) 
    Yahoo(Maps) 
    YouTube 
    Mozilla 
    Dropbox 
    Microsoft 
    Cisco 
    Spotify 
    Quora 
---------------------------------------------------------------------------------------------------
4-Download and Install Python 3 Latest Version :

How to Download and Install Python 3 Latest Version? In this article, 
you will get the answer to all your questions related to installing Python on Windows/Linux/macOS. 
Python was developed by Guido van Rossum in the early 1990s and its latest version is 3.10.0, 
we can simply call it as Python3.

To understand how to install Python You need to know What Python is and where it is actually installed in your system.

Let’s consider a few points:
    Python is a widely-used general-purpose, high-level programming language.
    Every Release of Python is open-source. Python releases have also been GPL-compatible.
    Any version of Python can be downloaded from Python Software Foundation website at python.org.
    Most of the languages, notably Linux provide a package manager through which you can directly install Python on your Operating System
    In this Python tutorial of Installation and Setup, you’ll see how to install Python on Windows, macOS, Linux, iOS, and Android.


Python Latest Version Installation and Setup:
Here you can choose your OS and see the corresponding tutorial,
    Windows
    Linux
    macOS / Mac OS X
    Android
    iOS (iPhone / iPad)
    Online Interpreters of Python


****How to install Python on Windows?
Since windows don’t come with Python preinstalled, it needs to be installed explicitly. 
Here we will define step by step tutorial on How to install Python on Windows.

Follow the steps below :
    *Download Python Latest Version from python.org
    *Install Python 3.7.4 Latest Version on Windows
    *Make sure to mark Add Python to PATH otherwise you will have to do it explicitly.
    *After installation is complete click on Close.
    Bingo..!! Python is installed. Now go to windows and type IDLE.


****How to install Python on Linux?
On every linux system including following OS,
    Ubuntu
    Linux Mint
    Debian
    openSUSE
    CentOS
    Fedora
    and my favourite one, Arch Linux.

*You will find Python already installed. You can check it using the following command from the terminal
    $ python --version

    To check latest version of python 2.x.x :
        $ python2 --version
    To check latest version of python 3.x.x :
        $ python3 --version

Clearly it won’t be the latest version of python. 
There can be multiple methods to install python on a linux base system and it all depends on your linux system.
For almost every Linux system, the following commands would work definitely.

    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
    $ sudo apt-get install python3.7

Download and install Python Latest Version on Linux
To install the latest version from source code of Python follow below steps:

    Download Python Latest Version from python.org:

    1-Download Python Latest Version from python.org:
    *First and foremost step is to open a browser and open https://www.python.org/downloads/source/
    *Underneath the Stable Releases find Download Gzipped source tarball (latest stable release as of now is Python 3.10.0).
    You can do all the above steps in a single command
        $ wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz

    2-Install Python 3.7.4 Latest Version on Linux:
    For installing Python successfully on Linux, Enter Following command to get the prerequisites and other source files
        $ sudo apt-get update
        $ sudo apt-get upgrade
        $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev  libncursesw5-dev xz-utils tk-dev

    Now we are all ready to unpack the file downloaded from the python official website’
    Move to downloads directory using cd downloads in terminal
    and then enter following commands

    $ tar xvf Python-3.6.5.tgz
    $ cd Python-3.6.5
    $ ./configure --enable-optimizations --with-ensurepip=install
    $ make -j 8
    $ sudo make altinstall

Bingo..!! 
The latest version of Python language is installed on your Linux system. You can confirm it using the below command.
   $ python --version

****How to install Python on macOS / Mac OS X ?
Like Linux, macOS also comes with Python pre-installed on the system. 
It might be Python version 2 or some similar outdated version. 
To update to the latest version, we will use the Homebrew Package manager. 
It is one of the best and convenient methods to install Python on macOS.
To know more about Homebrew Package manager, visit https://brew.sh/

    1-Download and install Homebrew Package Manager:
    If you don’t have homebrew installed on your system, follow the steps below
    Open the Terminal Application of macOS from Application -> Utilities. Bash terminal will open where you can enter commands
    Enter following command in macOS terminal

    #    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    Enter the system password if prompted. This will install the Homebrew package Manager on your OS.
    After you see a message called “Installation Successful”. 
    You are ready to install python version 3 on your macOS.

    2-Install Python Latest Version on macOS / macOS X:
    To install python simple open Terminal app from Application -> Utilities
    and enter following command

    #    brew install python3

    After command processing is complete, Python’s version 3 would be installed on your mac.
    To verify the installation enter following commands in your Terminal app

    #   python
    #   pip

Bingo..!! Python is installed on your computer.

****How to install Python on Android ?
Python can run on Android through various apps from play store library.
This tutorial will explain how to run python on Android using "Pydroid 3 – IDE for Python 3" application.

Features :
    Offline Python 3.7 interpreter: no Internet is required to run Python programs.
    Pip package manager and a custom repository for prebuilt wheel packages for enhanced scientific libraries, such as numpy, scipy, matplotlib, scikit-learn and jupyter.
    Tensorflow is now also available.
    Examples available out-of-the-box for quicker learning.
    Complete Tkinter support for GUI.
    Full-featured Terminal Emulator, with a readline support (available in pip).

    1-Download Pydroid 3 – IDE for Python 3 app from Play store
        To install Pydroid app go to play store link here – Pydroid 3 – IDE for Python 3:
            https://play.google.com/store/apps/details?id=ru.iiec.pydroid3
    2-After installation is complete, run the app and it will show as installing python.
    3-Wait for a minute and it will show the ide. Here you can enter the Python code.
    4-Click on the yellow button to run the code.
Python is installed successfully.

****How to install Python on iOS (iPhone / iPad)?
On iOS platform, Python can be installed using various apps from app store. 
One of the most popular app is "Pythonista". 
https://apps.apple.com/us/app/pythonista-3/id1085978097?ls=1
Pythonista is a complete development environment for writing Python™ scripts on your iPad or iPhone. 
Lots of examples are included — from games and animations to plotting, image manipulation, 
custom user interfaces, and automation scripts.

Since most of the apps are paid on IOS and it doesn’t allow any interpreters officially. 
One can run Python from online IDEs and https://ide.geeksforgeeks.org.

****Online Interpreters of Python :
In this modern era of digital technologies, one can run Python directly from its browser without explicitly installing Python on OS.
Here is a list of famous IDEs for python:

    GeeksforGeeks IDE – https://ide.geeksforgeeks.org
    Python Fiddle: http://pythonfiddle.com/
    Python Anywhere: https://www.pythonanywhere.com
    Online gdp compiler – https://onlinegdb.com

For expensive computations for deep learning libraries like TensorFlow, following IDEs can be used:

    kaggle – https://www.kaggle.com/
    JuPyter/IPython Notebook – https://jupyter.org/  
        Installation with pip:
            #   pip install jupyterlab
        Run JupyterLab: 
            #   jupyter-lab
    Google Colab – https://colab.research.google.com/

These interpreters can run Python codes easily except for complex 'Django' codes or 'TensorFlow libraries'. 
To run such advanced applications, you need to install Python explicitly.
---------------------------------------------------------------------------------------------------



"""




