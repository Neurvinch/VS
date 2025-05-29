import pandas as pd

from pgmpy.models import BayesianModel

from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator

from pgmpy.inference import VariavleElimination


url  =" ";

columns = ['A', 'B', 'C', 'D', 'E']

df =pd.read_csv(url, names = columns, na_values='?')