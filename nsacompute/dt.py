import numpy as np
import warnings

class Node:
    def __init__(self, predicted_class, depth=None):
        self.predicted_class = predicted_class
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None
        self.leftbranch = False
        self.rightbranch = False
        self.depth = depth
class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X:np.array, y:np.array):
        self.num_classes = len(np.unique(y))
        self.num_features = X.shape[1]
        self.tree = self.grow_tree(X, y)
    #TODO: Loop through the X feature columns
    #Combine the X (a single column) and y data into a single matrix and sort them by the X value
    #Separate them again. The X values are now all the possible thresholds and the y values are the observed class of each row of data
    #Keep track of how many observations of each class are in the left and right node using num_left and num_right
    #Loop through the index of every observation in the data
    #Find the Gini impurity of the child nodes for each potential split and check if it’s smaller than the Gini impurity of the parent node. If it is, save it as the new best_gini and update ideal_col and ideal_threshold
    def find_split(self, X, y):
        ideal_col = None
        ideal_threshold = None
        num_observations = y.size
        if num_observations <= 1:
            return None, None

        y = y.reshape(num_observations,)

        with warnings.catch_warnings():
            warnings.filterwarnings(action='ignore', category=FutureWarning)
            count_in_parent = [np.count_nonzero(y == c) for c in range(self.num_classes)]

        best_gini = 1.0 - sum((n / num_observations) ** 2 for n in count_in_parent



    def grow_tree(self, X, y, depth=0):
        with warnings.catch_warnings():
            warnings.filterwarnings(action='ignore', category=FutureWarning)
            pop_per_class = [np.count_nonzero(y == i) for i in range(self.num_classes)]
        
        predicted_class = np.argmax(pop_per_class)

        node = Node(predicted_class=predicted_class,depth=depth)
        node.samples = y.size

        if depth < self.max_depth:
            col, threshold = self.find_split(X, y)
            if col and threshold:
                indices_left = X[:, col] < threshold
                X_left, y_left = X[indices_left], y[indices_left]
                indices_right = X[:, col] >= threshold
                X_right, y_right = X[indices_right], y[indices_right]
                node.feature_index = col
                node.threshold = threshold
                node.left = self.grow_tree(X_left, y_left, depth+1)
                node.left.leftbranch = True
                node.right = self.grow_tree(X_right, y_right, depth+1)
                node.right.rightbranch = True
        return node

    def _predict(self, X_test):

        node = self.tree
        predictions = []
        for obs in X_test:
            node = self.tree
            while node.left:
                if obs[node.feature_index] < node.threshold:
                    node = node.left
                else:
                    node = node.right
            predictions.append(node.predicted_class)
        return np.array(predictions)        
      

