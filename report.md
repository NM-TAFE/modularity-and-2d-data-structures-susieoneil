# Overview
Provides a report addressing the following questions:
- Justification for your refactoring decisions.
- The challenges you would have faced maintaining and testing the original monolithic code.
- How you would modify your refactored code to handle a custom-sized tic-tac-toe game (larger than 3x3), and how this implementation would be easier to handle than in the original code.

## Justification

I refactored the code into 3 modules and their corresponding classes following an MVC pattern. 
- A game module to handle the inputs and outputs
- A board module to handle the logic
- A player module to hold the player data. 

This provides the following benefits:
1. Each section of the code is reusable and separate from the other parts.
2. The code is more flexible with the use of parameters (size of board, player symbols, etc.)
3. Separate functions can be tested in isolation, which make errors easier to find and fix.

## Challenges of original code

Without the refactoring, the code would have faced the following challenges:
1. The whole game was a single script, which would run in its entirety upon import of the module. This is not ideal for re-usability.
2. The board was hard-coded to a certain size, which is not flexible.

## Handling Custom-Sized Tic-Tac-Toe

My implementation can handle custom sizes because:
1. The board class has a size attribute which can be changed by passing a new size as an argument.
2. The 2d data structure of the board is generated by the code based on the given size attribute.
3. The string representation of the board, which provides the visual grid, is likewise generated from the given size.

On the other hand, the original code could not handle custom sizes because:
1. The size of the board was hard-coded as a flat 9 element list.
2. The shape of the board was created only by print statements rather than a proper 2d data structure with rows and columns.
3. The win conditions were also hard-coded in a list of 9 tuples, but independent of the board.

## Conclusion

The activity allowed me to practice refactoring and to understand the benefits of object-oriented programming. I learned that:
1. Classes make code reusable and more easily imported. They also make visualising the concept of objects easier. 
2. Parameters/arguments allow for flexibility while still providing default values, which is preferable to hard-coding those values.
3. Exception reporting is a fantastic use of class inheritance.
4. Mutability/Immutability are important considerations when creating data structures due to the difference between pass-by-value and pass-by-reference.
5. Writing/testing/committing one function at a time makes development and refactoring more bearable.

I will apply this knowledge in future projects.

