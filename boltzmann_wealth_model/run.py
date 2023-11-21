from boltzmann_wealth_model.model import BoltzmannWealthModel

# Initialize model
test_model = BoltzmannWealthModel(5, 10, 10)
# Run the model for 3 steps
test_model.run_model(3)
