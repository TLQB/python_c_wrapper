# Powake Project

## Overview

The Powake Project is a Python-based module that integrates with a C extension to provide functionality for license verification and execution of specific functions. This project demonstrates how to use Python's import system to override and extend module functionalities with C implementations.

## Components

### Python Modules

- **powake_loader.py**: This module contains a custom loader and finder to intercept the import of the `powake` module. It overrides the `add_license` and `func` functions with implementations from the C extension.

- **powake.py**: A placeholder module that defines the `add_license` and `func` functions, which are overridden by the loader.

- **test.py**: A test script that demonstrates the usage of the `powake` module by adding a license and calling the `func` function.

### C Extension

- **powake_impl.c**: A C extension that provides the actual implementation of the `add_license` and `func` functions. It checks the validity of a license key and prints "Hello World" if the license is valid.

## Installation

1. Compile the C extension:
   ```bash
   python setup.py build_ext --inplace
   python setup.py develop --user
   ```

2. Ensure that the compiled extension is available in the Python path.

## Usage

1. Import the `powake_loader` to set up the custom import mechanism:
   ```python
   from powakes import powake_loader
   ```

2. Use the `powake` module as follows:
   ```python
   import powake

   powake.add_license("ABC123-XYZ789")
   powake.func()
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

