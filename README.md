# 8lang

This is a spatial esoteric programming language, very much inspired by [Arrows](https://github.com/JohnathonNow/arrows-esolang).

The source code, a normal ascii file, is treated like a 2 dimensional array of commands that threads move around.  A few test scripts are included.

## Details

  - **Threads** are the main "units" of computation.  They move around the source code, and at any time, have a
    - Velocity (up, down, left, or right).  Starts as right.
    - Value (currently positive or negative, but that is subject to change).  Starts as 0.
    - Location (x, y).  Starts as (0, 0).

  - **Steps**: each thread is moved/advanced in its direction, then the command underneath it is interpreted.  Any newly created threads are not advanced the step they are created.

  - **Halting**: The program halts when any program exits the program, with the value of the exiting thread.  If multiple threads exit in one step, don't rely on that.  *Note*, the program is right padded by spaces on the lines that are shorter than the longest line, to make source a little more manageable.

  - **Commands** are as follows:
    - All of `\/_|` change the direction of the thread in the way that light would reflect off that angled surface.
      - For example, a thread moving right, hitting `\`, would then move down.
      - A thread moving right, `|`, would then move left.
      - A thread moving up, `|`, would continue moving up.
    - All of `<^v>` do nothing unless the thread is moving towards the "pointy" side.  In that case, the thread is duplicated, so that the two threads are moving in the two directions perpindicular to the original direction
    - The thread passes through `#` if it's value is 0, turns left (from its perspective) if it is positive, and right if negative.
    - `+` and `-` increment and decrement the thread's value, respectively.
    - `,` reads a character as ascii into the thread's value.  If the end of file is found, the thread's value is made 0.
    - `.` prints the thread's value as an ascii character.
    - `T` *is not yet implemented*, but will likely facilitate interactions between threads.

## Theory
I am not yet sure what class of languages 8lang recognizes.  [Jeffrey](https://github.com/JohnathonNow) and I were talking about this.  It seems without the `T` command, nothing more than regular languages can be recognized.  With `T` we aren't sure, but it doesn't seem turing complete.  I'll try and update this if I find more on this.

However, for this purpose I think we will count a nonzero return value as accepting, and zero as rejecting.

## Todo
  - [ ] Organize code into modules more
  - [ ] Implement `T`, or similar
  - [ ] Make a compiler(?)
