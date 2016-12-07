#!/usr/bin/env bash

# Copyright 2016 (c) Janus Friis Nielsen, all rights reserved.

git tag -a ${1} -m "Release version ${1}."

git push origin --tags
