import pytest
from boltzmann_wealth_model.agent import MoneyAgent


class TestMoneyAgent:
    """Tests for the MoneyAgent class."""

    def test_initialization(self):
        """Test if a MoneyAgent is initialized with correct attributes."""
        agent = MoneyAgent(1, None)
        assert agent.unique_id == 1
        assert agent.wealth == 1

    # Movement and grid
    def test_new_position(self):
        """Test if the MoneyAgent's move method changes its position (and not stays the same)."""
        # Placeholder

    def test_movement_range(self):
        """Test if the MoneyAgent's move method doesn't move the agent more than one cell up and/or down."""
        # Placeholder

    def test_position_within_grid(self):
        """Test that the MoneyAgent's position is always within the grid bounds."""
        # Placeholder

    # Money
    def test_give_money(self):
        """Test if the MoneyAgent's give_money method correctly transfers wealth to another agent."""
        # Placeholder

    def test_receive_money(self):
        """Test if an agent correctly receives wealth from another agent."""
        # Placeholder

    def test_dont_give_without_money(self):
        """Test if an agent doesn't give money if it doesn't have any."""
        # Placeholder
