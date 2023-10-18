# About pymunk

Pymunk is a popular 2D physics engine for Python that enables developers to simulate and interact with physics in their applications and games. It is a Python wrapper around the C-based physics engine Chipmunk, which is known for its efficiency and performance. Pymunk offers a user-friendly interface for creating and managing physics simulations in 2D space. 

Physical Objects:

**Body**: In Pymunk, a "body" represents an atom that is affected by physics. It can be thought of as a point mass with properties like mass, position, velocity, and more. Bodies are what you attach shapes to, and they interact with the simulated physics world.

**Shape**: A "shape" in Pymunk represents an area around a body that can collide with other shapes. Shapes are typically attached to bodies and are used to define the geometry of objects in the simulation. Shapes are responsible for handling collision detection and response.

**Space**: A "space" in Pymunk is the environment where all the physics simulations take place. It manages the simulation of physical objects, tracks their positions and interactions, and applies forces and constraints to them.
Gravity:

In Pymunk, you can set the gravity property of a space to define the gravitational force that affects objects within that space. The gravity vector is typically represented as a tuple (gx, gy), where gx is the horizontal component, and gy is the vertical component. Setting the gravity to (0, 500) in your code means that objects within the space will experience a vertical gravitational force of 500 units per second squared.

**Update**: The "update" operation in Pymunk typically refers to advancing the simulation by a small time step. In your code, you perform this update using the space.step(1/50) function. This function advances the simulation by a time step of 1/50 seconds, which is roughly 20 milliseconds. This allows Pymunk to calculate the new positions and velocities of physical objects based on the forces and constraints applied within the simulation.