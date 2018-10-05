from flask import Flask
from yattag import Doc
from util import get_head, indent_doc

app = Flask(__name__)


@app.route('/')
def index():
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag("html", lang="en"):
        doc.asis(get_head("DDraceNetwork"))
    return indent_doc(doc.getvalue())


@app.errorhandler(404)
def page_not_found(e):
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag("html"):
        doc.asis(get_head("DDraceNetwork: Page not found"))
        with tag("body"):
            with tag("div", klass="block"):
                text("Page not found")
    return indent_doc(doc.getvalue())


if __name__ == '__main__':
    app.run()
