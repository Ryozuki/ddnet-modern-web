from flask import Flask
from yattag import Doc
from util import get_head, indent_doc, get_header

app = Flask(__name__)


@app.route('/')
def index():
    doc, tag, text, line = Doc().ttl()
    doc.asis('<!DOCTYPE html>')
    with tag("html", lang="en"):
        doc.asis(get_head("DDraceNetwork"))
        with tag("body"):
            with tag("article"):
                doc.asis(get_header())
                with tag("section"):
                    with tag("div", klass="block"):
                        line("h2", "DDRace Servers and much more!")
                        doc.asis("""<p>DDraceNetwork (DDNet) is an actively maintained version of DDRace, a 
                            <a href="https://www.teeworlds.com/\">Teeworlds</a> modification with a unique cooperative 
                            gameplay. Help each other play through <a href="/releases/">custom maps</a> with up to 64 
                            players, compete against the best in <a href="/tournaments/">international tournaments</a>, 
                            design your <a href="/howto/">own maps</a>, or run your <a href="/settingscommands/">own 
                            server</a>. The <a href="/status/">official servers</a> are located in Germany, Russia, 
                            USA, Canada, China, Chile, Brazil and South Africa. All <a href="/ranks/">ranks</a> made 
                            on official servers are available worldwide and you can <a href="/players/milk">collect 
                            points</a>!</p>
                            """)
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
