# *args and **kwargs


def add(*args):
    print(args)


add(10, 12, 12, 1, 21, 2)  # (10, 12, 12, 1, 21, 2)


# kwargs


def sub(**data):
    for k, v in data.items():
        print(f"{k}:{v}")


sub(name="sahil")
