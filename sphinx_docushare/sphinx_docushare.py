from docutils import nodes
import docushare

ds = None


def docushare_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Link to a Docushare document

    Parameters
    ----------

    name :
        The role name used in the document.

    rawtext :
        The entire markup snippet, with role.

    text :
        The text marked with the role.

    lineno :
        The line number where rawtext appears in the input.

    inliner :
        The inliner instance that called us.

    options :
        Directive options for customization.

    content :
        The directive content for customization.

    Returns
    -------
    tuple
       2 part tuple containing list of nodes to insert into the
       document and a list of system messages.  Both are allowed to be
       empty.

    """
    app = inliner.document.settings.env.app
    global ds
    msg = []
    if ds is None:
        try:
            ds = docushare.docushare.DocuShare(base_url=app.config.docushare_baseurl)
            ds.login(
                username=app.config.docushare_username,
                password=app.config.docushare_password,
            )
        except Exception:
            msg.append(
                inliner.reporter.warning(
                    f"Could not login to DocuShare {app.config.docushare_baseurl}",
                    line=lineno,
                )
            )
            ds = "invalid"
    if ds == "invalid":
        url = f"{app.config.docushare_baseurl}/docushare/dsweb/Get/{text}"
        return [nodes.reference(rawtext, text, refuri=url)], msg
    try:
        doc = ds.object(text)
    except Exception:
        msg.append(
            inliner.reporter.warning(
                f"Could not find {text} on DocuShare",
                line=lineno,
            )
        )
        url = f"{app.config.docushare_baseurl}/dsweb/Get/{text}"
        return [nodes.reference(rawtext, text, refuri=url)], msg
    return [nodes.reference(rawtext, doc.title, refuri=doc.download_url)], msg


def setup(app):
    app.add_role("docushare", docushare_role)
    app.add_config_value("docushare_baseurl", None, "env")
    app.add_config_value("docushare_username", None, "env")
    app.add_config_value("docushare_password", None, "env")
