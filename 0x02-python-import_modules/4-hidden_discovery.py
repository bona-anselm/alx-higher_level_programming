#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    list_dir = dir(hidden_4)
    for name in list_dir:
        if name[:2] != '__':
            print("{}".format(name))

