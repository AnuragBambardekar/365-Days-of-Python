# About rst files

A ReStructuredText (RST) file is a plaintext file format commonly used for writing documentation. It is a lightweight markup language designed to be easy to read and write, while still allowing for the generation of structured documents.

## Common RST Directives and Elements

- Sections and Titles:

Sections are defined using underlines of dashes or equal signs.
Titles are created using the overline and underline syntax.

- Lists:

Unordered lists use asterisks, plus signs, or dashes.
Ordered lists use numbers followed by periods.

- Code Blocks:

Code blocks are created using the code-block directive or double colons ::.
Specify the programming language after the double colons for syntax highlighting.

- Links:

Internal links to sections: :ref:`Section Name`
External links: `Link Text <URL>`_

- Inline Markup:

Emphasis: *italic* or **bold**
Literal: code

- Images:

Include images using the image directive: .. image:: image.png

- Tables:

Create tables using the table directive or ASCII-style tables.

- Admonitions:

Highlight important information or warnings using admonitions.

```rst
.. note:: This is a note.
.. warning:: This is a warning.
```

## Rendering rst files

```cmd
rst2html my_document.rst > output.html
```