# Admonitions

In MkDocs Material, callouts are called Admonitions. You can implement them easily by following these steps:

## Topics

### Modify mkdocs.yml

To enable adminitions, ensure that your Material theme supports admonitions by adding these lines to your configuration file:

~~~yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences

~~~

### Syntax for Callouts

Here's a basic example:

~~~markdown
!!! note "Optional title"
    This is a simple note callout.

~~~

### Types of Admonitions

You can use various predefined types:

!!! info
    + note
    + info
    + tip
    + warning
    + danger
    + success
    + question
    + example
    + quote
    + bug

### Examples

~~~md
!!! info "Important Information"
    Please read carefully before proceeding.

~~~

!!! info "Important Information"
    Please read carefully before proceeding.

---
~~~md
!!! warning "Be Careful!"
    You might lose your changes if you proceed without saving.

~~~
!!! warning "Be Careful!"
    You might lose your changes if you proceed without saving.
---


~~~md
??? tip "Collapsible tip"
    This content is hidden until expanded by the user.
~~~

??? tip "Collapsible tip"
    This content is hidden until expanded by the user.
