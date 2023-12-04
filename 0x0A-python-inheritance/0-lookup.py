def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: Object to inspect.

    Returns:
    - List of attribute and method names.
    """
    return [attr for attr in dir(obj)];
