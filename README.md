# iya

<img src="https://badgen.net/github/license/apoleon33/iya"> [![Node.js CI](https://github.com/apoleon33/iya/actions/workflows/node.js.yml/badge.svg?branch=master)](https://github.com/apoleon33/iya/actions/workflows/node.js.yml) [![Docker Image CI](https://github.com/apoleon33/iya/actions/workflows/docker-image.yml/badge.svg)](https://github.com/apoleon33/iya/actions/workflows/docker-image.yml) <img src="https://badgen.net/github/dependabot/apoleon33/iya">  <img src="https://pyheroku-badge.herokuapp.com/?app=iyap"> 

A Smash-Or-Pass website to recommend you waifus

# Summary

- [iya](#iya)
- [Summary](#summary)
- [TODO](#todo)
- [Installation](#installation)
  - [With make](#with-make)
    - [Make a production-ready build](#make-a-production-ready-build)
  - [Without make](#without-make)
    - [Make a production-ready build](#make-a-production-ready-build-1)

> **Warning**

Im not going to lie the algorithms are pretty lame (as well as the frontend and a bunch of other stuffs) at the moment so there is a big margin with what can be done and where we are at the moment

# TODO

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

### Make a production-ready build

```sh
make production
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

### Make a production-ready build

```sh
cd frontend && npm run build
cp -r frontend/build/ backend/
python3 backend/server.py -p
```
