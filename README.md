# fix-apples-unicode

Apple uses ö instead of ö and I need to fix that.

* ä --> ä
* ö --> ö

Here's a good website to inspect the characters above: <https://babelstone.co.uk/Unicode/whatisit.html>

This program prints a list of `mv` commands that fixes the found issues.

## Installation

Assuming you have all the required Python dependencies installed globally on your system, you should be able to install it like this:

```shell
sudo make install
```

## Type checking

```shell
make test
```
