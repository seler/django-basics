from django.conf import settings
from django import template

if not getattr(settings, 'DEBUG', False):
    raise template.TemplateSyntaxError('dev_tools tags are available only when DEBUG = True')


register = template.Library()

class GetMethodsNode(template.Node):
    def __init__(self, object, context_name=None):
        self.object = template.Variable(object)
        self.context_name = context_name
        
    def render(self, context):
        object = self.object.resolve(context)
        methods = []
        core_model_methods = ['DoesNotExist', 'MultipleObjectsReturned', 'clean', 'clean_fields', 'date_error_message', 'delete', 'full_clean', 'prepare_database_save', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']
        for method in dir(object):
            try:
                if hasattr(getattr(object, method), '__call__') and not method.startswith('_') and method not in core_model_methods:
                    methods.append((method))
            except AttributeError:
                pass
        
        if self.context_name:
            context[self.context_name] = methods
            return ''
        else:
            return methods


@register.tag
def get_methods(parser, token):
    """

    Syntax::

        {% get_methods <object> [as <context_name>] %}

    """
    
    bits = token.split_contents()
    syntax_message = ("%(tag_name)s expects a syntax of "
                       "{% get_methods <object> [as <context_name>] %}")
    
    if len(bits) == 4 and bits[2] == 'as':
        return GetMethodsNode(bits[1], context_name=bits[3])
    elif len(bits) == 2:
        return GetMethodsNode(bits[1])
    else:
        raise template.TemplateSyntaxError(syntax_message)
    
    

class GetFieldsNode(template.Node):
    def __init__(self, object, context_name=None):
        self.object = template.Variable(object)
        self.context_name = context_name
        
    def render(self, context):
        object = self.object.resolve(context)
        fields = [(field.name, field.value_to_string(object)) for field in object._meta.fields]
        
        if self.context_name:
            context[self.context_name] = fields
            return ''
        else:
            return fields


@register.tag
def get_fields(parser, token):
    bits = token.split_contents()
    syntax_message = ("%(tag_name)s expects a syntax of "
                       "{% get_fields <object> [as <context_name>] %}")
    
    if len(bits) == 4 and bits[2] == 'as':
        return GetFieldsNode(bits[1], context_name=bits[3])
    elif len(bits) == 2:
        return GetFieldsNode(bits[1])
    else:
        raise template.TemplateSyntaxError(syntax_message)