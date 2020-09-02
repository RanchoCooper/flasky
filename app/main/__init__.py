#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint

from ..models import Permission

from . import views, errors

main = Blueprint('main', __name__)


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
