#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.Create_creature import Creature
from typing import Any
from ex1.Create_creature_2 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                f"for this normal strategy")
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                f"for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature) and isinstance(
            creature, TransformCapability
        )


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                f"for this defensive strategy")
        print(creature.attack())
        print(creature.heal("itself"))

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature) and isinstance(
            creature, HealCapability
        )
