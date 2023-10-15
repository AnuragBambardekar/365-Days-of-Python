# MkDocs

- allow you to generate nice-looking and modern documentation for Markdown files and your code's docstrings.

```cmd
pip install mkdocs
pip install "mkdocstrings[python]"
pip install mkdocs-material
```

Write all the relevant docstrings and when done, run:
```cmd
mkdocs new .
mkdocs serve
```

Setting up a new MkDocs project creates a default index.md page in docs/. The index page is the default entry point for your project documentation, and you can edit the text in this file to fit your project landing page. 

```
docs/
├── explanation.md
├── how-to-guides.md
├── index.md
├── reference.md
└── tutorials.md
```

MkDocs builds every Markdown file that it finds in docs/ as a separate page. The first page that shows up is always index.md. All remaining pages show up in the order listed in docs/.



