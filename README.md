# NSACompute

NSACompute is a libary designed to make computations easier using neural networks and GPU accelerated math. This is a python port of [bitcompute](https://github.com/drivevio/bitcompute) by DRIVEVIO however with added support and feature.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nsacompute.

```bash
pip3 install git+https://github.com/waqasislam/nsacompute.git --upgrade
```

## Usage
Example module (Adding negative numbers):
```python
#--IMPORTS
from nsacompute.Skeleton import Math
# *** Add negative numbers ***
sum = Math.addNegativeNumbers(["-12","-14"])
print(sum)
#--OUTPUT: -26

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
