# -*- coding: utf-8 -*-

"""Main `gitlab_bulkcheckout` CLI."""

import logging

import click
import yaml

from gitlab_bulkcheckout.GitBulkCheckoutManager import ProjectExecuter
from gitlab_bulkcheckout.GitlabConnector import GitLabConnector
from gitlab_bulkcheckout.log import configure_logger
from gitlab_bulkcheckout.objects import CheckoutPreferenceManager

logger = logging.getLogger(__name__)


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
@click.option(u"--debug-file", type=click.Path(), default=None, help=u"File to be used as a stream for DEBUG logging")
def main(verbose, debug_file):
    """Console script for gitlab_bulkcheckout."""
    configure_logger(stream_level="DEBUG" if verbose else "INFO", debug_file=debug_file)


@main.command(help="Display the current version.")
def version():
    """Display the current version."""

    click.echo("0.1.0")


@main.command(help="Checkout all listed projects from configured groups.")
@click.option(
    "--host",
    "-h",
    default="https://gitlab.com",
    envvar="GITLAB_HOST",
    help="Url from the Gitlab Server, like https://gitlab.com",
)
@click.option("--private-token", envvar="GITLAB_TOKEN", help="Gitlab Private Acccess Token")
@click.option(
    "--mapping-config-path",
    "-m",
    default="gitlab_groupMapping.yml",
    envvar="GROUPS_MAPPINGS",
    help="Bulk Checkout configuration",
)
@click.option("--base", "-b", envvar="PROJECTS_BASE", help="The Basedirectory for the local checkout")
def checkoutbulk(private_token, host, mapping_config_path, base):
    """Checkout Projects from group config."""

    click.echo("start bulk download")
    # load the mapping config from filesystem
    mapping_config = yaml.load(open(mapping_config_path), Loader=yaml.SafeLoader)

    # init the config manager
    checkoutManagers = CheckoutPreferenceManager(mapping_config)

    # extract listed groups from config
    groupsList = checkoutManagers.getManagedGroups()
    logger.debug("import groups by ids: %s", groupsList)

    executor = ProjectExecuter(base, checkoutManagers)
    connector = GitLabConnector(host, private_token)

    # start bulk checkout
    connector.findProjectsFromGroups(groupsList, executor)
