from yattag import Doc, SimpleDoc, indent


def indent_doc(doc: str):
    return indent(doc,
                  indentation="  ",
                  indent_text=True,
                  newline="\r\n")


def script(doc: SimpleDoc, path: str):
    """A script tag"""
    with doc.tag("script", src=path, type="text/javascript"):
        pass


def link(doc: SimpleDoc, path: str):
    """A link tag"""
    doc.stag("link", rel="stylesheet", type="text/css", href=path)


def raw_script(path: str):
    """A script tag"""
    doc = Doc()
    with doc.tag("script", src=path, type="text/javascript"):
        pass
    return doc.getvalue()


def raw_link(path: str):
    """A link tag"""
    doc = Doc()
    doc.stag("link", rel="stylesheet", type="text/css", href=path)
    return doc.getvalue()


def raw_atom_link(title: str, path: str):
    doc = Doc()
    doc.stag("link", rel="alternate", type="application/atom+xml", title=title, href=path)
    return doc.getvalue()
