from yattag import Doc
from typing import List
from .util import script, link

FAVICON_APPLE_SIZES = [57, 114, 72, 144, 60, 120, 76, 152]
FAVICON_SIZES = [196, 160, 96, 16, 32]


def get_head(title: str, extra_tags: List[str] =None, refresh=False):
    if extra_tags is None:
        extra_tags = []

    doc, tag, text, line = Doc().ttl()
    stag = doc.stag
    with tag("head"):
        stag("meta", ("http-equiv", "Content-Type"), content="text/html;charset=utf-8")
        # Add favicons
        for x in FAVICON_APPLE_SIZES:
            doc.stag("meta", rel="apple-touch-icon", sizes=f"{x}x{x}",
                     href=f"/static/favicon/apple-touch-icon-{x}x{x}.png")
        for x in FAVICON_SIZES:
            doc.stag("meta", rel="icon", type="image/png", sizes=f"{x}x{x}",
                     href=f"/static/favicon/favicon-{x}x{x}.png")

        stag("meta", name="msapplication-TileColor", content="#2d89ef")
        stag("meta", name="msapplication-TileImage", content="/static/favicon/mstile-144x144.png")
        stag("meta", name="viewport", content="width=device-width")
        stag("meta", ("http-equiv", "cache-control"), content="max-age=0")
        stag("meta", ("http-equiv", "cache-control"), content="no-cache")
        stag("meta", ("http-equiv", "expires"), content="0")
        stag("meta", ("http-equiv", "expires"), content="Tue, 01 Jan 1980 1:00:00 GMT")
        stag("meta", ("http-equiv", "pragma"), content="no-cache")

        if refresh:
            stag("meta", ("http-equiv", "refresh"), content="120")

        link(doc, "/static/css/css.css?version=10")
        script(doc, "/static/js/js.js")

        line("title", title)

        for x in extra_tags:
            doc.asis(x)

    return doc.getvalue()


def get_header(menu: List[str]=None):
    if menu is None:
        menu = []

    doc, tag, text, line = Doc().ttl()
    stag = doc.stag

    with tag("header"):
        with tag("div", klass="fade"):
            with tag("menu", klass="contentleft"):
                with tag("div", klass="title"):
                    with tag("h1"):
                        with tag("a", href="/"):
                            stag("img", klass="logobig", alt="DDraceNetwork",
                                 src="/static/img/logos/ddnet2.svg")
                            stag("img", klass="logosmall", alt="DDraceNetwork",
                                 src="/static/img/logos/ddnet.svg")
                with tag("ul", klass="big"):
                    with tag("li"):
                        line("a", "Status", href="/status/")
                    with tag("li"):
                        line("a", "Ranks", href="/ranks/")
                    with tag("li"):
                        line("a", "Releases", href="/releases/")
                    with tag("li"):
                        line("a", "Discord", href="/discord")
                    with tag("li"):
                        line("a", "Forum", href="//forum.ddnet.tw/")
                    with tag("li"):
                        line("a", "Downloads", href="/downloads/")
                    with tag("li"):
                        line("a", "Downloads", href="/downloads/")
                    with tag("li"):
                        line("a", "Tournaments", href="/tournament/")
                    with tag("li"):
                        line("a", "Skin Database", href="/skins/")
                    with tag("li"):
                        line("a", "Statistics", href="/stats/")

                for x in menu:
                    doc.asis(x)

    return doc.getvalue()
