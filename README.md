
# Count the Chord Intersections Inside a circle

A Python script to calculate the number of intersections of chords inside a circle.

## Overview

This script takes as input two lists: the list of radians for each chord's start and end points, and a list of identifiers for each point. It then calculates the total number of intersections between chords within the specified circle.

## Features

- **User Input Options**: Choose between updating input from a text file or providing input from the command prompt.

- **File Input**: If updating from a text file, the script reads the radians and identifiers from the 'input.txt' file.

- **Command Prompt Input**: If entering input from the command prompt, you can manually input the list of radians and identifiers.

- **Efficient Calculation**: The script uses NumPy for efficient array operations to determine chord intersections.

## Usage

To run the script, execute the following command in your terminal:

```bash
python main.py
```

Follow the prompts to choose input options and provide necessary input.

## Example

Suppose you have a set of chords defined by radians and identifiers your input text file should look like this:

```txt
[0.2, 1.5, 2.7, 4.3, 0.1, 3.0, 3.9, 5.2], ['s0', 'e0', 's1', 'e1', 's2', 'e2', 's3', 'e3']
```

Running the script with this input text would output the total number of chord intersections.

## Installation

1. Clone the repository:

```bash
https://github.com/Varunsaistark/ChordIntersectionDetectionStructify.git
cd ChordIntersectionDetectionStructify
```

2. Install required dependencies:

```bash
pip install numpy
```

3. Run the script:

```bash
python main.py
```

## Contribution

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or create a pull request.

## References

[Stack Overflow - Counting intersecting chords inside a circle](https://stackoverflow.com/questions/77901464/counting-intersecting-chords-inside-a-circle)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
