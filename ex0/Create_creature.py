#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self._name: str
        self._type: str

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Aquabub"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Torragon"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"


class CreatureFactory(ABC):
    def __init__(self) -> None:
        self._creature: Creature
        self._evolved_creature: Creature

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        self._creature = Flameling()
        return self._creature

    def create_evolved(self) -> Creature:
        self._evolved_creature = Pyrodon()
        return self._evolved_creature


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        self._creature = Aquabub()
        return self._creature

    def create_evolved(self) -> Creature:
        self._evolved_creature = Torragon()
        return self._evolved_creature
