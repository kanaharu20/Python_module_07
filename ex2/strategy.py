#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import cast
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is asked to act on an unsuitable Creature."""


class BattleStrategy(ABC):
    _label: str

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    def _check(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                f"for this {self._label} strategy")


class NormalStrategy(BattleStrategy):
    _label = "normal"

    def act(self, creature: Creature) -> None:
        self._check(creature)
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    _label = "aggressive"

    def act(self, creature: Creature) -> None:
        self._check(creature)
        tc = cast(TransformCapability, creature)
        print(creature.attack())
        print(tc.transform())
        print(creature.attack())
        print(tc.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    _label = "defensive"

    def act(self, creature: Creature) -> None:
        self._check(creature)
        hc = cast(HealCapability, creature)
        print(creature.attack())
        print(hc.heal("itself"))

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
