---
title: 02 - Installing Python and basic tools
root: '/modules/module-0'
tree: '00 - Prerequisites'
module: module-0
---

# 02. Installing Python and basic tools

`TODO: Add a link to the OVA and tell that it's also a possibility.`

Throughout this course we'll be using Python version `3.6.17` (together with [Pipenv](https://pipenv.readthedocs.io/en/latest/), [IPython](https://ipython.org) and [Jupyter Labs](https://jupyterlab.readthedocs.io)) which is the easiest to install via [Homebrew](https://brew.sh/) so let's get started and follow the instructions below:

Run (from command-line):

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

and wait for the script to finish. After that, reload the shell with:

```bash
$ exec $SHELL -l
```

Homebrew needs a couple of extra configuration steps in order to properly compile Python. We'll install these with:

```bash
$ brew install zlib
```

and

```bash
$ brew install sqlite
```

These installations take a while to complete, so grab yourself a decent cup of coffee & relax for a while. After the installation is done, we need to instruct Homebrew to use previously installed packages on compilers & pkg-config by adding a few lines to shell's configuration (it's either `~/.bashrc`, `~/.bash_profile` or `~/.zshrc`, depends on the shell used):

```bash
# ...pyenv config
# --------------------
export PIP_REQUIRE_VIRTUALENV=false
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"


# ... Homebrew config
# --------------------

#For compilers to find zlib you may need to set:
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"

#For pkg-config to find zlib you may need to set:
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/sqlite/lib/pkgconfig"
```

Now we're ready to install pyenv by running:

```bash
$ brew install pyenv
```

Verify the installation by running:

```bash
$ pyenv --version
```

This should give you something like:

```bash
$ pyenv 1.2.9
```

Now we're ready to _actually_ install the `3.6.7` version by running:

```bash
$ pyenv install 3.6.17
```

Now, let's set this version as the default and reload the shell by running:

```bash
$ pyenv global 3.6.17 && exec $SHELL
```

Verify the current (default) version of Python with:

```bash
$ python --version
```

...which should give you `Python 3.6.17`

Let's install [Pipenv](https://pipenv.readthedocs.io/en/latest/) via Homebrew:

```bash
$ brew install pipenv
```

and verify the installation with:

```bash
$ pipenv --version
```

...which should give you something like `pipenv, version 2018.11.26`

Finally(!) let's install [IPython](https://ipython.org) and [Jupyter Lab](https://jupyterlab.readthedocs.io):

```bash
$ pip install jupyter jupyterlab ipython
```

---
**Congrats! We're now done with the prerequisites for tools used in the first modules of this course.**
