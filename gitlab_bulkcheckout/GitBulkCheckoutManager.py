# -*- coding: utf-8 -*-

"""Local Git Checkout Tool repo Management"""

import logging
import pathlib

from git import Repo

logger = logging.getLogger(__name__)


class ProjectExecuter:
    def __init__(self, basePath, mapper):
        self.mapper = mapper
        self.basePath = basePath

    def processProject(self, project):
        localPath = self.mapper.getLocalProjectName(project)
        fullPath = self.basePath + "/" + localPath
        logger.debug("checkout to: %s", fullPath)
        self.checkoutProject(fullPath, project)

    def checkoutProject(self, projectBaseDir, project):
        logger.info("start project checkout %s to %s", project.name, projectBaseDir)
        try:
            pathlib.Path(projectBaseDir).mkdir(parents=True, exist_ok=True)

            try:
                repo = Repo(projectBaseDir)
                if hasattr(repo.remotes, "origin"):
                    try:
                        repo.remotes.origin.pull()
                    except Exception as e:
                        logger.info("faild to pull %s", e)

            except Exception as e:
                logger.info("fail update exising project %s", e)
                repo = Repo.clone_from(project.ssh_url_to_repo, projectBaseDir)

        except Exception as e:
            logger.info("fail to clone direct %s", e)
            pass

        logger.info("start project checkout %s", projectBaseDir)
