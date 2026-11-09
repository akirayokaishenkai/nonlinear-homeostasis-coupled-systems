# Resource-Agent Dynamics: Topological Invariance & Phase Inversion

This repository contains the core numerical simulation script for the coupled non-linear ordinary differential equations (ODEs) derived in the manuscript: *"Topological Invariance, Phase Inversion, and Boundary Extinction in Coupled Resource-Agent Non-Linear Dynamical Systems"*.

The system maps the continuous-time feedback loop between a Resource Field potential ($x$) and an autonomous self-replicating Agent Population ($y$), modulated by a directional parity operator $\sigma = \pm 1$.

## Features
- Complete continuous integration utilizing `scipy.integrate.solve_ivp`.
- Exact mapping of Forward (Growth) and Inverse (Dissipation) phase space trajectories.
- Geometric marking of the Invariant Neutral Point equilibrium at $P^* = (1.50, 5.83)$.
- Formal identification of boundary extinction conditions.
