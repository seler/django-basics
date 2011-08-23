from django.conf import settings
from django import template

if not getattr(settings, 'DEBUG', False):
    raise template.TemplateSyntaxError('dev_tools tags are available only when DEBUG = True')


register = template.Library()


class CallNode(template.Node):
    def __init__(self,object, method, args=None, kwargs=None, context_name=None):
        self.object = template.Variable(object)
        self.method = method
        if args:
            self.args = []
            for arg in args:
                self.args.append(template.Variable(arg))
        else:
            self.args = None

        if kwargs:
            self.kwargs = {}
            for key in kwargs:
                self.kwargs[key] = template.Variable(kwargs[key])
        else:
            self.kwargs = None

        self.context_name = context_name
        
    def render(self, context):
        object = self.object.resolve(context)
        if isinstance(object, str):
            raise template.TemplateSyntaxError('Given object is string ("%s") of length %d' 
                                               % (object, len(object)))
        
        args = []
        kwargs = {}
        if self.args:
            for arg in self.args:
                args.append(arg.resolve(context))
        if self.kwargs:
            for key in self.kwargs:
                kwargs[key] = self.kwargs[key].resolve(context)
            
        method = getattr(object, self.method, None)
        
        if method:
            if hasattr(method, '__call__'):
                result = method(*args, **kwargs)
            else:
                callable = False
            if self.context_name:
                context[self.context_name] = result
                return ''
            else:
                if not result == None: 
                    return result
                else:
                    return ''
        else:
            
            try:
                error_msg = 'Model %s don\'t have method "%s"' % (object._meta.object_name, self.method)
            except AttributeError:
                error_msg = 'Model %s don\'t have method "%s"' % (object, self.method)
            raise template.TemplateSyntaxError(error_msg)
                


@register.tag
def call(parser, token):
    """
    Passes given arguments to given method and returns result

    Syntax::

        {% call <object>[.<object>].<method or attribute> [with <*args> <**kwargs>] [as <context_name>] %}

    Example usage::

        {% call article.__unicode__ %}
        {% call article.get_absolute_url as article_url %}
        {% call article.is_visible with user %}
        {% call article.get_related with tag 5 as related_articles %}
        
        {% call object.foreign_object.test with other_object "some text" 123 article=article text="some text" number=123 as test %} 
    """
    
    bits = token.split_contents()
    syntax_message = ("%(tag_name)s expects a syntax of %(tag_name)s "
                       "<object>.<method or attribute> [with <*args> <**kwargs>] [as <context_name>]" %
                       dict(tag_name=bits[0]))
    
    temp = bits[1].split('.')
    method = temp[-1]
    object = '.'.join(temp[:-1])
    
    # Must have at least 2 bits in the tag
    if len(bits) > 2:
        try:
            as_pos = bits.index('as')
        except ValueError:
            as_pos = None
        try:
            with_pos = bits.index('with')
        except ValueError:
            with_pos = None

        if as_pos:
            context_name = bits[as_pos+1]
        else:
            context_name = None
        
        if with_pos:
            if as_pos:
                bargs = bits[with_pos+1:as_pos]
            else:
                bargs = bits[with_pos+1:]
        else:
            bargs = []
            
        args = []
        kwargs = {}
        
        if bargs:
            for barg in bargs:
                t = barg.split('=')
                if len(t) > 1:
                    kwargs[t[0]] = t[1]
                else:
                    args.append(t[0])
            
        return CallNode(object, method, args=args, kwargs=kwargs, context_name=context_name)
    elif len(bits) == 2:
        return CallNode(object, method)
    else:
        raise template.TemplateSyntaxError(syntax_message)
    

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