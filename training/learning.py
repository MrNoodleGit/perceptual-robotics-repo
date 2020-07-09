from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.base_env import *

env = UnityEnvironment(file_name=None, seed=1)

for i in range(15):
    behaviors = env.get_behavior_names()
    print(behaviors)
    try:
        print(env.get_behavior_spec(behaviors[0]))
        print(env.get_steps(behaviors[0])[0][0].obs)
    except: pass
    env.step()

env.close()
