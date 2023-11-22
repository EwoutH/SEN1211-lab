from boltzmann_wealth_model.model import BoltzmannWealthModel

# Initialize model
test_model = BoltzmannWealthModel(100, 10, 10)
# Run the model for n steps
n_steps = 100
test_model.run_model(n_steps)
