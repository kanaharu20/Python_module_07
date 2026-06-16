#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0 import CreatureFactory, FlameFactory, AquaFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory


class BattleStrategy(ABC):
    @abstractmethod
    def act():
        ...

    @abstractmethod
    def is_valid() -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, factory: CreatureFactory) -> bool:
        return isinstance(factory, (AquaFactory, FlameFactory))


class AgressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, factory: CreatureFactory) -> bool:
        return isinstance(factory, TransformCreatureFactory)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())
        print(creature.heal("itself"))

    def is_valid(self, factory: CreatureFactory) -> bool:
        return isinstance(factory, HealingCreatureFactory)
