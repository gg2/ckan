"""
This type stub file was generated by pyright.
"""

import ckan.lib.navl.dictization_functions as df

missing = df.missing
StopOnError = df.StopOnError
Invalid = df.Invalid
def identity_converter(key, data, errors, context):
    ...

def keep_extras(key, data, errors, context):
    ...

def not_missing(key, data, errors, context):
    ...

def not_empty(key, data, errors, context):
    ...

def if_empty_same_as(other_key):
    ...

def both_not_empty(other_key):
    ...

def empty(key, data, errors, context):
    ...

def ignore(key, data, errors, context):
    ...

def default(default_value):
    '''When key is missing or value is an empty string or None, replace it with
    a default value'''
    ...

def configured_default(config_name, default_value_if_not_configured):
    '''When key is missing or value is an empty string or None, replace it with
    a default value from config, or if that isn't set from the
    default_value_if_not_configured.'''
    ...

def ignore_missing(key, data, errors, context):
    '''If the key is missing from the data, ignore the rest of the key's
    schema.

    By putting ignore_missing at the start of the schema list for a key,
    you can allow users to post a dict without the key and the dict will pass
    validation. But if they post a dict that does contain the key, then any
    validators after ignore_missing in the key's schema list will be applied.

    :raises ckan.lib.navl.dictization_functions.StopOnError: if ``data[key]``
        is :py:data:`ckan.lib.navl.dictization_functions.missing` or ``None``

    :returns: ``None``

    '''
    ...

def ignore_empty(key, data, errors, context):
    ...

def convert_int(value, context):
    ...

def unicode_only(value):
    '''Accept only unicode values'''
    ...

def unicode_safe(value):
    '''
    Make sure value passed is treated as unicode, but don't raise
    an error if it's not, just make a reasonable attempt to
    convert other types passed.

    This validator is a safer alternative to the old ckan idiom
    of using the unicode() function as a validator. It tries
    not to pollute values with Python repr garbage e.g. when passed
    a list of strings (uses json format instead). It also
    converts binary strings assuming either UTF-8 or CP1252
    encodings (not ASCII, with occasional decoding errors)
    '''
    ...

def limit_to_configured_maximum(config_option, default_limit):
    '''
    If the value is over a limit, it changes it to the limit. The limit is
    defined by a configuration option, or if that is not set, a given int
    default_limit.
    '''
    ...

