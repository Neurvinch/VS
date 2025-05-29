import pandas as pd

from pgmpy.models import BayesianModel

from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator

from pgmpy.inference import VariavleElimination


url  =" ";

columns = ['A', 'B', 'C', 'D', 'E']

df =pd.read_csv(url, names = columns, na_values='?')

df = df.dropna()

df["A"] = pd.cut(df['A'], bin = 3, labels = ["a", "b", "c"])


model = BayesianModel([
    ("A",'target'),
    ("B",'target'),
]);


model.fit(df, estimator = MaximumLikelihoodEstimator)

inference = VariavleElimination(model)

query = inference.query(variables=['targer'], evidence={'age': 'a', 'cp':3})

print(query);
