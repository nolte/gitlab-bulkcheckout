# content of test_module.py
import pytest
import yaml

from gitlab_bulkcheckout.objects import CheckoutPreferenceManager


@pytest.fixture
def manager():
    mapping_config = yaml.load(open("./tests/example_config.yml"), Loader=yaml.SafeLoader)
    checkoutManagers = CheckoutPreferenceManager(mapping_config)
    return checkoutManagers


def test_func_fast(mocker, manager):
    assert 1 == len(manager.mappings)


def test_find_not_existing_group_by_id(mocker, manager):
    assert None is manager.getGroupConfig(666)


def test_find_existing_group_by_id(mocker, manager):
    groupConfig = manager.getGroupConfig(4564793)
    assert "cookiecutter" == groupConfig.fs_prefix


def test_get_name_of_non_existing_config(mocker, manager):
    gitlabProject = mocker.Mock()
    gitlabProject.name = "test-project"
    gitlabProject.id = 1
    gitlabProject.namespace = {"id": 6666}
    assert "test-project" == manager.getLocalProjectName(gitlabProject)


def test_get_name_of_existing_config(mocker, manager):
    gitlabProject = mocker.Mock()
    gitlabProject.name = "test-project"
    gitlabProject.id = 1
    gitlabProject.namespace = {"id": 4564793}
    assert "templating/cookiecutter-test-project" == manager.getLocalProjectName(gitlabProject)
