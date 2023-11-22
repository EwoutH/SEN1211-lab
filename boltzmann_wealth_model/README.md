## Boltzmann Wealth Model Description
A simple model of agents exchanging wealth. All agents start with the same amount of money. Every step, each agent with one unit of money or more gives one unit of wealth to another random agent.

This is a starter-level simulated agent-based economy. In an agent-based economy, the behavior of an individual economic agent, such as a consumer or producer, is studied in a market environment.
This model is drawn from the field econophysics, specifically a paper prepared by Drăgulescu et al. for additional information on the modeling assumptions used in this model. [Drăgulescu, 2002].

The assumption that govern this model are:

1. There are some number of agents.
2. All agents begin with 1 unit of money.
3. At every step of the model, an agent gives 1 unit of money (if they
   have it) to some other agent.

As the model runs, the distribution of wealth among agents goes from being perfectly uniform (all agents have the same starting wealth), to highly skewed -- a small number have high wealth, more have none at all.

Even as a starter-level model the yielded results are both interesting and unexpected to individuals unfamiliar with it the specific topic. As such, this model is a good starting point to examine Mesa's core features.

#### Sources
- This model is taken from the [mesa-examples](https://github.com/projectmesa/mesa-examples/tree/main/examples/boltzmann_wealth_model) repository.
- It's described further in the [Introductory Tutorial](https://mesa.readthedocs.io/en/latest/tutorials/intro_tutorial.html)

#### References
- [Dragulescu2002] Drăgulescu, Adrian A., and Victor M. Yakovenko. “Statistical Mechanics of Money, Income, and Wealth: A Short Survey.” arXiv Preprint Cond-mat/0211175, 2002. http://arxiv.org/abs/cond-mat/0211175.
