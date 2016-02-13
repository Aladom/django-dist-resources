# -*- coding: utf-8 -*-
# Copyright (c) 2016 Aladom SAS & Hosting Dvpt SAS
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DistResourcesConfig(AppConfig):
    name = 'dist_resources'
    verbose_name = _("Dist Resources")
