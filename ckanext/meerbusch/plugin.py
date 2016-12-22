import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.meerbusch.helpers as _helpers


class MeerbuschPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes)
    
    # IPackageController
    
    def after_show(self, context, pkg_dict):
        
        pkg_dict.update({'identifier': pkg_dict.get('id')})
        return pkg_dict
        
    def before_view(self, pkg_dict):
        
        pkg_dict.update({'identifier': pkg_dict.get('id')})
        return pkg_dict

    # IRoutes

    def before_map(self, map):
        return map

    def after_map(self, map):
        return map

    # IDatasetForm
    
    def create_package_schema(self):
        schema = super(MeerbuschPlugin, self).create_package_schema()
        return schema

    def update_package_schema(self):
        schema = super(MeerbuschPlugin, self).update_package_schema()
        return schema

    def show_package_schema(self):
        
        schema = super(MeerbuschPlugin, self).show_package_schema()
        defaults = [toolkit.get_converter('convert_from_extras'),
                    toolkit.get_validator('ignore_missing')]
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'meerbusch')
        
    def get_helpers(self):
        return {
            'language_options':
                _helpers.language_options,
            'get_language_by_code':
                _helpers.get_language_by_code,
            'get_package_version':
                _helpers.get_package_version
        }
