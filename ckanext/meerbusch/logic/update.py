import json
from datetime import datetime

import ckan.logic as l

def package_update(context, data_dict):
    package_dict = l.get_action('package_show')({}, {'id': data_dict['id']})
    
    try:
        temporal_coverage = json.loads(data_dict['temporal_coverage'])
        temporal_from = temporal_coverage['temporal_coverage_from']
        temporal_to = temporal_coverage['temporal_coverage_to']
        try:
            temporal_coverage['temporal_coverage_from'] = datetime.strptime(temporal_from, '%d.%m.%Y').strftime('%Y-%m-%d')
            temporal_coverage['temporal_coverage_to'] = datetime.strptime(temporal_to, '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError:
            temporal_coverage['temporal_coverage_from'] = temporal_from
            temporal_coverage['temporal_coverage_to'] = temporal_to
    except KeyError:
        temporal_from = data_dict['temporal_coverage-temporal_coverage_from']
        temporal_to = data_dict['temporal_coverage-temporal_coverage_to']
        try:
            data_dict['temporal_coverage-temporal_coverage_from'] = datetime.strptime(temporal_from, '%d.%m.%Y').strftime('%Y-%m-%d')
            data_dict['temporal_coverage-temporal_coverage_to'] = datetime.strptime(temporal_to, '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError:
            data_dict['temporal_coverage-temporal_coverage_from'] = temporal_from
            data_dict['temporal_coverage-temporal_coverage_to'] = temporal_to
    
    try:
        dates = json.loads(data_dict['dates'])
        try:
            for date_role in dates:
                date_role['date'] = datetime.strptime(date_role['date'], '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError:
            for date_role in dates:
                date_role['date'] = date_role['date']
        data_dict['dates'] = json.dumps(dates)
    except KeyError:
        try:
            data_dict['dates-1-date'] = datetime.strptime(data_dict['dates-1-date'], '%d.%m.%Y').strftime('%Y-%m-%d')
            data_dict['dates-2-date'] = datetime.strptime(data_dict['dates-2-date'], '%d.%m.%Y').strftime('%Y-%m-%d')
            data_dict['dates-3-date'] = datetime.strptime(data_dict['dates-3-date'], '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError:
            data_dict['dates-1-date'] = data_dict['dates-1-date']
            data_dict['dates-2-date'] = data_dict['dates-2-date']
            data_dict['dates-3-date'] = data_dict['dates-3-date']

    
    dataset = l.action.update.package_update(context, data_dict)
    
    return dataset