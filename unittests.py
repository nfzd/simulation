#!/usr/bin/env python3

import shutil
import tempfile
import unittest

from Simulation import Simulation


class TestCase(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_basic_runs(self):
        with Simulation(output_root=self.root) as sim:
            print()

        with Simulation(output_root=self.root, sim_name='test') as sim:
            print()

        with Simulation(output_root=self.root, suffix=dict(a=123, b='d')) as sim:
            print()

        with Simulation(output_root=self.root, numbered=False) as sim:
            print()

        with Simulation(output_root=self.root, catch_sigint=True) as sim:
            print()

        with Simulation(output_root=self.root):
            sim.save_data([1, 2, 3], 'test')

if __name__ == '__main__':
    unittest.main()
