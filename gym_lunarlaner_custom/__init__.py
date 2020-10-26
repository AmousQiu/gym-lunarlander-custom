from gym.envs.registration import register

register(
    id='LunarLanderCustom-v0'
    entry_point='gym_lunarlander_custom.envs:CustomLunarLanderEnv'
    max_episode_steps=200,
    reward_threshold=195.0,
)
