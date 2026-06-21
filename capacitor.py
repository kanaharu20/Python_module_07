#!/usr/bin/env python3

from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability
from ex0 import Creature

if __name__ == "__main__":
    heal_ctr_fac: HealingCreatureFactory = HealingCreatureFactory()
    trans_ctr_fac: TransformCreatureFactory = TransformCreatureFactory()

    def test_heal(heal_ctr_fac: HealingCreatureFactory) -> None:
        print("Testing Creature with healing capability")
        print(" base:")
        sprouting: Creature = heal_ctr_fac.create_base()
        print(sprouting.describe())
        print(sprouting.attack())
        print(cast(HealCapability, sprouting).heal("itself"))
        print(" evolved")
        bloomelle: Creature = heal_ctr_fac.create_evolved()
        print(bloomelle.describe())
        print(bloomelle.attack())
        print(cast(HealCapability, bloomelle).heal("itself and others"))

    def test_trans(trans_ctr_fac: TransformCreatureFactory) -> None:
        print("\nTesting Creature with transform capability")
        print(" base:")
        shiftling: Creature = trans_ctr_fac.create_base()
        print(shiftling.describe())
        print(shiftling.attack())
        print(cast(TransformCapability, shiftling).transform())
        print(shiftling.attack())
        print(cast(TransformCapability, shiftling).revert())
        print(" evolved")
        morphagon: Creature = trans_ctr_fac.create_evolved()
        print(morphagon.describe())
        print(morphagon.attack())
        print(cast(TransformCapability, morphagon).transform())
        print(morphagon.attack())
        print(cast(TransformCapability, morphagon).revert())

    test_heal(heal_ctr_fac)
    test_trans(trans_ctr_fac)
