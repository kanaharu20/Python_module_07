#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy,
    InvalidStrategyError
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                fac_a, strat_a = opponents[i]
                fac_b, strat_b = opponents[j]
                crea = fac_a.create_base()
                creb = fac_b.create_base()
                print("* Battle *")
                print(crea.describe())
                print(" vs.")
                print(creb.describe())
                print(" now fight!")
                strat_a.act(crea)
                strat_b.act(creb)
                print()
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    def test() -> None:
        flame_fac: CreatureFactory = FlameFactory()
        aqua_fac: CreatureFactory = AquaFactory()
        heal_fac: CreatureFactory = HealingCreatureFactory()
        trans_fac: CreatureFactory = TransformCreatureFactory()
        nor_str: BattleStrategy = NormalStrategy()
        agr_str: BattleStrategy = AggressiveStrategy()
        def_str: BattleStrategy = DefensiveStrategy()

        print("Tournament 0 (basic)")
        print(" [ (Flameling+Normal), (Healing+Defensive) ]")
        battle([(flame_fac, nor_str), (heal_fac, def_str)])

        print("Tournament 1 (error)")
        print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
        battle([(flame_fac, agr_str), (heal_fac, def_str)])

        print("Tournament 2 (multiple)")
        print(
            " [ (Aquabub+Normal), (Healing+Defensive), "
            "(Transform+Aggressive) ]"
            )
        battle([
            (aqua_fac, nor_str),
            (heal_fac, def_str),
            (trans_fac, agr_str),
        ])

    test()
