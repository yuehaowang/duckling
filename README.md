# Duckling
----------

An OpenGL based game engine for Python.



## Configuration

This project is still under development, but you can follow the steps below to check the current progress.

### 1, Make sure you're using *python3*

*Duckling* is built on *python3* and you may come across some weird problems if you import *duckling* to a *python2* project. 

### 2, Setup *PyOpenGL* and *Pillow*

Before using *duckling*, install *PyOpenGL* and *Pillow* at first because *duckling* is based on the two libraries:

```bash
$ pip install PyOpenGL
$ pip install pillow
```

> :warning: Note: if you are using *Linux* or *MacOS*, the default *pip* may serve *python2*. Therefore, try using *pip3* instead.

> :warning: Note: if your installation is stopped by 'Permission denied', retry this step with prefixed command *sudo* . 

### 3, Clone *duckling*

Clone *duckling* to your local file system by using *git*:

```bash
$ git clone https://github.com/yuehaowang/duckling.git
```

### 4, Run a simple demo

Then, run a simple demo to test whether you have successfully finished those steps above:
```bash
$ cd ./duckling
$ python run_demo.py  # if the default python in your system is python2, use `python3 run_demo.py` instead.
```



## To-do

1. Implement mouse event, keyboard event and loop event.
2. Implement `TweenLite`.
3. Implement `SAT` for testing collision.



## Issues

Any questions, suggestions and bug reports can be committed to the [issues](https://github.com/yuehaowang/duckling/issues) page.

In addition, emailing me is available as well: *wangyuehao1999@gmail.com*.
