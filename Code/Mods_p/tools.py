import pygame
from os.path import dirname, abspath
from sys import path
BASE_PATH = dirname(dirname(abspath(__file__)))
path.append(BASE_PATH)
from entity import Entity