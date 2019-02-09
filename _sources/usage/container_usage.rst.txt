Container Usage
=================================================

|microbadger image| |microbadger version| |docker stars| |docker pulls|

For easy and quickly usage you can use the Dockerfile from `Dockerhub <https://hub.docker.com/r/nolte/gitlab-bulkcheckout>`_.

.. code:: bash

    docker pull nolte/gitlab-bulkcheckout:latest

For wrapping the tool, and checkout to your local FS it is required that you define some additional :ref:`usage-container-run-parameters`.

.. literalinclude:: docker_call.txt
   :language: bash
   :caption: execute checkout
   :name: docker-checkout-command


.. _usage-container-run-parameters:


Container Run Parameters
--------------------------------------------------

``--user ${UID}:$(id -g $(whoami))``
    The Container User will mapped to your user and group from the Host System, see `User <https://docs.docker.com/engine/reference/run/#user>`_.

.. _usage-container-run-parameters-ssh-forward:
``-v $SSH_AUTH_SOCK`` *(optional)*
    Required for forward the User SSH Agent from the Host System to the container.

``-e SSH_AUTH_SOCK`` *(optional)*
    see :ref:`-v $SSH_AUTH_SOCK <usage-container-run-parameters-ssh-forward>`

``-e GROUPS_MAPPINGS``
  The Path to the checkout config
  (see: :ref:`cli-parameters`, :ref:`Config Volume <usage-container-run-parameters-volume-checkout-config>`, :ref:`cli-config`,)

``-e GITLAB_TOKEN``
  `Gitlab Access Token <https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html>`_ for using the `Gitlab API <https://docs.gitlab.com/ee/api/>`_ (see: :ref:`cli-parameters`)
  This example use the Commandline Tool `pass <https://www.passwordstore.org/>`_ for manage this secred.

``-e PROJECTS_BASE``
  The Local Checkout Location, this path should be mapped to your Host System, (see: :ref:`cli-parameters`).

``-w /tmp/bulkcheckout``
  The Container `Workingdir <https://docs.docker.com/engine/reference/run/#workdir>`_.

``-v /tmp/bulkcheckout:/tmp/bulkcheckout``
  Some Folder mounted to your Host System, used as checkout Base.

``-v ${HOME}/.ssh:/home/builder/.ssh:ro``
  Mount your local SSH folder, for checkout the repositories over ssh.

.. _usage-container-run-parameters-volume-checkout-config:

``-v ${PWD}/gitlab_groupMapping.yml:/app/gitlab_groupMapping.yml:ro``
  The Used config file (see: :ref:`cli-config`)


.. include:: ../links.rst
