---
title: Python Version with Quarto
toc-title: Table of contents
---

-   [Issues](#issues)
-   [Resolution](#resolution)
-   [Earlier Command Outputs](#earlier-command-outputs)
-   [References](#references)
-   [Code Chunks](#code-chunks)

Use `quarto render python_version.qmd -t markdown` to render as
markdown.

## Python Versions

Looking at list of environments:

  -------------------------------------------------------------------------------------------------------------------
  name                     version             location                                               label
  ------------------------ ------------------- ------------------------------------------------------ ---------------
  Python                   3.9.6               /usr/bin/python3                                       

  Python                   3.9.6               /Library/Developer/CommandLineTools/usr/bin/python3    recommended

  base Python              3.12.4              \~/miniconda3/bin/python                               conda env

  earth-analytics-python   3.11.10             \~/miniconda3/envs/earth-analytics-python/bin/python   

  Python                   3.12.7              /opt/homebrew/bin/python3.12                           global env

  Python                   3.13.0              /opt/homebrew/bin/python3                              

  r-reticulate Python      3.12/4              \~/.virtualenvs/r-reticulate/bin/python                

  old-eda-python           Python 3.11.10      \~/miniconda3/envs/old-eda-python/bin/python           virtual env
  -------------------------------------------------------------------------------------------------------------------

Jupyter finds Python environments through a few mechanisms:

1.  Kernel Specs:
    -   When you install a Python environment, and want to use it with
        Jupyter, you typically install the ipykernel package within that
        environment.
    -   This package creates a "kernel spec" file, which contains
        information about the environment (like its name, location, and
        Python interpreter path).
    -   Jupyter scans known locations for these kernel specs, allowing
        you to select the desired environment when creating a new
        notebook.
2.  Default Environment:
    -   If no kernel is explicitly selected, Jupyter uses the default
        Python environment associated with the Jupyter installation.
    -   This can often be the base Python environment where Jupyter is
        installed.
3.  JupyterLab Desktop:
    -   In JupyterLab Desktop, you can directly select the Python
        environment from a dropdown menu.
    -   This menu lists all detected environments, including virtual
        environments and conda environments.
4.  Conda Environments:
    -   If you're using conda, Jupyter automatically detects conda
        environments.
    -   You can use the conda install ipykernel command within your
        environment to make it available in Jupyter.

The shell command `jupyter kernelspec list` is supposed to list all
available kernels, but only shows\
`python3` `/Users/brianyandell/.local/share/jupyter/kernels/python3`

## Issues

The challenge I had when using Quarto was that I seem to have two
versions of Python:

-   Base(Python 3.12.4) \~/miniconda3/bin/python
-   Python 3.9.6 /Library/Developer/CommandLineTools/usr/bin/python3

I read [references](#references) but I don't understand them. I know how
to use the **Python: Select Interpreter** by hand, and that works for
code chunks but not for the qmd document (that is, I don't know how to
select interpreter for qmd files).The hint I get is that `conda` and
`quarto` may not always play well together, but I cannot understand what
to do next. I reached out to Elsa Culler, who suggested changes to
`~/.zshrc`. I further found an issue when mixing `python` and `r` code
chunks.

### Resolution

-   Edit `~/.zshrc` to point to conda bin
-   Edit `~/.zshrc` to export `QUARTO_PYTHON`
-   Change symbolic links in `~/.virtualenvs/r-reticulate/bin`

Changes to `~/.zshrc`:

> export PATH=\$PATH:/opt/R/arm64/gfortran/bin:/opt/homebrew/bin\

> #export PATH=/users/brianyandell/miniconda3/bin:\$PATH\

> #export
> PATH=/users/brianyandell/Library/Python/3.9/bin:/users/brianyandell/Library/Python/3.8/bin:\$PATH\

> export QUARTO_PYTHON=/users/brianyandell/miniconda3/bin/python

Changes to `~/.virtualenvs/r-reticulate/bin`:

The issue was revealed by mixing `python` and `r` code blocks in the
document. The `r` code block simply had

> knitr::knit_exit()

This forces `quarto` to use the `~/.virtualenvs/r-reticulate/bin`, which
had an old link. \[It also enables `bash` code chunks.\] I changed
symbolic link of `python` to point to the current miniconda version of
python, and changed the symbolic link of `python3.9` to the older
version

> `ls -l ~/.virtualenvs/r-reticulate/bin/python*`

> lrwxr-xr-x@ 1 brianyandell staff 7 Sep 9 13:28 python -\> python3

> lrwxr-xr-x 1 brianyandell staff 41 Jan 17 11:49 python3 -\>
> /Users/brianyandell/miniconda3/bin/python

> lrwxr-xr-x@ 1 brianyandell staff 58 Sep \> 9 13:28 python3.9 -\>
> /Applications/Xcode.app/Contents/Developer/usr/bin/python3

### Earlier Command Outputs

From the shell (bash or zsh), I get

> (base) brianyandell@Brians-MacBook-Pro habitatSuitability % python
> --version Python 3.12.4

If I run a code chunk from within a qmd, I get this as well. Consider
this current document,
[simple.qmd](https://github.com/byandell-envsys/habitatSuitability/blob/main/simple.qmd)
The code chunk yields.

> /Users/brianyandell/miniconda3/bin/python 3.12.4 \| packaged by
> Anaconda, Inc. \| (main, Jun 18 2024, 10:07:17) \[Clang 14.0.6 \]\`

However, rendering the document (using the little icon within VSCode or
from the command line with `quarto preview simple.qmd` yields

> /Library/Developer/CommandLineTools/usr/bin/python3 3.9.6 (default,
> Feb 3 2024, 15:58:27) \[Clang 15.0.0 (clang-1500.3.9.4)\]

I know there is a way in the YAML to set the version, say with
`jupyter: python3`. I tried putting `python` instead of `python3` and it
choked as it cannot find another kernel

> \% quarto preview simple.qmd --no-browser --no-watch-inputs\

> ERROR: Jupyter kernel 'python' not found. Known kernels: python3. Run
> 'quarto check jupyter' with your python environment activated to check
> python version used.

So it clearly does not know about the other versions.

## References

I found the following references. Note in particular the
`nb_conda_kernels`. This sounds pretty arcane. I tried it briefly, with
no success.

-   [Quarto: Virtual
    Environments](https://quarto.org/docs/projects/virtual-environments.html)
-   [Manage Jupyter Kernels in VS
    Code](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
-   [Quarto: Project
    Basics](https://quarto.org/docs/projects/quarto-projects.html)
-   [Quarto: Environment
    Variables](https://quarto.org/docs/projects/environment.html)
-   [How to Know Which Python is Running in Your Jupyter Notebook
    (SaturnCloud)](https://saturncloud.io/blog/how-to-know-which-python-is-running-in-your-jupyter-notebook/)
-   [Quarto: Using Python: Kernel
    Selection](https://quarto.org/docs/computations/python.html#kernel-selection)
    -   [nb_conda_kernels](https://github.com/anaconda/nb_conda_kernels#use-with-nbconvert-voila-papermill)

## Code Chunks

::::: cell
``` {.python .cell-code}
import sys
print(sys.executable)
```

::: {.cell-output .cell-output-stdout}
    /Users/brianyandell/.virtualenvs/r-reticulate/bin/python
:::

``` {.python .cell-code}
print(sys.version)
```

::: {.cell-output .cell-output-stdout}
    3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 10:11:37) [Clang 14.0.6 ]
:::
:::::

:::: cell
``` {.bash .cell-code}
cd ~/.virtualenvs/r-reticulate/bin
ls -l python*
```

::: {.cell-output .cell-output-stdout}
    lrwxr-xr-x@ 1 brianyandell  staff   7 Sep  9 13:28 python -> python3
    lrwxr-xr-x  1 brianyandell  staff  41 Jan 17 11:49 python3 -> /Users/brianyandell/miniconda3/bin/python
    lrwxr-xr-x@ 1 brianyandell  staff  58 Sep  9 13:28 python3.9 -> /Applications/Xcode.app/Contents/Developer/usr/bin/python3
:::
::::

::: cell
``` {.r .cell-code}
knitr::knit_exit()
```
:::
