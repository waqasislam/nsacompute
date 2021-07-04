# NSACompute

NSACompute is a libary designed to decode NSA signals and keys.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nsacompute.

```bash
pip3 install git+https://github.com/waqasislam/nsacompute.git --upgrade
```

## Usage
Example module (signal):
```python
#--IMPORTS
import nsacompute
# Decode a random set of hash bytes from NSA.
nsacompute.signal(['b7', 'fe', '88', 'a5', '37', 'c8', '7a', 'a5', '5c', 'e0'])

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
