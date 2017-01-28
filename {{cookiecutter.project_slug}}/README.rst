{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
###############################
{{ cookiecutter.project_name }}
###############################

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.project_slug }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
    :alt: Wheel Status

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
    :alt: Python Versions

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
    :alt: License

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    :alt: Build status

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.svg
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    :alt: Coverage

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?format=svg
    :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io
    :alt: Documentation
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
    :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
    :alt: Updates

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `kidosoft/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`kidosoft/cookiecutter-pypackage`: https://github.com/kidosoft/cookiecutter-pypackage
