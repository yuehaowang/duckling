# Duckling
----------

An OpenGL based game engine for Python.



## Installation

This project is still under development, but you can follow the steps below to check the current progress.

### 1, Make sure you're using *python3*

*Duckling* is built on *python3* and you may come across some weird problems if you import *duckling* to a *python2* project. The instructions below are based on the assumption that you are using *python3*, namely `python` and `pip` command serve *python3* instead of *python2*. If the default *python* in your system is *python2*, replace `python` and `pip` command in the following instructions with `python3` and `pip3` command respectively.

### 2, Clone *duckling*

Clone *duckling* to your local file system by using *git*:

```bash
$ git clone https://github.com/yuehaowang/duckling.git
```

### 3, Install *duckling*

#### On *Windows*

Windows users have to install *PyOpenGL* by yourself before configuring *duckling* since *duckling* is based on it and official *PyOpenGL* package doesn't work satisfyingly on modern Windows. Few steps below will show you how to install an unofficial but suitable *PyOpenGL* package on your Windows. 

First, download a *PyOpenGL* package which is compatible with your python environment [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl). Then, install the downloaded '.wheel' file using `pip install /path/to/your_downloaded_file.wheel`.

After the setup of *PyOpenGL*, open *Command Prompt*(or *Powershell*) in 'duckling/' directory and install *duckling* using `python setup.py install`.

#### On *Linux/MacOS*

It's quite easy for Linux/MacOS users to install *duckling* with the help of 'setup.py' after cloning *duckling* repo:

```bash
$ cd ./duckling
$ python setup.py install
```

> :warning: Note: if your installation is stopped by 'Permission denied', retry this step with prefixed command *sudo*. 


### 4, Run demo and examples

The *duckling* repo cloned from Github contains some demo and examples which can be utilized to check whether the intallation is perfectly done. For instance, run a 'Hello World' demo:

```bash
$ python demo/hello_world/main.py  # assuming your current working directory is 'duckling/'
```



## Documentation

- Online Documentation: http://wyh.wjjsoft.com/docs/duckling/



## To-do List

1. :white_square_button: Implement mouse event, keyboard event and loop event.
2. :white_medium_square: Implement `TweenLite`.
3. :white_medium_square: Implement `SAT` for testing collision.
4. :white_medium_square: Write a CLI tool for creating project, building project and deploying project.



## Issues

Any questions, suggestions and bug reports can be submitted to the [issues](https://github.com/yuehaowang/duckling/issues) page.

In addition, emailing me is available as well: *wangyuehao1999@gmail.com*.
