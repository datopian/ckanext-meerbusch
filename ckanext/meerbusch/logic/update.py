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

    try:
        temporal_coverage['temporal_coverage_from'] = datetime.strptime(temporal_from, '%d.%m.%Y').strftime('%Y-%m-%d')
        temporal_coverage['temporal_coverage_to'] = datetime.strptime(temporal_to, '%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        temporal_coverage['temporal_coverage_from'] = temporal_from
        temporal_coverage['temporal_coverage_to'] = temporal_to
    
    dates = json.loads(package_dict['dates'])
    try:
        for date_role in dates:
            date_role['date'] = datetime.strptime(date_role['date'], '%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        pass

    data_dict['dates-1-date'] = dates[0]['date']
    data_dict['dates-1-role'] = dates[0]['role']
    data_dict['dates-2-date'] = dates[1]['date']
    data_dict['dates-2-role'] = dates[1]['role']
    data_dict['dates-3-date'] = dates[2]['date']
    data_dict['dates-3-role'] = dates[2]['role']


    # On resource_update the data_dict keys are as follows 'temporal_coverage-temporal_coverage_from/to'
    try:
        data_dict['temporal_coverage-temporal_coverage_from'] = datetime.strptime(temporal_from, '%d.%m.%Y').strftime('%Y-%m-%d')
        data_dict['temporal_coverage-temporal_coverage_to'] = datetime.strptime(temporal_to, '%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        data_dict['temporal_coverage-temporal_coverage_from'] = temporal_from
        data_dict['temporal_coverage-temporal_coverage_to'] = temporal_to
     
    data_dict['dates'] = dates

    print 'after data_dict'
    print '-------------------------------------------------'
    print data_dict
    print type(data_dict)

    
    dataset = l.action.update.package_update(context, data_dict)
    
    return dataset