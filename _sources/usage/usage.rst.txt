==============================================
Usage
==============================================


.. _cli-parameters:

.. click:: gitlab_bulkcheckout.cli:main
   :prog: gitlab_bulkcheckout
   :show-nested:


.. _cli-config:

Config
----------------------------------------------


.. literalinclude:: ../../tests/example_config.yml
   :language: yaml
   :caption: example config
   :name: checkout-command-config-example


.. code:: yaml
  :name: checkout-command-config-bootstrap

  ...
  [gitlabGroupId]:
    # prefix for the local projects
    fs_prefix: "cookiecutter"
    # local folder for all projects from this group relative to $PROJECTS_BASE
    path: "templating"
  ...
