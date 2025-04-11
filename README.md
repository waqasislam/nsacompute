# NSACompute
# Library is no longer being maintained
NSACompute is a libary designed to make computations easier using neural networks and GPU accelerated math. It also is a framework to send hardware interface commands to a raspberry pi or arduino for
electronic engineering. This is a python port of [bitcompute](https://github.com/drivevio/bitcompute) by DRIVEVIO however with added support and feature.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nsacompute.

```bash
pip3 install git+https://github.com/waqasislam/nsacompute.git --upgrade
```

## Usage
Example of using a decision tree classifier with a .csv file.
```python
from nsacompute.tree import DecisionTree
import pandas as pd
tree = DecisionTree(max_depth=5)
csv = pd.read_csv("example.csv")
X = csv.drop(columns=['genre'])
y = csv['genre']
tree.fit(X,y)
predictions = tree.predict([ [21,0], [23,1]])
print(predictions)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
