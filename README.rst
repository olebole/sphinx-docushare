Sphinxdoc DocuShare role
========================

This is a quick and dirty approach to retrieve the document title and
download URL for Docushare documents. The package is based on
`PyDocuShare <https://tmtsoftware.github.io/cont-pydocushare>`_.


Installation
------------

Install the package from Github:

.. code-block:: shell-session

    $ pip install git+https://github.com/olebole/sphinx-docushare


Configuration
-------------

Put the following to sphinxdocs ``conf.py``:

.. code-block:: python

    extensions = [
	"sphinx_docushare",
    ]
    docushare_baseurl = "https://example.com/docushare"
    docushare_username = os.environ["DOCUSHARE_USERNAME"]
    docushare_password = os.environ["DOCUSHARE_PASSWORD"]

.. warning::

   Do not put your password to ``conf.py``; this is a major
   security risk.


Usage
-----

Then, you can use it to refer to documents and document versions by their id:

.. code-block:: ReST

    * :docushare:`Document-3725`
    * :docushare:`Version-5760`

This creates links with the document title as text that points to the
download URL of the document.
