from manim import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle()  
               
        self.play(Create(circle), run_time=2)