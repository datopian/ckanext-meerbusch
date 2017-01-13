import os
import json
import logging
import collections

import ckan.logic as l
from ckan.plugins import toolkit

log = logging.getLogger(__name__)

get_languages_path = lambda: os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                      'language-codes.json')
def language_options():
    '''ISO-639-1 Languages''' 
    
    languages = []
    try:
        with open(get_languages_path()) as f:
            try:
                languages = json.loads(f.read())
                log.info('Successfully loaded {} languages'.format(len(languages)))
                
            except ValueError as e:
                log.error(str(e))
                
    except IOError as e:
        log.error(str(e))
            
    return languages

def get_language_by_code(code):
    
    language = None
    try:
        with open(get_languages_path()) as f:
            try:
                languages = json.loads(f.read())
                for lang in languages:
                    
                    if lang.get('code') != code:
                        continue
                    
                    language = lang
                
            except ValueError as e:
                log.error(str(e))
                
    except IOError as e:
        log.error(str(e))
            
    return language

def get_package_version(id):
    version = 1
    try:
        _ = l.get_action('package_revision_list')({}, {'id': id})
        version = len(_)
        
    except l.NotFound:
        pass
    
    return version

def get_number_of_resources_for_type(list_, key, unique=False):
    ''' Take a list of dicts and create a new one containing just the
    values and the count for the key with unique values if requested. '''
    new_list = []
    formated_list =[]

    for item in list_:
        value = item.get(key)
        if not value or (unique and value in new_list):
            continue
        new_list.append(value)

    counter = collections.Counter(new_list)

    for key, value in dict(counter).iteritems():
        formated_list.append({'format': key, 'count': value})

    return formated_list

def get_package_by_name(package_name):

    package = toolkit.get_action('package_show')(data_dict={
        'id': package_name,
        'include_tracking': True
    })

    return package
