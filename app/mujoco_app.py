import envs
from envs.base.robot import Robot
from configs.defs import RobotConfig, EnvConfig


def MujocoAppWrapper(RobotBaseClass):
    model_path = f"{RobotConfig.robot}/xml/{RobotConfig.robot}.xml"
    class MujocoApp(RobotBaseClass):
        def __init__(self, model_path, frame_skip=1):
            super().__init__(model_path, frame_skip)
        def create_robot(self):
            pass
        def step(self):
            self._step()
            pass
    return MujocoApp(model_path, EnvConfig.frame_skip)



