# This sample tests type inference for list expressions.

# pyright: strict, reportUnknownVariableType=false

from typing import Any, Collection, Generic, Literal, Sequence, TypeVar


v1 = [1, 2, 3]
t_v1: Literal["list[int]"] = reveal_type(v1)

v2 = [1, 3.4, "hi"]
t_v2: Literal["list[int | float | str]"] = reveal_type(v2)

v3 = []
t_v3: Literal["list[Unknown]"] = reveal_type(v3)

v4: list[object] = []

v5: object = []

v6: Sequence[float] = [3, 4, 5]

v7: Collection[object] = [[]]


_T = TypeVar("_T")


class Baz(Generic[_T]):
    def __get__(self, instance: Any, owner: Any) -> _T:
        ...

    def __set__(self, instance: Any, value: _T) -> None:
        ...


class Foo:
    ...


class Bar:
    baz: Baz[list[Foo]]


v10 = Bar()
t_v10_1: Literal["list[Foo]"] = reveal_type(v10.baz)
v10.baz = [Foo()]
t_v10_2: Literal["list[Foo]"] = reveal_type(v10.baz)