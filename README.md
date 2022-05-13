# Modular Smartphone Scenario Data Dump

## About the scenario

The whole scenario is described [here](Specification%20Modular%20Smartphone%20Production%20Scenario.pdf).

The data is taken from a simulation of a minimized scenario (only the first production step and no product variants) that is further described [here](https://paul.ti.rw.fau.de/~pi69geby/2021/demoESWC/).

Furthermore a video of the simulation where the data is taken from can be seen [here](https://www.youtube.com/watch?v=kL57WT1qKdk) and the simulation can be replayed [here](https://paul.ti.rw.fau.de/~pi69geby/2021/demoESWC/gui/).

## The dump
The original RDF data is located in the `rdf/` folder. Each `.trig` file represents the simulation state at a time step.

`transform.py` is used to extract the relevant values using a SPARQL query, resulting in `dump_recipes_simulated_incorrectly.csv`.

The actual results can be seen in `dump.csv` where the column `memoryStorageStation1Recipe` has been manually corrected due to an error in the simulation regarding the active recipes.

## Acknoledgements
This work was funded by the German Federal Ministry of Education and Research through the MOSAIK project (grant no. 01IS18070A).