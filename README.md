# iya

<img src="https://img.shields.io/badge/status-under%20developement-9cf"> [![Node.js CI](https://github.com/apoleon33/iya/actions/workflows/node.js.yml/badge.svg?branch=master)](https://github.com/apoleon33/iya/actions/workflows/node.js.yml) <img src="https://badgen.net/github/dependabot/apoleon33/iya"> <img src="https://badgen.net/github/license/apoleon33/iya">

A Smash-Or-Pass website to recommend you waifus

# Summary

- [iya](#iya)
- [Summary](#summary)
- [Warning: WIP](#warning-wip)
- [TODO](#todo)
- [Installation](#installation)
  - [With make](#with-make)
  - [Whitout make](#whitout-make)

> **Warning**

Im not going to lie the algorithms are pretty lame (as well as the frontend and a bunch of other stuffs) at the moment so there is a big margin with what can be done and where we are at the moment

# TODO

- better-looking website
  - image not changing width/height
  - better responsive design
- website online
- way better algorithm
- indication on where the character is coming from
- etc...

# Installation

Once the repository has been cloned:

## With make

```sh
make install
```

Then whenever you feel launching the server:

```sh
make
```

## Without make

```sh
pip install -r backend/requirements.txt
cd frontend
npm install
```

Then whenever you feel launching the server:

```sh
python3 server.py
```
