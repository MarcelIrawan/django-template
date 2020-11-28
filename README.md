# Django Template Project

Originally for personal use


## What I do

I override django user model for authentication,

As you may know, django use username for user authentication method

But I always prefer to use email instead of username

So I create this template so I can easily clone this project everytime I'm bulding django app


## What is it for

I create this repository for personal use

But if you find this repository and want to use it, feel free to clone or download the code


## Package Version
* Django - 3.1.3
* Django-REST-Framework - 3.12.2
* Django-rest-auth - 0.9.5
* Django-allauth - 0.44.0

For more detail about package version check the [requirements.txt](requirements.txt)

## Installing

!! I use Windows and git bash for the development !!
!! I'm not really sure if the command for the Linux and MacOS is working !!

Clone or download the project
```
$ git clone https://github.com/MarcelIrawan/django-template.git
```

Create virtual environment
```
Windows
$ python -m venv env

Linux or MacOS
$ python3 -m venv env
```

Activate the virtual environment
```
Windows
$ source env/Scripts/activate

Linux or MacOS
$ source env/bin/activate
```

Update pip (Opsional)
```
Windows
(env)$ python -m pip install -U pip

Linux or MacOS
(env)$ pip3 install -U pip
```

Install the requirements
```
Windows
(env)$ pip install -r requirements.txt

Linux or MacOS
(env)$ pip3 install -r requirements.txt
```


## Generate new Django Secret Key

I delete the secret key in this project [setting.py](https://github.com/MarcelIrawan/django-template/blob/main/base/settings.py#L23)

You can easily generate new code using [Djecrety](https://djecrety.ir/) - by [mrouhi13](https://github.com/mrouhi13)