# iya

<img src="https://img.shields.io/badge/status-under%20developement-9cf"> <img  src="https://img.shields.io/tokei/lines/github/apoleon33/iya"> <img src="https://badgen.net/github/dependabot/apoleon33/iya">

A Smash-Or-Pass website to recommend you waifus

# Summary

- [iya](#iya)
- [Summary](#summary)
- [Warning: WIP](#warning-wip)
- [TODO](#todo)
- [Installation](#installation)
  - [With make](#with-make)
  - [Whitout make](#whitout-make)

# Warning: WIP

Im not going to lie the algorithms are pretty lame (as well as the frontend and a bunch of other stuffs) at the moment so there is a big margin with what can be done and where we are at the moment

# TODO

- [ ] better-looking website
- [ ] website online
- [ ] way better algorithm

# Installation

Once the repository has been cloned:

You need to have [sass](https://sass-lang.com/install) installed for preprocessing the css

## With make

```sh
make install
```

Then whenever you feel launching the server:

```sh
make all # if you have never preprocessed the sass
# or
make run
```

## Whitout make

```sh
sass static/style.scss static/style.css
pip install -r requirements.txt
```

Then whenever you feel launching the server:

```sh
python3 server.py
```

Remember to re-preprocess the css everytime you modify the scss!
