from dataclasses import dataclass


@dataclass
class RobotConfig:
    robot : str = "b2w"

@dataclass
class EnvConfig:
    frame_skip : int = 1