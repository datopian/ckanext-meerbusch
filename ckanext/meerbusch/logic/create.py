from datetime import datetime

import ckan.logic as l
from ckanext.meerbusch.helpers import get_date_format


def package_create(context, data_dict):
    temporal_from = data_dict['temporal_coverage-temporal_coverage_from']
    temporal_to = data_dict['temporal_coverage-temporal_coverage_to']
    role_date_1 = data_dict['dates-1-date']
    role_date_2 = data_dict['dates-2-date']
    role_date_3 = data_dict['dates-3-date']

    date_format = get_date_format()
    
    try:
        data_dict['temporal_coverage-temporal_coverage_from'] = datetime.strptime(temporal_from, date_format).strftime('%Y-%m-%d')
        data_dict['temporal_coverage-temporal_coverage_to'] = datetime.strptime(temporal_to, date_format).strftime('%Y-%m-%d')
        data_dict['dates-1-date'] = datetime.strptime(role_date_1, date_format).strftime('%Y-%m-%d')
        data_dict['dates-2-date'] = datetime.strptime(role_date_2, date_format).strftime('%Y-%m-%d')
        data_dict['dates-3-date'] = datetime.strptime(role_date_3, date_format).strftime('%Y-%m-%d')
    except ValueError:
        data_dict['temporal_coverage-temporal_coverage_from'] = temporal_from
        data_dict['temporal_coverage-temporal_coverage_to'] = temporal_to
        data_dict['dates-1-date'] = role_date_1
        data_dict['dates-2-date'] = role_date_2
        data_dict['dates-3-date'] = role_date_3

    dataset = l.action.create.package_create(context, data_dict)
       
    return dataset