# flowtools

For more detailed documentation, please see our  
[GitHub Pages](TODO).

## Installation

To install from `GitHub`, open a new terminal and type:

```sh
pip3 install git+https://github.com/ahill187/flowtools#egg=flowtools
```

If you want to develop this package, please see the installation instructions for
developers below.

## Developers

### Installation

```sh
git clone https://github.com/ahill187/flowtools
cd flowtools
pip install -e ".[dev]"
```

### Testing

To run the test suite, from the `flowtools` root directory, type in a shell terminal:

```sh
cd flowtools
pytest tests/
```

To run a specific test file:

```sh
pytest tests/test_flow_data.py
```

To run a specific test in a file, use the `-k` flag:

```sh
pytest tests/test_flow_data.py -k test_flow_data_read_fcs
```

### Distribution Wheel

```sh
cd flowtools
python3 setup.py bdist_wheel
```

### Documentation

This project is documented using `Sphinx` documentation. To modify the documentation,
see the `docs` folder. To build the documentation:

```sh
cd flowtools/docs
make clean
make html
```

This will create a `build` folder containing the `HTML` files. Open up the `index.html` file
in your browser to view the documentation.
