#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import Creature

if __name__ == "__main__":
    heal_ctr_fac: HealingCreatureFactory = HealingCreatureFactory()
    trans_ctr_fac: TransformCreatureFactory = TransformCreatureFactory()

    def test_heal(heal_ctr_fac: HealingCreatureFactory):
        print("Testing Creature with healing capabiity")
        print(" base:")
        sprouting: Creature = heal_ctr_fac.create_base()
        print(sprouting.describe())
        print(sprouting.attack())
        print(sprouting.heal("itself"))
        print(" evolved")
        bloomelle: Creature = heal_ctr_fac.create_evolved()
        print(bloomelle.describe())
        print(bloomelle.attack())
        print(bloomelle.heal("itself and others"))

    def test_trans(trans_ctr_fac: TransformCreatureFactory):
        print("\nTesting Creature with transform capability")
        print(" base:")
        shiftling: Creature = trans_ctr_fac.create_base()
        print(shiftling.describe())
        print(shiftling.attack())
        print(shiftling.transform())
        print(shiftling.attack())
        print(shiftling.revert())
        print(" evolved")
        morphagon: Creature = trans_ctr_fac.create_evolved()
        print(morphagon.describe())
        print(morphagon.attack())
        print(morphagon.transform())
        print(morphagon.attack())
        print(morphagon.revert())

    test_heal(heal_ctr_fac)
    test_trans(trans_ctr_fac)
