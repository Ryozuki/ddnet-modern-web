from flask import Flask, request
from yattag import Doc
from util import get_head, indent_doc, get_header, script, raw_link, raw_atom_link
import re

app = Flask(__name__)

# TODO: Move this into a config file or something.
DDNET_VERSION = "11.4.4"
YT_VIDEO_ID = "bcys_l20cKE"


@app.route('/')
def index():
    print(request.user_agent.string)
    doc, tag, text, line = Doc().ttl()
    stag = doc.stag
    doc.asis('<!DOCTYPE html>')
    with tag("html", lang="en"):
        doc.asis(get_head("DDraceNetwork", [raw_link("/static/css/jquery-ui-1.8.22.custom.css"),
                                            raw_atom_link("DDNet News", "/feed/")]))
        with tag("body"):
            with tag("article"):
                doc.asis(get_header())
                script(doc, "/static/js/youtube.js")
                with tag("section"):
                    with tag("div", klass="block"):
                        line("h2", "DDRace Servers and much more!")
                        doc.asis("""<p>DDraceNetwork (DDNet) is an actively maintained version of DDRace, a 
                            <a href="https://www.teeworlds.com/">Teeworlds</a> modification with a unique cooperative 
                            gameplay. Help each other play through <a href="/releases/">custom maps</a> with up to 64 
                            players, compete against the best in <a href="/tournaments/">international tournaments</a>, 
                            design your <a href="/howto/">own maps</a>, or run your <a href="/settingscommands/">own 
                            server</a>. The <a href="/status/">official servers</a> are located in Germany, Russia, 
                            USA, Canada, China, Chile, Brazil and South Africa. All <a href="/ranks/">ranks</a> made 
                            on official servers are available worldwide and you can <a href="/players/milk">collect 
                            points</a>!</p>
                            """)

                        # Video container
                        with tag("div", klass="startvideo"):
                            with tag("div", klass="video-container"):
                                with tag("div", ("data-id", YT_VIDEO_ID), klass="ytplayer"):
                                    pass
                        stag("br")

                        # Download buttons, donation...
                        with tag("div", klass="download"):
                            stag("img", klass="download-button", src="/static/img/download.svg", alt="Download")
                            with tag("p", klass="download"):
                                with tag("span", klass="big"):
                                    # TODO: DETECT OS HERE
                                    user_os = "unk"
                                    extension = ""
                                    for_text = ""
                                    version = DDNET_VERSION

                                    if re.match(r"android", request.user_agent.string, re.IGNORECASE):
                                        user_os = "and"
                                        extension = ".apk"
                                        for_text = "for Android"
                                        version = "9.3.1"
                                    elif re.match(r"wow64|win64", request.user_agent.string, re.IGNORECASE):
                                        user_os = "win64"
                                        extension = ".zip"
                                        for_text = "for Windows (64 bit)"
                                    elif re.match(r"windows", request.user_agent.string, re.IGNORECASE):
                                        user_os = "win32"
                                        extension = ".zip"
                                        for_text = "for Windows (32 bit)"
                                    elif re.match(r"linux.*x86_64", request.user_agent.string, re.IGNORECASE):
                                        user_os = "lin64"
                                        extension = ".tar.xz"
                                        for_text = "for Linux x86_64"
                                    elif re.match(r"linux.*i686", request.user_agent.string, re.IGNORECASE):
                                        user_os = "lin32"
                                        extension = ".tar.xz"
                                        for_text = "for Linux x86"
                                    elif re.match(r"macintosh|mac os", request.user_agent.string, re.IGNORECASE):
                                        user_os = "mac"
                                        extension = "-osx.dmg"
                                        for_text = "for Mac OS X"

                                    with tag("a",
                                             href=f"/static/downloads/DDNet-{DDNET_VERSION}-{user_os}{extension}"):
                                        text("Download DDraceNetwork Client & Server 11.4.4 for Windows (64bit)")
                                stag("br")
                                with tag("a", href="/downloads/"):
                                    text("Other systems and versions")
                            with tag("a", href="/discord"):
                                stag("img", width="36", src="/static/img/logos/discord.svg", alt="Discord")
                            with tag("a", href="/feed"):
                                stag("img", width="36", src="/static/img/logos/feed.svg", alt="Feed")
                            with tag("a", href="https://github.com/ddnet/"):
                                stag("img", width="36", src="/static/img/logos/github.svg", alt="GitHub")
                            with tag("div", klass="right", style="width: 100%; max-width: 20em;"):
                                with tag("a", href="/funding/"):
                                    with tag("div", klass="progressbar", id="funding-total",
                                             style="width:100%; margin-top:0.25em"):
                                        with tag("div", klass="progress-label"):
                                            pass
                                with tag("a", href="/funding/"):
                                    with tag("div", klass="progressbar", id="funding-old",
                                             style="width:100%; margin-top:0.25em"):
                                        with tag("div", klass="progress-label"):
                                            pass
                    with tag("div", klass="block"):
                        text("todo")
    return indent_doc(doc.getvalue())


@app.errorhandler(404)
def page_not_found(e):
    doc, tag, text, line = Doc().ttl()
    doc.asis('<!DOCTYPE html>')
    with tag("html"):
        doc.asis(get_head("DDraceNetwork: Page not found"))
        with tag("body"):
            with tag("article"):
                doc.asis(get_header())
                with tag("section"):
                    with tag("div", klass="block"):
                        line("h2", "Error 404:")
                        line("p", "Page not found")
    return indent_doc(doc.getvalue())


if __name__ == '__main__':
    app.run()
