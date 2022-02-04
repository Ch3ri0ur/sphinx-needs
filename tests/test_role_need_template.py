from pathlib import Path

import pytest


@pytest.mark.parametrize("buildername, srcdir", [("html", "doc_test/doc_role_need_template")])
def test_doc_build_html(create_app, buildername):
    make_app = create_app[0]
    srcdir = create_app[1]
    app = make_app(buildername, srcdir=srcdir)

    app.build()
    html = Path(app.outdir, "index.html").read_text()
    assert "ROLE NEED TEMPLATE" in html
    assert (
        "[SP_TOO_001] Command line interface (implemented) Specification/spec - test;test2 - SP_TOO_002 -  - "
        "The Tool awesome shall have a command line interface." in html
    )
