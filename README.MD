# Python_OOP_Principles

Welcome to Python_OOP_Principles! This repository contains Python code examples that demonstrate key object-oriented programming (OOP) principles using movie-related classes.

## Overview

This repository serves as a resource for understanding fundamental OOP concepts through practical examples. The code focuses on illustrating how OOP principles can be applied in the context of movie classes.

## OOP Principles Demonstrated

The examples in this repository illustrate the following object-oriented programming (OOP) principles:

1. **Abstraction**: 
   - AbstractVideo class serves as an abstraction for video content, defining common methods such as `show_details()` and `play()`.
   - `show_details()` method is abstract in the AbstractVideo class, allowing concrete subclasses to provide their own implementation.

2. **Encapsulation**:
   - Private attributes such as `__director` in the Movie class are encapsulated to control access and modification, ensuring data integrity.

3. **Inheritance**:
   - Videoclip class inherits from the AbstractVideo class, inheriting its methods and behaviors.
   - Movie class inherits from the Videoclip class, extending its functionality with additional attributes and methods.

4. **Polymorphism**:
   - Polymorphism is demonstrated through method overriding, where the `show_details()` method is overridden in the Movie class to provide a specialized implementation.

## Contents

- `AbstractVideo`: Abstract class representing a video with methods for displaying details and playing.
- `Videoclip`: Concrete class implementing AbstractVideo for representing video clips.
- `Movie`: Concrete class extending Videoclip to represent movies, with additional attributes for genre, director, and actors.

## Usage

Feel free to explore the code examples provided in this repository to gain a better understanding of OOP principles applied to movie classes in Python.

To get started, you can clone this repository to your local machine using the following command:

