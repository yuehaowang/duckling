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
$ pip install Pillow
```

> :warning: Note: if you are using *Linux* or *MacOS*, the default *pip* may serve *python2*. Therefore, try using *pip3* instead.

> :warning: Note: if your installation is stopped by 'Permission denied', retry this step with prefixed command *sudo* . 

> :warning: Note: if you are a Windows user, choose an appropriate PyOpenGL package [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl), then download and install it using `pip install PyOpenGL‑A.B.C‑cpXX‑cpXXm‑win_amd64.whl`. Official PyOpenGL package doesn't work satisfyingly on modern Windows.

### 3, Clone *duckling*

Clone *duckling* to your local file system by using *git*:

```bash
$ git clone https://github.com/yuehaowang/duckling.git
```

### 4, Run a simple demo

Then, run a simple demo to test whether you have successfully finished those steps above:
```bash
$ cd ./duckling
$ python run.py demo/hello_world/  # if the default python in your system is python2, use `python3 run.py demo/hello_world/` instead.
```



## To-do

1. :white_square_button: Implement mouse event, keyboard event and loop event.
2. :white_medium_square: Implement `TweenLite`.
3. :white_medium_square: Implement `SAT` for testing collision.



## Issues

Any questions, suggestions and bug reports can be committed to the [issues](https://github.com/yuehaowang/duckling/issues) page.

In addition, emailing me is available as well: *wangyuehao1999@gmail.com*.
