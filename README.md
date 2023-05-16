# pokemon_inheritance
Inheritance example using Pokemon types [OOP lesson]

# Pokemon Battle Simulator

This is a simple Python program that simulates a battle between two Pokémon. It defines two classes, `Pokemon` and `BugType`,
which represent different types of Pokémon and their attributes. The program demonstrates the usage of inheritance and polymorphism 
in object-oriented programming.

## Usage

To run the program, ensure that you have Python installed on your system. Save the code in a file with a `.py` extension, 
such as `pokemon_battle.py`. Open a terminal or command prompt, navigate to the directory where the file is saved, and execute 
the following command:

```shell
python pokemon_battle.py
```

The program will simulate a battle between a regular Pokémon and a Bug-type Pokémon. It will display the initial stats of each 
Pokémon and simulate their attacks. The output will show the updated stats after each attack.

## Code Explanation

The code begins with an import statement to import the `random` module, which is used to determine the probability of 
certain events.

### Class Definitions

1. `Pokemon` Class:
   - This class represents a basic Pokémon and has the following attributes:
     - `name`: The name of the Pokémon.
     - `trainer`: The name of the trainer who owns the Pokémon.
     - `level`: The level of the Pokémon.
     - `hp`: The hit points (health) of the Pokémon.
     - `paralyzed`: A boolean indicating if the Pokémon is paralyzed or not.
   - The class defines the following methods:
     - `__init__(self, name, trainer)`: Initializes a new instance of the `Pokemon` class with the provided name and trainer.
     - `__str__(self)`: Returns a string representation of the Pokémon, including its name, trainer, level, HP, and paralysis status.
     - `speak(self)`: Returns a string representing the Pokémon's speech.
     - `attack(self, other)`: Simulates an attack by the Pokémon on another Pokémon. It prints the Pokémon's speech and the attack used and returns a string representation of the attack. It also calls the `receive_damage` method on the target Pokémon.
     - `receive_damage(self, damage)`: Reduces the Pokémon's HP by the specified amount of damage. If the HP reaches 0, it returns a string indicating that the Pokémon has fainted.

2. `BugType` Class (Inherits from `Pokemon`):
   - This class represents a Bug-type Pokémon and inherits from the `Pokemon` class. It adds the following attributes:
     - `basic_attack`: The basic attack of the Bug-type Pokémon.
     - `probability`: The probability of inflicting confusion on the opponent.
     - `confusion`: A boolean indicating if the Pokémon is confused or not.
   - The class overrides the following methods from the `Pokemon` class:
     - `__init__(self, name, trainer, hp)`: Initializes a new instance of the `BugType` class with the provided name, trainer, and HP.
     - `__str__(self)`: Returns a string representation of the Bug-type Pokémon, including its type, name, trainer, level, HP, and confusion status.
     - `attack(self, other)`: Simulates an attack by the Bug-type Pokémon on another Pokémon. It calls the `speak` method of the parent class, prints the attack used, and returns a string representation of the attack. It also calls the `receive_damage` method on the target Pokémon. If the attack is successful and the target is not a Bug-type Pokémon, it sets the target's `confusion` attribute to `True` and returns a string indicating that the target is confused.

### Example Usage

The code provides an example usage scenario at the end
