#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory, Creature

if __name__ == "__main__":
    flame_fac: CreatureFactory = FlameFactory()
    aqua_fac: CreatureFactory = AquaFactory()

    def test_create(
            flame_fac: CreatureFactory, aqua_fac: CreatureFactory
            ) -> None:
        print("Testing factory")
        flaming: Creature = flame_fac.create_base()
        print(flaming.describe())
        print(flaming.attack())
        pydoron: Creature = flame_fac.create_evolved()
        print(pydoron.describe())
        print(pydoron.attack())
        print("\nTesting factory")
        aquabub: Creature = aqua_fac.create_base()
        print(aquabub.describe())
        print(aquabub.attack())
        torragon: Creature = aqua_fac.create_evolved()
        print(torragon.describe())
        print(torragon.attack())

    def test_battle(
            flame_fac: CreatureFactory, aqua_fac: CreatureFactory
            ) -> None:
        flaming: Creature = flame_fac.create_base()
        aquabub: Creature = aqua_fac.create_base()
        print("\nTesting battle")
        print(flaming.describe())
        print(" vs.")
        print(aquabub.describe())
        print(flaming.attack())
        print(aquabub.attack())

    test_create(flame_fac, aqua_fac)
    test_battle(flame_fac, aqua_fac)
