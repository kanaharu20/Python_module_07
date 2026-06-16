#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy, AgressiveStrategy, DefensiveStrategy
)

if __name__ == "__main__":
    def test() -> None:
        flame_fac: CreatureFactory = FlameFactory()
        aqua_fac: CreatureFactory = AquaFactory()
        heal_ctr_fac: CreatureFactory = HealingCreatureFactory()
        trans_ctr_fac: CreatureFactory = TransformCreatureFactory()
        nor_str: BattleStrategy = NormalStrategy()
        agr_str: BattleStrategy = AgressiveStrategy()
        def_str: BattleStrategy = DefensiveStrategy()
        print("Tournament 0 (basic)")
        print(" [ (Flameling+Normal), (Healing+Defensive) ]")
        print("*** Tournament ***\n2 opponents involved\n")
        print("* Battle *")
        print(flame_fac.create_base().describe())
        print(" vs.")
        print(heal_ctr_fac.create_base().describe())
        print(" now fight!")
        tournament0: list[tuple[CreatureFactory, BattleStrategy]] = [
            (flame_fac, nor_str),
            (heal_ctr_fac, def_str)
        ]
        try:
            for one_pair in tournament0:
                if one_pair[1].is_valid(one_pair[0]) is False:
                    raise TypeError(
                        "Battle error, aborting tournament: "
                        f"Invalid Creature '{one_pair[0].create_base()._name}'"
                        f" for this {one_pair[1].__class__.__name__}")
            for one_pair in tournament0:
                one_pair[1].act(one_pair[0].create_base())
            print()
        except TypeError as e:
            print(e)
        print("Tournament 1 (error)")
        print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
        print("*** Tournament ***\n2 opponents involved\n")
        print("* Battle *")
        print(flame_fac.create_base().describe())
        print(" vs.")
        print(heal_ctr_fac.create_base().describe())
        print(" now fight!")
        tournament1: list[tuple[CreatureFactory, BattleStrategy]] = [
            (flame_fac, agr_str),
            (heal_ctr_fac, def_str)
        ]
        try:
            for one_pair in tournament1:
                if one_pair[1].is_valid(one_pair[0]) is False:
                    raise TypeError(
                        "Battle error, aborting tournament: "
                        f"Invalid Creature '{one_pair[0].create_base()._name}'"
                        f" for this {one_pair[1].__class__.__name__}")
            for one_pair in tournament1:
                one_pair[1].act(one_pair[0].create_base())
            print()
        except TypeError as e:
            print(e)
        print("Tournament 2 (multiple)")
        print(
            " [ (Aquabub+Normal), (Healing+Defensive), "
            "(Transform+Aggressive) ]"
            )
        print("*** Tournament ***\n3 opponents involved\n")
        print("* Battle *")
        print(aqua_fac.create_base().describe())
        print(" vs.")
        print(heal_ctr_fac.create_base().describe())
        print(" now fight!")
        tournament2: list[tuple[CreatureFactory, BattleStrategy]] = [
            (aqua_fac, nor_str), (heal_ctr_fac, def_str)
        ]
        try:
            for one_pair in tournament2:
                if one_pair[1].is_valid(one_pair[0]) is False:
                    raise TypeError(
                        "Battle error, aborting tournament: "
                        f"Invalid Creature '{one_pair[0].create_base()._name}'"
                        f" for this {one_pair[1].__class__.__name__}")
            for one_pair in tournament2:
                one_pair[1].act(one_pair[0].create_base())
            print()
        except TypeError as e:
            print(e)
        print("* Battle *")
        print(aqua_fac.create_base().describe())
        print(" vs.")
        print(trans_ctr_fac.create_base().describe())
        print(" now fight!")
        tournament3: list[tuple[CreatureFactory, BattleStrategy]] = [
            (aqua_fac, nor_str), (trans_ctr_fac, agr_str)
        ]
        try:
            for one_pair in tournament3:
                if one_pair[1].is_valid(one_pair[0]) is False:
                    raise TypeError(
                        "Battle error, aborting tournament: "
                        f"Invalid Creature '{one_pair[0].create_base()._name}'"
                        f" for this {one_pair[1]().__class__.__name__}")
            for one_pair in tournament3:
                one_pair[1].act(one_pair[0].create_base())
            print()
        except TypeError as e:
            print(e)
        print("* Battle *")
        print(heal_ctr_fac.create_base().describe())
        print(" vs.")
        print(trans_ctr_fac.create_base().describe())
        print(" now fight!")
        tournament4: list[tuple[CreatureFactory, BattleStrategy]] = [
            (heal_ctr_fac, def_str),
            (trans_ctr_fac, agr_str)
        ]
        try:
            for one_pair in tournament4:
                if one_pair[1].is_valid(one_pair[0]) is False:
                    raise TypeError(
                        "Battle error, aborting tournament: "
                        f"Invalid Creature '{one_pair[0].create_base()._name}'"
                        f" for this {one_pair[1].__class__.__name__}")
            for one_pair in tournament4:
                one_pair[1].act(one_pair[0].create_base())
        except TypeError as e:
            print(e)

    test()
