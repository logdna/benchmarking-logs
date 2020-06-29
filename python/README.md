# Python Benchmarking

Here's a bunch of benchmarks to attempt with Python. Note that these were written with Python 3.7.4 on MacOS Mojave (10.14.6), and all commands are on a basic terminal.

## Setting up

This directory uses `pipenv` to make things simpler. Use the Pipfile to install your dependencies as explained in the `pipenv` docs.

## Running benchmarks

Use `time` to get a sense of timing. To learn more about why you need to know how long your benchmarks run, check out [the brief explanation in the benchmark's related article](https://dev.to/logdna/serverless-logging-performance-part-2-laj).

```bash
$ time python <filename>.py
```
