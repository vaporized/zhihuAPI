.. _examples:

Example Scripts
====================

.. highlight:: text

Here are some small examples using the package directly to achieve some common tasks.

If you have installed the package, you can run them directly. Otherwise please :code:`cd` to the code directory and run:

.. code:: bash

    python -m examples.xxxx [-a args]



machine_backup.py
--------------------
This script backups the followers, followees, following questions, following topics, following columns,
following favorite lists, questions, answers, pins, articles, columns, favorite lists, and activities in :code:`json`
format.

It also saves the plain html page of all answers, question and articles. However, pictures are not downloaded.

The program takes the following parameters:

.. code:: bash

    machine_backup [-c cookie_file_path] [-u single or multiple url_tokens] [-p save_path]

machine_renewal.py
--------------------
This script clones the following question, following topics and following people of an old account (usually terminated)
to the current account.

The program takes the following parameters:

.. code:: bash

    machine_renewal [-c cookie_file_path] [-u old_account_url_token]

machine_status.py
--------------------
This script checks the status of an account. It can handle common status like 停用, 禁言, 限制, and 重置.

The program takes the following parameters:

.. code:: bash

    machine_status [-c cookie_file_path] [-u url_token_to_query]

mourn_machines.py
--------------------
This script sends message: "RIP" to all followers whose accounts are disabled and reseted(special English translation of
[已重置] created by Zhihu).

The program takes the following parameters:

.. code:: bash

    mourn_machines [-c cookie_file_path]
