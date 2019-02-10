# Gitlab Bulk Checkout Tool

[![Github Project Stars](https://img.shields.io/github/stars/nolte/gitlab-bulkcheckout.svg?label=Stars&style=social)](https://github.com/nolte/gitlab-bulkcheckout) [![Travis CI build status](https://travis-ci.org/nolte/gitlab-bulkcheckout.svg?branch=master)](https://travis-ci.org/nolte/gitlab-bulkcheckout) [![CircleCI build status](https://circleci.com/gh/nolte/gitlab-bulkcheckout.svg?style=svg)](https://circleci.com/gh/nolte/gitlab-bulkcheckout) [![Documentation Status](https://readthedocs.org/projects/gitlab-bulkcheckout/badge/?version=latest)](https://gitlab-bulkcheckout.readthedocs.io/en/stable/?badge=stable) [![Github Issue Tracking](https://img.shields.io/github/issues-raw/nolte/gitlab-bulkcheckout.svg)](https://github.com/nolte/gitlab-bulkcheckout) [![Github LatestRelease](https://img.shields.io/github/release/nolte/gitlab-bulkcheckout.svg)](https://github.com/nolte/gitlab-bulkcheckout) [![CodeFactor](https://www.codefactor.io/repository/github/nolte/gitlab-bulkcheckout/badge)](https://www.codefactor.io/repository/github/nolte/gitlab-bulkcheckout) [![microbadger image](https://images.microbadger.com/badges/image/nolte/gitlab-bulkcheckout.svg)](https://microbadger.com/images/nolte/gitlab-bulkcheckout) [![version](https://images.microbadger.com/badges/version/nolte/gitlab-bulkcheckout.svg)](https://microbadger.com/images/nolte/gitlab-bulkcheckout) [![docker stars](https://img.shields.io/docker/stars/nolte/gitlab-bulkcheckout.svg?style=flat)](https://hub.docker.com/r/nolte/gitlab-bulkcheckout) [![docker pulls](https://img.shields.io/docker/pulls/nolte/gitlab-bulkcheckout.svg?style=flat)](https://hub.docker.com/r/nolte/gitlab-bulkcheckout) [![pypi.org version](https://img.shields.io/pypi/v/gitlab-bulkcheckout.svg?style=flat)](https://pypi.org/project/gitlab-bulkcheckout)

Simple utitlity written in [Python](https://www.python.org) for the local repositories.
In a Time of SaaS, Isac and microservices, it can happen that you need many small repositories at your local Machine for Development, so it didn`t make fun to pull so many repositories.

## Features

- sort gitlab grops to fs folder
- append a prefix to the repos
- pull changes from origin


## Python

**Supported Python:**
[![version](https://img.shields.io/pypi/pyversions/gitlab-bulkcheckout.svg?style=flat)](https://pypi.org/project/gitlab-bulkcheckout)

**Current Version:**
[![pypiorgversion](https://img.shields.io/pypi/v/gitlab-bulkcheckout.svg?style=flat)](https://pypi.org/project/gitlab-bulkcheckout)

### Virtualenv

For easy usage and better dependency handling use a
[python-virtualenv](https://docs.python.org/3/tutorial/venv.html).

``` bash
virtualenv ~/venvs/gitlab-bulkcheckout
source ~/venvs/gitlab-bulkcheckout/bin/activate
```

### Install

For install the application from [pypi.org](https://pypi.org) use
[pip](https://pip.pypa.io/en/stable/).

``` bash
pip install gitlab-bulkcheckout
```

### Build

``` bash
virtualenv ~/venvs/gitlab-bulkcheckout-dev
source ~/venvs/gitlab-bulkcheckout-dev/bin/activate
pip install tox
tox
```

The tox script create a installable dist under ``./.tox/dist/*.tar.gz``

## Docker

For easy usage, the tool can be wrapped with docker, so you don`t need a local python env for using.


### Build

```bash
  docker build -t nolte/gitlab-bulkcheckout .
```

### Usage

```bash
  docker run -it \
    --user=${UID}:$(id -g $(whoami)) \
    -v $SSH_AUTH_SOCK:/ssh-agent \
    -e SSH_AUTH_SOCK=/ssh-agent \
    -e GROUPS_MAPPINGS=/app/gitlab_groupMapping.yml \
    -e GITLAB_TOKEN=$(pass /internet/gitlab.com/tokens/management) \
    -e PROJECTS_BASE=/tmp/bulkcheckout \
    -w /tmp/bulkcheckout \
    -v /tmp/bulkcheckout:/tmp/bulkcheckout \
    -v ${HOME}/.ssh:/home/builder/.ssh:ro \
    -v ${PWD}/gitlab_groupMapping.yml:/app/gitlab_groupMapping.yml:ro \
    nolte/gitlab-bulkcheckout -v checkoutbulk
```
