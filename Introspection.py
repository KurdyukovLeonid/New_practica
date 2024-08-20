import inspect


def introspection_info(obj):
    print({'Type': type(obj)})
    for i in dir(introspection_info):
        print({'Attributes and methods': i})
    print({'Module': inspect.getmodule(introspection_info)})

introspection_info(5)
