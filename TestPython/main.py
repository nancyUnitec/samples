
from sklearn import linear_model
from sklearn import cross_validation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cost_and_click=pd.DataFrame(pd.read_excel('cost_and_click.xlsx'))

cost_and_click.head()
