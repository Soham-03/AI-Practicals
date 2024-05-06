from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 2: Define the network structure
model = BayesianModel([('Burglary', 'Alarm'), 
                       ('Earthquake', 'Alarm'), 
                       ('Alarm', 'JohnCalls'), 
                       ('Alarm', 'MaryCalls')])

# Step 3: Define the Conditional Probability Tables (CPTs)
cpd_b = TabularCPD(variable='Burglary', variable_card=2, values=[[0.99], [0.01]])
cpd_e = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])

# Alarm depends on both Burglary and Earthquake
cpd_a = TabularCPD(variable='Alarm', variable_card=2,
                   values=[[0.999, 0.71, 0.06, 0.05],    # Probability Alarm is off
                           [0.001, 0.29, 0.94, 0.95]],   # Probability Alarm is on
                   evidence=['Burglary', 'Earthquake'],
                   evidence_card=[2, 2])

# JohnCalls and MaryCalls depend on the status of the Alarm
cpd_j = TabularCPD(variable='JohnCalls', variable_card=2, values=[[0.95, 0.1], [0.05, 0.9]], evidence=['Alarm'], evidence_card=[2])
cpd_m = TabularCPD(variable='MaryCalls', variable_card=2, values=[[0.99, 0.3], [0.01, 0.7]], evidence=['Alarm'], evidence_card=[2])

# Step 4: Add CPDs to the model
model.add_cpds(cpd_b, cpd_e, cpd_a, cpd_j, cpd_m)

# Validate the model
assert model.check_model()

# Step 5: Perform inference
inference = VariableElimination(model)
result = inference.query(variables=['Burglary'], evidence={'JohnCalls': 1, 'MaryCalls': 1})

print(result)