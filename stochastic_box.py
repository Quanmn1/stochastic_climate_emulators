import numpy as np
import scipy
from matplotlib import pyplot as plt
import math

"""
Stochastic simulation of a few coupled boxes.
The state of the boxes is stored in vector "state".
Evolution: response * state + forcing
Numerical integration: Euler method (?)
"""

num_components = 3
rng = np.random.default_rng()

# couplings
def response(state, time):
    pass

# deterministic forcings
def deterministic_forcing(state, time):
    pass

# random forcings: gaussian white noise
def stochastic_forcing(amplitude, state, time):
    noise = rng.normal(0, 1, size=num_components)

# stopping condition: final time
def stopping_condition(state, time):
    pass

def step(dt, state, t):
    new_state = state + response(state, t) @ state * dt + deterministic_forcing(state, t) * dt \
                + stochastic_forcing(dt, state, t)


def run(dt, initial_state, initial_time, stopping_condition):
    state = initial_state
    t = initial_time
    states = [initial_state]
    ts = [initial_time]
    noise_amplitude = math.sqrt(dt)
    while not stopping_condition(state, t):
        t, state = step(dt, state, t)
        states.append(state)
        ts.append(t)
    
    states = np.array(states)
    # plot
    for component in range(num_components):
        plt.plot(ts, states[component, :])

