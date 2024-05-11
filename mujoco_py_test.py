#!/usr/bin/env python3
"""
Shows how to toss a capsule to a container.
"""
from re import T
from mujoco_py import load_model_from_path, MjSim, MjViewer
import os
import math


def main():
    robot = "a1"
    model = load_model_from_path(f"resources/{robot}/xml/{robot}.xml")
    sim = MjSim(model)
    viewer = MjViewer(sim)
    sim_state = sim.get_state()
    while True:

        sim.step()
        viewer.render()
        
        if os.getenv('TESTING') is not None:
            break


if __name__ == "__main__":
    main()