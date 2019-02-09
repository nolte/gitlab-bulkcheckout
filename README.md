# Gitlab Bulk Checkout Tool

Simple utitlity written in [Python](https://www.python.org) for the local repositories.
In a Time of SaaS, Isac and microservices, it can happen that you need many small repositories at your local Machine for Development, so it didn`t make fun to pull so many repositories.

## Features

- sort gitlab grops to fs folder
- append a prefix to the repos
- pull changes from origin

## Using Tox Build Script

```bash
   source ~/development/lib/virtualenv/tox/bin/activate
   tox
```

The tox script create a installable dist under ``./.tox/dist/*.tar.gz``

## Docker

For easy usage, the tool can be wrapped with docker, so you don`t need a local python env for using.


### Build

```bash
  docker build -t nolte/gitlab-bulkcheckout .
```
ssh agent
https://kb.iu.edu/d/aeww

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
