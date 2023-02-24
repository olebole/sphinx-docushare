import os
import sys

sys.path.append(os.path.abspath(".."))

master_doc = "index"
extensions = [
    "sphinx_docushare",
]
docushare_baseurl = os.environ["DOCUSHARE_BASEURL"]
docushare_username = os.environ["DOCUSHARE_USERNAME"]
docushare_password = os.environ["DOCUSHARE_PASSWORD"]
