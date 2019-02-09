import logging

logger = logging.getLogger(__name__)


class CheckoutPreferenceManager:
    def __init__(self, mapping_config):
        self.mappings = {}
        for mapping in mapping_config:
            prefs = CheckoutPreference(mapping_config[int(mapping)])
            self.mappings[mapping] = prefs

    def getGroupConfig(self, groupId):
        if groupId in self.mappings:
            return self.mappings[groupId]
        else:
            return None

    def getManagedGroups(self):
        return self.mappings.keys()

    def getLocalProjectName(self, project):

        if project.namespace:
            groupConfig = self.getGroupConfig(project.namespace["id"])
        else:
            groupConfig = None

        if groupConfig:
            return groupConfig.toLocalProjctName(project)
        else:
            return project.name


class CheckoutPreference:
    def __init__(self, preferences):
        self.useProjectPath = True
        self.useProjectPrefix = True
        if "fs_prefix" in preferences.keys():
            self.fs_prefix = preferences["fs_prefix"]
        if "path" in preferences.keys():
            self.path = preferences["path"]

    def toLocalProjctName(self, project):
        path = ""
        if self.useProjectPath:
            if hasattr(self, "path"):
                path += self.path
                path += "/"

        if self.useProjectPrefix:
            if hasattr(self, "fs_prefix"):
                if self.fs_prefix not in project.name:
                    path += self.fs_prefix
                    path += "-"
                else:
                    logger.debug(
                        "skip adding checkoutprefix, the prefix %s allways exist in project name %s",
                        self.fs_prefix,
                        project.name,
                    )

        path += project.name
        return path
