from envs.base.robot import Robot


class GO1(Robot):

    def __init__(self, model_path, frame_skip=1):
        super().__init__(model_path, frame_skip)

    def __str__(self):
        return super().__str__()

    def _step(self):
        self._simulation_step()
        self._render()
    