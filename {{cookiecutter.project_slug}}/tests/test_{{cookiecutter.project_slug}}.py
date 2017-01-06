#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""

import unittest
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from contextlib import contextmanager
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_do_something(self):
        pass
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
{%- endif %}
