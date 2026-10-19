"""Bouwt webshop/preview/index.html: een klikbare preview van Hyggehond uit de productdata en blogteksten.
Gebruik: python3 webshop/preview/build.py"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "data"))
import producten  # noqa: E402

LEV = {"Rust & slapen": "L1", "Thuis": "L1", "Op pad": "L2", "Verzorging": "L2", "Cadeaus": "L2",
       "Eten & drinken": "L3", "Spelen & verrijking": "L3"}

prods = [{"h": p["handle"], "t": p["titel"], "c": p["collectie"], "l": LEV[p["collectie"]],
          "v": [{"n": n, "p": pr} for n, i, v, pr in p["var"]], "i": p["intro"], "b": p["voordelen"],
          "s": p["specs"], "f": [list(x) for x in p["faq"]], "w": p["w"]} for p in producten.P]


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(/products/([a-z0-9-]+)\)", r'<a href="#p-\2">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\(/collections/([a-z0-9-]+)\)", r'<a href="#c-\2">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\(/pages/([a-z0-9-]+)\)", r'<a href="#\2">\1</a>', s)
    return s


def md(text):
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    out, lst, tbl = [], None, []
    def flush():
        nonlocal lst, tbl
        if lst:
            out.append(f"<{lst[0]}>" + "".join(f"<li>{x}</li>" for x in lst[1]) + f"</{lst[0]}>")
            lst = None
        if tbl:
            rows = [r for r in tbl if not re.match(r"^\|[\s\-|]+\|$", r)]
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            h = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in cells[1:])
            out.append(f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            tbl = []
    for line in body.strip().splitlines():
        if line.startswith("|"):
            tbl.append(line); continue
        m = re.match(r"^(\s*)(- \[ \] |- |\d+\. )(.*)", line)
        if m:
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            if not lst or lst[0] != kind:
                flush(); lst = (kind, [])
            lst[1].append(inline(m.group(3))); continue
        flush()
        if not line.strip():
            continue
        if line.startswith("# "):
            continue  # titel komt uit front matter
        if line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    flush()
    return meta, "\n".join(out)


blogs = []
bdir = os.path.join(ROOT, "05-teksten", "blog")
for fn in sorted(os.listdir(bdir)):
    meta, body = md(open(os.path.join(bdir, fn)).read())
    slug = meta["url"].rsplit("/", 1)[1]
    blogs.append({"slug": slug, "t": meta["titel"], "d": meta["metabeschrijving"], "html": body})

tpl = open(os.path.join(HERE, "template.html")).read()
data = json.dumps({"products": prods, "blogs": blogs}, ensure_ascii=False).replace("</", "<\\/")
open(os.path.join(HERE, "index.html"), "w").write(tpl.replace("/*__DATA__*/null", data))
print("ok", len(prods), "producten,", len(blogs), "blogs")
