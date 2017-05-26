#!/usr/local/bin/python3

# ---------------------------------------------------------------------------------------------------------------------
#
#                                        Bioinformatics Research Group
# 									        http://biorg.cis.fiu.edu/
#                             			Florida International University
#
#   This software is a "Camilo Valdes Work" under the terms of the United States Copyright Act.
#   Please cite the author(s) in any work or product based on this material.
#
#   OBJECTIVE:
#   The purpose of this program is to...
#
#   NOTES:
#   Please see the dependencies section below for the required libraries (if any).
#
#   DEPENDENCIES:
#
#       • somePythonModule (http://url_for_module.org)
#
#   The above libraries & modules are required. You can check the modules currently installed in your
#   system by running: python -c "help('modules')"
#
#   USAGE:
#   Run the program with the "--help" flag to see usage instructions.
#
#   AUTHOR:	Camilo Valdes (cvalde03@fiu.edu)
#           Bioinformatics Research Group,
#           School of Computing and Information Sciences,
#           Florida International University (FIU)
#
#
# ---------------------------------------------------------------------------------------------------------------------

# 	Python Modules
import numpy as np

class Perceptron(object):
    """Perceptron Classifier.
        This module implements the Perceptron Learning algorithm.

        Parameters:
            eta : float Learning rate (between 0.0 and 1.0)
            n_iter : int Number of passes over the entire dataset (epochs).

        Attributes:
            w_ : 1-d array and the weights after fitting.
            errors_ : list Number of misclassifications in every epoch.
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        Fits the training data.
        :param X:   {array-like}, shape = [n_samples, n_feature] Training vectors, where n_samples is the number of
                    samples and n_features is the number of features.
        :param y:   array-like, shape = [n_samples] Target values.
        :return: self : object
        """

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):

            errors = 0

            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)

            self.errors_.append(errors)

        return self

    def net_input(self, X):
        """
        Calculates the Net Input for a given neuron.
        :param X:
        :return:
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """
        Return class label after unit step.
        :param X:
        :return:
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)

