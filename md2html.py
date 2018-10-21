#!/usr/bin/env python3

"""md2html: Markdown to PDF-printable HTML slideshow"""

import sys
import re
from markdown import markdown
from pygments.formatters import HtmlFormatter


def error():
    print("Usage: md2html [white|black] [IMG_FILENAME]", file=sys.stderr)
    sys.exit(1)


if len(sys.argv) > 3:
    error()

THEMES = ("white", "black")

args = iter(sys.argv[1:])
theme = next(args, "white")
img = next(args, None)

if theme not in THEMES:
    error()

hilite = HtmlFormatter().get_style_defs(".codehilite")
style = """
/* No background color of .codehilite */
.codehilite { background: transparent; }

* { box-sizing: border-box; }

html, body, section {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

section {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

a {
  color: cornflowerblue;
  text-decoration: none;
}

img { max-width: 95%; }

h1, h2, h3, h4, h5, h6 {
  width: 100%;
  font-family: Consolas, monospace;
}

p, ul > li { font-family: Verdana, Geneva, sans-serif; }

h1, h2, h3, h4, h5, h6, p {
  margin-bottom: 0;
  text-align: center;
}

h1 { font-size: 6em; }
h2, h3 { font-size: 4em; }
p { font-size: 2em; }

h1::before {
  color: #999;
  font-weight: 400;
  content: "./";
}

ul > li { font-size: 5rem; }

blockquote p { font-style: italic; }
  blockquote p::before,
  blockquote p::after {
    content: "\\"";
    color: #999;
  }

code {
  font-family: Courier, monospace;
}
  code::before,
  code::after {
    color: #999;
    content: "`";
  }

pre {
  font-size: 3em;
}

table {
  font-family: Consolas, monospace;
  font-size: 3em;
  text-align: center;
}
  th, td {
    padding: .2em;
  }
"""

script = """
class Slideshow {
  constructor () {
    this.$slides = document.querySelectorAll('section')
    this._len = this.$slides.length
    this._id = 0
    document.addEventListener('click', () => { ++this.activeId })
    window.addEventListener('keydown', e => {
      const key = e.which ? e.which : e.keyCode
      switch (key) {
        case 13:  // enter
        case 32:  // space
        case 39:  // right
        case 40:  // down
          e.preventDefault()
          ++this.activeId
          break
        case 8:   // backspace
        case 37:  // left
        case 38:  // up
          e.preventDefault()
          --this.activeId
          break
      }
    })
  }

  get activeId () { return this._id }

  set activeId (val) {
    if (val !== this.activeId && val >= 0 && val < this._len) {
      const prevId = this._id
      this._id = val
      this.show(prevId)
    }
  }

  show (prevId) {
    this.$slides[prevId].style.display = 'none'
    this.$slides[this.activeId].style.display = 'flex'
  }
}

(() => {
  const presentation = new Slideshow()
  presentation.show(0)
})()
"""

template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="initial-scale=1">
  <title>{title}</title>
  <style>{hilite}</style>
  <style>{style}</style>
  <style>{theme_block}</style>
</head>
<body>
{content}
<script>{script}</script>
</body>
</html>
"""

bgimg_rule = f"background: url({img}) no-repeat center center" if img else ""

theme_block = f"""
section {{
  {bgimg_rule};
  background-size: 100%;
  color: {"#000" if theme == "white" else "#fff"};
  background-color: {"#fff" if theme == "white" else "#000"};
}}

@media print {{
  @page {{ size: A3 landscape; }}

  section {{
    display: flex;
    page-break-after: always;
    page-break-inside: avoid;
  }}
}}
"""

md_exts = [
    f"markdown.extensions.{ext}"
    for ext in ("fenced_code", "tables", "codehilite")
]

content = sys.stdin.read()
_, _, title = content.split("\n", 1)[0].partition("# ")

content = markdown(content, extensions=md_exts)
content = "".join(
    [f"<section>{sec}</section>" for sec in content.split("<hr />")]
)

css_minify = lambda s: re.sub(r"\/\*.*\*\/|\n", "", s)

print(
    template.format(
        title=title,
        hilite=css_minify(hilite),
        style=css_minify(style),
        theme_block=css_minify(theme_block),
        script=script,
        content=content,
    )
)
