# Introduction #

See http://cjklib.org/0.3/installing.html for a full explanation.

Make sure you have [Python 2.5 or newer](http://www.python.org/download/), [SQLalchemy](http://www.sqlalchemy.org/download.html) and [SQLite](http://www.sqlite.org/download.html) installed (lets focus on SQLite for now). Jump to [Windows](QuickStart#Windows.md), [Ubuntu](QuickStart#Ubuntu.md) or [Debian](QuickStart#Debian.md) for an installer version.

# Steps #

  1. First download the latest release from [Downloads](http://code.google.com/p/cjklib/downloads/list) and unpack it.
```
  tar -xzf cjklib-0.3.tar.gz
```
  1. Go to the new directory
```
  cd cjklib-0.3
```
  1. Install
```
  sudo python setup.py install
```

Now you should be able to test most of the examples given under [Screenshots](Screenshots.md).

For the additionally offered dictionary functions you can:

  1. Install CEDICT (or any other out of EDICT, HanDeDict, CEDICTGR, CFDICT):
```
  sudo installcjkdict CEDICT
```

That's it.

## Windows ##
Download the .exe installer for MS Windows from [Downloads](http://code.google.com/p/cjklib/downloads/list) and run it.

Make sure C:\Python26\Scripts is in your `PATH` enviroment.

Install CEDICT (or any other, see above)::
```
  installcjkdict CEDICT
```