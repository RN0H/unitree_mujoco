from envs.base.robot import Robot


class B2W(Robot):

    def __init__(self, model_path, frame_skip=1):
        super().__init__(model_path, frame_skip)


    def _step(self):
        self._simulation_step()
        self._render()
    