from yattag import SimpleDoc, indent


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
