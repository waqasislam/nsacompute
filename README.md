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
from nsacompute.Skeleton import Decoder
# Decode a random set of hash bytes from NSA.
sets = Decoder.read("numbers.csv")
print(sets.values)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
