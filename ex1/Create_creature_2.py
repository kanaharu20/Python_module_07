#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0 import CreatureFactory, Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._status: str

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        self._creature = Sproutling()
        return self._creature

    def create_evolved(self) -> Creature:
        self._evolved_creature = Bloomelle()
        return self._evolved_creature


class Sproutling(HealCapability, Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Sproutling"
        self._type = "Grass"

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self._name} heals {target} for a small amount"


class Bloomelle(HealCapability, Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Bloomelle"
        self._type = "Grass/Fairy"

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self._name} heals {target} for a large amount"


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        self._creature = Shiftling()
        return self._creature

    def create_evolved(self) -> Creature:
        self._evolved_creature = Morphagon()
        return self._evolved_creature


class Shiftling(TransformCapability, Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Shiftling"
        self._type = "Normal"
        self._status = "normal"

    def attack(self) -> str:
        if self._status == "normal":
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self._status = "sharper form"
        return f"{self._name} shifts into a {self._status}!"

    def revert(self) -> str:
        self._status = "normal"
        return f"{self._name} returns to {self._status}."


class Morphagon(TransformCapability, Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Morphagon"
        self._type = "Normal/Dragon"
        self._status = "its form"

    def attack(self) -> str:
        if self._status == "its form":
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._status = "dragonic battle form"
        return f"{self._name} morphs into a {self._status}!"

    def revert(self) -> str:
        self._status = "its form"
        return f"{self._name} stabilizes {self._status}."
