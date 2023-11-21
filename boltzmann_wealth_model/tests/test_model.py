import pytest
from boltzmann_wealth_model.model import BoltzmannWealthModel


class TestBoltzmannWealthModel:
    """Tests for the BoltzmannWealthModel class."""

    def test_initialization(self):
        """Test if the BoltzmannWealthModel is initialized with correct parameters and state."""
        model = BoltzmannWealthModel(100, 10, 10)
        assert model.num_agents == 100
        assert model.grid.width == 10
        assert model.grid.height == 10

    # Initialization tests
    def test_initial_number_of_agents(self):
        """Test that all agents are added to the schedule"""
        # Placeholder

    def test_all_agents_on_grid(self):
        """Test that all agents have a place on the grid"""
        # Placeholder

    def test_equal_initial_wealth(self):
        """Test that after initialization each agent has the same amount of wealth."""
        # Placeholder

    # Step tests
    def test_constant_money(self):
        """Test if the amount of money stays constant during a step in the model."""
        # Placeholder

    def test_each_agent_moved(self):
        """Test if each agent moves during a step in the model."""
        # Placeholder

    def test_each_agent_gives_money_to_another_agent(self):
        """Test if each agent gives money to another agent (and not himself) during a step in the model."""
        # Placeholder

    def test_agent_count(self):
        """Test if the number of agents stays constant during a step in the model."""
        # Placeholder

    # Data collection tests
    def test_data_collection_length(self):
        """Test if the number of rows in the data collector dataframes is equal to the number of steps."""
        # Placeholder

    # Edge cases
    def no_negative_wealth(self):
        """Test that the wealth of each agent is never negative."""
        # Placeholder
