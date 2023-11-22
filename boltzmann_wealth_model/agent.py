# Libraries
from mesa import Agent


class MoneyAgent(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.max_take_money = 10

    def step(self):
        other_agent = self.random.choice(self.model.schedule.agents)
        money_to_take = self.random.randrange(self.max_take_money)

        available_to_take = other_agent.wealth

        if available_to_take >= money_to_take:
            other_agent.wealth -= money_to_take
            self.wealth += money_to_take
        else:
            # take all they have
            self.wealth += other_agent.wealth
            other_agent.wealth = 0

