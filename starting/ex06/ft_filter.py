def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable
    for which function is true.

    If function is None, the identity function is assumed,
    that is, all elements of iterable that are false are removed.
    """

    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
