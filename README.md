# GemScanner

GemScanner identifies depreciated versions of gems in your ruby on rails project ( Gemfile.lock )  and notifies about their latest version.

## Requirements

```
▶ requests
▶ os
▶ sys
▶ corlorama
▶ argparse
```

## Usage

Basic usage:

```
▶ python3 GemScanner.py --file /path/to/Gemfile.lock --output results.txt

```

Options:

```
▶ usage: GemScanner.py [-h] -f FILE -o OUTPUT

Script to find depreciated versions in Gemfile.lock

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to Gemfile.lock
  -o OUTPUT, --output OUTPUT
                        Output file

```

## Demo

![GemScanner%209c8742e5462e4da7a32cb6507ee0c57c/gemscanner.gif](GemScanner%209c8742e5462e4da7a32cb6507ee0c57c/gemscanner.gif)

## TODO

- Add HTML Template Reporting
- Add threading Support