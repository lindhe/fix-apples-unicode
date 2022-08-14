# fix-apples-unicode

Apple uses composite characters instead of proper Unicode characters for umlauts and overrings, and I need to fix that.

* å --> å
* ä --> ä
* ö --> ö
* Å --> Å
* Ä --> Ä
* Ö --> Ö

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
