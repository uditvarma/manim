from manim import *


class ManimLogo(Scene):
    def construct(self):
        # self.camera.background_color = "ffffff"
        logo_gr = "#88ccaa"
        logo_bl = "#555599"
        logo_rd = "#e07a55"
        logo_wt = "#dddddd"

        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_wt).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_gr, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_bl, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_rd, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)
        logo.move_to(ORIGIN)
        #self.add(logo)
        self.play(Write(logo))
        self.wait(5)
