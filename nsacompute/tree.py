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
    
def print_help(root, space, count=[10]):
    if root == None:
        return
    
    space += count[0]

    print_help(root.right, space)

    print()
    for i in range(count[0], space):
        print(end = " ")
    if (root.left == None) and (root.right == None):
        if root.leftbranch == True:
            print(f"Left Leaf -> Predicted Class: {root.predicted_class}, Samples: {root.samples}")
        if root.rightbranch == True:
            print(f"Right Leaf -> Predicted Class: {root.predicted_class}, Samples: {root.samples}")
    else:
        msg = f"X{root.feature_index}, Threshold: {root.threshold}, Predicted Class: {root.predicted_class}, Samples: {root.samples}"
        print(msg)

    print_help(root.left, space)


class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def print_tree(self):
        node = self.tree
        if node == None:
            return "Tree not fit yet"
        print_help(node, 0)
        return ""

    def fit(self, X:np.array, y:np.array):
        self.num_classes = len(np.unique(y))
        self.num_features = X.shape[1]
        self.tree = self.grow_tree(X, y)
		def _best_split(self, X, y):
        m = y.size
        if m <= 1:
            return None, None
        num_parent = [np.sum(y == c) for c in range(self.n_classes_)]
        best_gini = 1.0 - sum((n / m) ** 2 for n in num_parent)
        best_idx, best_thr = None, None
        for idx in range(self.n_features_):
            thresholds, classes = zip(*sorted(zip(X[:, idx], y)))
            num_left = [0] * self.n_classes_
            num_right = num_parent.copy()
            for i in range(1, m):
                c = classes[i - 1]
                num_left[c] += 1
                num_right[c] -= 1
                gini_left = 1.0 - sum(
                    (num_left[x] / i) ** 2 for x in range(self.n_classes_)
                )
                gini_right = 1.0 - sum(
                    (num_right[x] / (m - i)) ** 2 for x in range(self.n_classes_)
                )
                gini = (i * gini_left + (m - i) * gini_right) / m
                if thresholds[i] == thresholds[i - 1]:
                    continue
                if gini < best_gini:
                    best_gini = gini
                    best_idx = idx
                    best_thr = (thresholds[i] + thresholds[i - 1]) / 2
        return best_idx, best_thr

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
