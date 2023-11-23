from model import BoltzmannWealthModel
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize model
test_model = BoltzmannWealthModel(5, 10, 10)
# Run the model for 3 steps
test_model.run_model(3)


def hisplot():
    agent_data = test_model.datacollector.get_agent_vars_dataframe()
    sns.histplot(agent_data)


if __name__ == "__main__":
    hisplot()