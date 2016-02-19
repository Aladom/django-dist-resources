# -*- coding: utf-8 -*-
# Copyright (c) 2016 Aladom SAS & Hosting Dvpt SAS
from dist_resources import Zip, Raw)


class TwitterBootstrap(Zip):

    version = '4.0.0-alpha.2',
    source = 'https://github.com/twbs/bootstrap/archve/v{V}.zip'
    include = {
        'bootstrap-{V}': [
            'scss/',
            'dist/js/bootstrap.min.js',
        ],
    }
    rename = {
        'scss/bootstrap.scss': 'scss/_twbs.scss',
        'dist/js/bootstrap.min.js': 'js/bootstrap.js',
    }


class FontAwesome(Zip):

    version = '4.5.0'
    source = ('https://fortawesome.github.io/Font-Awesome/assets/'
              'font-awesome-{V}.zip')
    include = {
        'font-awesome-{V}': ['scss/', 'fonts/']
    }
    rename = {
        'scss/font-awesome.scss': 'scss/_fa.scss',
    }


class JQuery(Raw):

    version = '2.2.0'
    source = 'http://code.jquery.com/jquery-{V}.min.js'
    rename = {'jquery-{V}.min.js': 'jquery.js'}


class Pickadate(Zip):

    version = '3.5.6'
    source = 'https://github.com/amsul/pickadate.js/archive/{V}.zip'
    include = {
        'pickadate.js-{V}/lib/compressed': [
            'picker.js', 'picker.date.js', 'picker.time.js',
            'translations/fr_FR.js', 'themes/default.css',
            'themes/default.date.css', 'themes/default.time.css',
        ]
    }


class UriJS(Raw):
    version = '1.17.0'
    source = ('https://raw.githubusercontent.com/medialize/URI.js/v{V}/src/'
              'URI.min.js')
    rename = {'URI.min.js': 'URI.js'}


class Tether(Zip):

    version = '1.1.1'
    source = 'https://github.com/HubSpot/tether/archive/v{V}.zip'
    include = {
        'tether-{V}/dist/js': ['tether.min.js']
    }
    rename = {'tether.min.js': 'tether.js'}
