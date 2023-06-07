class A:
    def __init__(self):
        print("A")


class B(A):
    def test(self):
        print("test")


b = B()  # will print "A" bec. the class B do not have constructor

# ____________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")

    def test(self):
        print("test")


b = B()  # will print "B" bec. the class B have a constructor

# _________________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")

    def test(self):
        print("test")


b = B()  # will print A B

# ____________________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")

    def test(self):
        print("test")


class C(B, A):
    def __init__(self):
        print("C")


c = C()  # will print "C" bec. class C have his own constructor
# __________________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")

    def test(self):
        print("test")


class C(B, A):
    def test(self):
        print("test C")


c = C()  # will print "B" just the constructor of the first class he inherit it
# ___________________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")

    def test(self):
        print("test")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("C")


c = C()  # will print "B C" bec. the constructor have super so he will print the first class he inherit it and his constructor
# __________________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")

    def test(self):
        print("test")


class C:
    def __init__(self):
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")


d = D()  # will print "B D"
# ____________________________________________________________________________


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")

    def test(self):
        print("test")


class C(A):
    def __init__(self):
        super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")


d = D()  # here the class B(A) and class C(A) so will print "A C B D"
