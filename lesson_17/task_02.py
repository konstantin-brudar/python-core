# Множественное наследование

class WorldEaters:
    def khorn(self):
        print("World Eaters за Кхорна!")

class ThousandSons:
    def tzeentch(self):
        print("Thousand Sons за Тзинча!")

class Legion(WorldEaters, ThousandSons):
    pass

legion = Legion()
legion.khorn()
legion.tzeentch()


# У двух родительских классов есть общий предок

class Base:
    def process(self):
        print("Base.process")

class Left(Base):
    def process(self):
        print("Left.process")

class Right(Base):
    def process(self):
        print("Right.process")

class Combined(Left, Right):
    pass

obj = Combined()
obj.process()
print(Combined.mro())

# Ромбовидное наследование (diamond inheritance)

class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")

class C(A):
    def f(self):
        print("C")

class D(B, C):
    ...

d = D()
d.f()
print(D.mro())
super(B, d).f()
C.f(d)
print()


class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")
        super().f()

class C(B):
    def f(self):
        print("C")
        super(B, self).f()

C().f()

class C2(B):
    def f(self):
        print("C2")
        super().f()

C2().f()
print()


class X:
    def f(self):
        print("X")

class Y(X):
    def f(self):
        print("Y")

class Z(Y):
    def f(self):
        print("Z")

class Tail(Z):
    def f(self):
        super(Y, self).f()

t = Tail()
t.f()
