PyAegis
=======

**PyAegis** is an AST-based Static Application Security Testing (SAST) engine
for Python. It parses Python source files into an abstract syntax tree, runs
security rule plugins against the resulting nodes, and reports findings with
severity and confidence ratings before code is deployed.

The primary project documentation is maintained in `README.md
<README.md>`_.

Key capabilities
----------------

* Detection of SQL injection and OS command injection.
* Detection of hardcoded credentials and API keys.
* Detection of weak cryptographic hashes, ciphers, and key sizes.
* Detection of unsafe deserialization with ``pickle`` and ``yaml``.
* Exportable HTML and JSON security audit reports.

Installation
------------

PyAegis requires Python 3.10 or newer.

.. code-block:: console

   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   pip install -e .

On Windows, use ``py -m venv .venv`` and activate the environment with
``.\.venv\Scripts\Activate.ps1``. If PyYAML cannot build its native extension,
set ``PYYAML_FORCE_LIBYAML=0`` before running ``pip install -e .``.

Quick start
-----------

.. code-block:: console

   pyaegis app.py
   pyaegis -r ./src
   pyaegis -r ./src -ll
   pyaegis -r ./src -f html -o audit_report.html

Attribution
-----------

PyAegis builds on the open-source PyCQA Bandit AST engine, the foundational
static analysis framework for Python security scanning. The internal
``bandit`` Python package is retained for compatibility with the upstream
engine, plugins, formatters, and extension points.

License
-------

PyAegis is distributed under the Apache License 2.0. See ``LICENSE`` for
details.
