from sample_python.sub_b.b import f_b


def f_a():
    return "a" + f_b()


if __name__ == "__main__":
    print(f_a())
