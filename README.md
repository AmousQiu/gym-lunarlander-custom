<!--
 * @Author: your name
 * @Date: 2020-11-04 14:52:08
 * @LastEditTime: 2020-11-04 14:55:58
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \gym-lunarlander-custom\README.md
-->
# Custom Lunar Lander
Modified version of OpenAI Gym Lunar Lander environment(https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py) to be able to adjust the initial height.

For installation instructions see https://github.com/openai/gym/blob/master/docs/creating-environments.md

## Install this environment

- Clone this repository
- Install Package: pip install -e gym-lunar-lander-custom
- Python3
>> import gym
>> env = gym.make('gym_lunarlander_custom:CustomLunarLander-v0')

## Example using this environment
python train.py --env gym_lunarlander_custom:CustomLunarLander-v0 --verbose true
