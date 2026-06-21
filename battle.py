#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(fac_a: CreatureFactory, fac_b: CreatureFactory) -> None:
    crea = fac_a.create_base()
    creb = fac_b.create_base()
    print("\nTesting battle")
    print(crea.describe())
    print(" vs.")
    print(creb.describe())
    print(" fight!")
    print(crea.attack())
    print(creb.attack())


if __name__ == "__main__":
    flame_fac: CreatureFactory = FlameFactory()
    aqua_fac: CreatureFactory = AquaFactory()

    test_factory(flame_fac)
    print()
    test_factory(aqua_fac)
    test_battle(flame_fac, aqua_fac)
