# Code to ellyptical python
The code in this repository will overwrite any python file and replace it with ellyptical Python (see [this](https://susam.net/elliptical-python-programming.html) for reference).
Any machine that can run a .py file can run ellyptical python as it's a feature of the language and doesn't have any dependencies.

## Examples
I've provided, alongside the converter, two example files:
-example_python.py is a very simple and normal python file that asks the user for their name and repeats it.
-example_ellyptical-python.py is what example_python.py looks like after being overwritten by my converter. Even though it looks very different, the two files actually do the same exact thing.

## Pros and cons of ellyptical python
One downside of ellyptical python is that it's quite slow, although this issue may be partly avoided by optimizing the ellypses. As of now, they aren't at all optimized so both the converter and the resulting files will take some time to execute, especially if there's a lot of code.
However, it can also double as code obfuscation. It is not very good at that, though, because you can just get the normal python code by substituting the exec function call with a print statement.
