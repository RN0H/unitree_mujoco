#!/usr/bin/env python3
"""
Shows how to toss a capsule to a container.
"""


import os
import math
import pdb
from typing import Tuple
from envs import A1
from app.mujoco_app import MujocoAppWrapper
from configs.defs import RobotConfig


def main():
    
    robot = MujocoAppWrapper(RobotBaseClass = A1.A1)
    while True:
        robot.step()
        if os.getenv('TESTING') is not None:
            break


if __name__ == "__main__":
    main()  