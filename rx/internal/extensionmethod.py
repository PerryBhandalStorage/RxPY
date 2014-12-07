def extends(base, needs_init=False):
    """Class decorator that extends base with methods from the decorated
    class.

    Keyword arguments:
    base -- Base class to extend with methods from cls
    needs_init -- If true, then init method of cls will be run by base init

    Returns a function that takes the class to be decorated.
    """

    def inner(cls):
        for name, value in cls.__dict__.items():
            iscallable = callable(getattr(cls, name))
            if iscallable and not name.startswith("__"):
                setattr(base, name, value)
            elif needs_init and name == "__init__":
                base.initializers.append(value)
        return cls
    return inner