#!/usr/bin/env python3
import os
import importlib
from app.mujoco_app import MujocoAppWrapper
from configs.definitions import RobotConfig, EnvConfig


def main():
    
    robot_name = RobotConfig.robot  
    robot_path = f"envs.{robot_name}" 

    # Dynamically import the module and class
    try :
        module = importlib.import_module(robot_path)
    except Exception as e:
        print(f"Cannot import robot path {str(e)}")
        return 
    
    RobotClass = getattr(module, robot_name.upper())

    # Create instance and run
    robot = MujocoAppWrapper(RobotBaseClass=RobotClass)
    while True:
        robot.step()
        if os.getenv('TESTING') is not None:
            break
            
if __name__ == "__main__":
    
    main()  