# simulation

A simple simulation handler for Python.

Usage:

* Saving simulations in numbered subdirectories:

        with Simulation() as sim:
            # saves git state and all code files at simulation start
            # all output is logged
            pass

        with Simulation(suffix='name_of_this_run') as sim:
            # suffix string for numbered directory
            pass

        with Simulation(suffix=dict(param='value')) as sim:
            # suffix string is created from dict
            pass

* Saving simulations in unnumbered subdirectories:

        with Simulation(numbered=False, suffix=dict(param='value')) as sim:
            # subdirectory name is created from dict
            pass

* Saving data:

        with Simulation() as sim:
            print(sim.outdir)  # simulation directory

            sim.save_data([1, 2, 3])  # save as data.pkl
            sim.save_data([1, 2, 3], 'file_name')  # save as data_file_name.pkl

            # can also save to hdf5

* Catching SIGINT:

        with Simulation(catch_sigint=True) as sim:
            while True:
                pass

                if sim.received_sigint:
                    break
