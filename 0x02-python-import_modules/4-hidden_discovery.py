#!/usr/bin/python3

if __name__ == '__main__':
    """print name defined by hidden_4bmodule."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
