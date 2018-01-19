from setuptools import setup, find_packages


setup(
	name = "duckling",
	version = "1.0.0b1",
	description = "An OpenGL based game engine for Python.",
	author = "Yuehao Wang",
	author_email = "wangyuehao1999@gmail.com",
	url = "https://github.com/yuehaowang/duckling",
	license = "MIT",
	install_requires = [
		"Pillow",
		"PyOpenGL"
	],
	packages = find_packages()
)
