import streamlit as st
import pandas as pd
import pyomo.environ as pyo
import pyomo.opt as opt
import plotly
import os
from pyutilib.services import register_executable, registered_executable
register_executable(name='glpsol')

st.write("Hello world!")

model = pyo.ConcreteModel()

model.x = pyo.Var([1,2], domain=pyo.NonNegativeReals)

model.OBJ = pyo.Objective(expr = 2*model.x[1] + 3*model.x[2])

model.Constraint1 = pyo.Constraint(expr = 3*model.x[1] + 4*model.x[2] >= 1)

st.write(type(model))


solver = "glpk"
optimizer = opt.SolverFactory() #solver

try:
    solver_info = optimizer.solve(model, tee=True)
    st.write(type(solver_info))
except Exception as e:
    st.write(e)
