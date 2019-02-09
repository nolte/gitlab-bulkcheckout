# -*- coding: utf-8 -*-

"""Local Git Checkout Tool repo Management"""

import logging

import gitlab

logger = logging.getLogger(__name__)


class GitLabConnector:
    def __init__(self, host, token):
        logger.debug("Start glitlab connector to %s", host)
        self.gl = gitlab.Gitlab(host, private_token=token)

    def findProjectsFromGroups(self, groups, activity):
        logger.debug("load projects from groups: %s", groups)
        for groupId in groups:
            logger.debug("load projects from: %s", groupId)
            glGroup = self.gl.groups.get(groupId)
            for project in glGroup.projects.list():
                activity.processProject(project)
