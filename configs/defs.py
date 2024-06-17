from dataclasses import dataclass


@dataclass
class RobotConfig:
    robot : str = "a1"

@dataclass
class EnvConfig:
    frame_skip : int = 1