"""
This type stub file was generated by pyright.
"""

import logging
import os
import six

'''
Internationalization utilities.

This module contains code from the pojson project, which is subject to
the following license (see https://bitbucket.org/obviel/pojson):

Copyright (c) 2010, Fanstatic Developers
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and/or other materials provided with the
      distribution.
    * Neither the name of the organization nor the names of its
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL FANSTATIC
DEVELOPERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
if six.PY2:
    ...
log = logging.getLogger(__name__)
_CKAN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), u'..'))
_JS_TRANSLATIONS_DIR = os.path.join(_CKAN_DIR, u'public', u'base', u'i18n')
def get_ckan_i18n_dir():
    ...

def get_locales_from_config():
    ''' despite the name of this function it gets the locales defined by
    the config AND also the locals available subject to the config. '''
    ...

available_locales = None
locales = None
locales_dict = None
_non_translated_locals = None
def get_locales():
    ''' Get list of available locales
    e.g. [ 'en', 'de', ... ]
    '''
    ...

def non_translated_locals():
    ''' These are the locales that are available but for which there are
    no translations. returns a list like ['en', 'de', ...] '''
    ...

def get_locales_dict():
    ''' Get a dict of the available locales
    e.g.  { 'en' : Locale('en'), 'de' : Locale('de'), ... } '''
    ...

def get_available_locales():
    ''' Get a list of the available locales
    e.g.  [ Locale('en'), Locale('de'), ... ] '''
    ...

def get_identifier_from_locale_class(locale):
    ...

def handle_request(request, tmpl_context):
    ''' Set the language for the request '''
    ...

def get_lang():
    ''' Returns the current language. Based on babel.i18n.get_lang but
    works when set_lang has not been run (i.e. still in English). '''
    ...

def set_lang(language_code):
    ''' Wrapper to pylons call '''
    ...

def build_js_translations():
    '''
    Build JavaScript translation files.

    Takes the PO files from CKAN and from plugins that implement
    ``ITranslation`` and creates corresponding JS translation files in
    ``ckan.i18n_directory``. These include only those translation
    strings that are actually used in JS files.
    '''
    ...

