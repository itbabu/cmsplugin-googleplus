#!/usr/bin/env bash

flake8 cmsplugin_googleplus || exit $?
isort -q --recursive --diff src/ || exit $?
