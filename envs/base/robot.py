import os
from collections import OrderedDict
from gym import error, spaces
from gym.utils import seeding
import numpy as np
from os import path
import gym
import mujoco_py as mjpy

def convert_observation_to_space(observation):
    if isinstance(observation, dict):
        space = spaces.Dict(
            OrderedDict(
                [
                    (key, convert_observation_to_space(value))
                    for key, value in observation.items()
                ]
            )
        )
    elif isinstance(observation, np.ndarray):
        low = np.full(observation.shape, -float("inf"), dtype=np.float32)
        high = np.full(observation.shape, float("inf"), dtype=np.float32)
        space = spaces.Box(low, high, dtype=observation.dtype)
    else:
        raise NotImplementedError(type(observation), observation)

    return space


class Robot(gym.Env):
    """Superclass for robots"""

    def __init__(self, model_path, frame_skip=1):

        """
        Load model, and sim.
        """
        #TODO: check if path is valid
        if model_path.startswith("/"):
            resources_path = model_path
        else:
            base_env_path  = os.path.dirname(__file__)
            envs_path      = os.path.dirname(base_env_path)
            resources_path = os.path.join(os.path.dirname(envs_path), "resources", model_path)
        if not path.exists(resources_path):
            raise IOError("File %s does not exist" % resources_path)
        
        self.model      = mjpy.load_model_from_path(resources_path)
        self.frame_skip = frame_skip
        self.sim        = mjpy.MjSim(self.model)
        self.viewer     = mjpy.MjViewer(self.sim)


    def _simulation_step(self, ctrl=0, n_frames=1):
        self.sim.data.ctrl[:] = ctrl
        for _ in range(n_frames):
                self.sim.step()

    def _render(self):
        self.viewer.render()

    def _create_observation_space(self, observation):
        self.observation_space = convert_observation_to_space(observation)
        return self.observation_space

    def _create_action_space(self):
        bounds = self.model.actuator_ctrlrange.copy().astype(np.float32)
        low, high = bounds.T
        self.action_space = spaces.Box(low=low, high=high, dtype=np.float32)
        return self.action_space

    def _reset_model(self):
        pass

    @property
    def dt(self):
        pass


