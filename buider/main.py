from os.path import join
from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()

print("Building for Greycode IoT Platform (ESP32-WROOM-32)")
