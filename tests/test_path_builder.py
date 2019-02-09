# content of test_module.py
import pytest

from gitlab_bulkcheckout.objects import CheckoutPreference


@pytest.mark.parametrize(
    "config,expected",
    [
        (
            CheckoutPreference({"fs_prefix": "cookiecutter", "path": "templating"}),
            "templating/cookiecutter-test-project",
        ),
        (CheckoutPreference({"fs_prefix": "test", "path": "templating"}), "templating/test-project"),
        (CheckoutPreference({}), "test-project"),
    ],
)
def test_func_fast(mocker, config, expected):
    gitlabProject = mocker.Mock()
    gitlabProject.name = "test-project"
    gitlabProject.id = 1
    gitlabProject.namespace = {"idMasterdata": 12345}
    assert expected == config.toLocalProjctName(gitlabProject)
