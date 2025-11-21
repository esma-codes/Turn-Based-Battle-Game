# Python OOP: Turn-Based RPG Battle Simulator

This project is a console-based, turn-based battle game created in Python. It serves as a practical application of core Object-Oriented Programming (OOP) principles, moving beyond simple list management to simulate direct interaction between objects and manage their internal state.

A `Player` object and a `Monster` object take turns attacking each other until one's health drops to zero.

## 🚀 Core Features

* **Turn-Based Combat:** A main game loop (`while True`) manages the flow of the battle, giving the player and the monster turns to act.
* **Player Actions:** The player can choose between a standard `attack` or a more powerful, resource-consuming `cast_spell`.
* **State Management:** The game actively tracks the `health` of both combatants and ends when one `is_alive()` method returns `False`.
* **Object-Driven Logic:** The `Game` class doesn't calculate damage; it *delegates* actions. It tells the `Player` object *who* to attack, and the objects handle the interaction themselves.

## 💻 OOP Concepts Mastered in This Project

This project was specifically designed to master object interaction and state management.

1.  **Inheritance (IS-A Relationship)**:
    * A parent `Character` class defines the "blueprint" for all living entities. It holds common attributes (`name`, `health`, `attack_power`) and common methods (`attack()`, `take_damage()`, `is_alive()`).
    * Child classes, `Player` and `Monster`, inherit from `Character` using `super()`.
    * They **extend** the parent's functionality:
        * `Player` adds new attributes (`mana`) and new methods (`cast_spell()`).
        * `Monster` adds new attributes (`species`).

2.  **Composition (HAS-A Relationship)**:
    * This is the core of the game engine's design. The `Game` class is not a `Character`; it *has-a* (or owns) a `Player` object and a `Monster` object.
    * In `game.py`, the `__init__` method creates these instances:
        * `self.player = Player(...)`
        * `self.monster = Monster(...)`

3.  **Direct Object Interaction & Delegation**:
    * This was the main challenge. Instead of managing a list, objects talk directly to each other.
    * When the `Game` loop runs `self.player.attack(self.monster)`, the `Player` object is given a *direct reference* to the `Monster` object.
    * The `Player`'s `attack()` method then *delegates* the damage by calling the `take_damage()` method *on the `Monster` object*. (e.g., `target.take_damage(self.attack_power)`).

4.  **Polymorphism**:
    * The `attack()` and `take_damage()` methods are defined in the parent `Character` class.
    * This allows the `Player` to attack a `Monster`, and the `Monster` to attack a `Player`, using the *exact same* `attack()` method, even though they are different child classes.

