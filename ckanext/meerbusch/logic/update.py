import ast
import logging
import json
from datetime import datetime

import ckan.logic as l

def package_update(context, data_dict):
    package_dict = l.get_action('package_show')({}, {'id': data_dict['id']})
    print "package_dict"
    print package_dict
    print "data_dict"
    print data_dict

    temporal_coverage = json.loads(package_dict['temporal_coverage'])
    temporal_from = temporal_coverage['temporal_coverage_from']
    temporal_to = temporal_coverage['temporal_coverage_to']
    temporal_coverage['temporal_coverage_from'] = datetime.strptime(temporal_from, '%d.%m.%Y').strftime('%Y-%m-%d')
    temporal_coverage['temporal_coverage_to'] = datetime.strptime(temporal_to, '%d.%m.%Y').strftime('%Y-%m-%d')
    
    # On resource_update the data_dict keys are as follows 'temporal_coverage-temporal_coverage_from/to'
    temporal_coverage['temporal_coverage-temporal_coverage_from'] = datetime.strptime(temporal_from, '%d.%m.%Y').strftime('%Y-%m-%d')
    temporal_coverage['temporal_coverage-temporal_coverage_to'] = datetime.strptime(temporal_to, '%d.%m.%Y').strftime('%Y-%m-%d')
    data_dict['temporal_coverage-temporal_coverage_from'] = temporal_coverage['temporal_coverage-temporal_coverage_from']
    data_dict['temporal_coverage-temporal_coverage_to'] = temporal_coverage['temporal_coverage-temporal_coverage_to']
    print 'after data_dict'
    print '-------------------------------------------------'
    print temporal_coverage['temporal_coverage-temporal_coverage_from']
    print temporal_coverage['temporal_coverage-temporal_coverage_to']
    print data_dict
    print type(data_dict)

    
    dataset = l.action.update.package_update(context, data_dict)
    
    return dataset