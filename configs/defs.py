from dataclasses import dataclass



@dataclass
class EnvConfig:
    num_envs : int = 10


@dataclass
class RobotConfig:
    robot : str = "a1"
    
