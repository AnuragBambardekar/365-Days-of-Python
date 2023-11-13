=========
RST Guide
=========

Introduction
------------

This guide covers advanced features of ReStructuredText. NewText

Admonitions
~~~~~~~~~~~

.. note:: This is a note.

.. warning:: This is a warning.

Tables
~~~~~~

+-----------+------------+
| Header 1  | Header 2   |
+===========+============+
| Cell 1,1  | Cell 1,2   |
+-----------+------------+
| Cell 2,1  | Cell 2,2   |
+-----------+------------+

Images
~~~~~~

.. image:: path/to/image.png
   :width: 400
   :height: 300
   :alt: Alternative Text

Footnotes
~~~~~~~~~

This is a sentence with a footnote [#]_.

.. [#] Here is the footnote text.

Glossary
~~~~~~~~

Glossary term
  A definition of the glossary term.

References
~~~~~~~~~~

- :ref:`Link to a section`
- `External Link <https://example.com>`_
