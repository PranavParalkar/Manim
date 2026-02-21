from manim import *
import numpy as np

class PerpendicularBisector(Scene):
    def construct(self):
        title = Text("Methods for obtaining perpendicular bisector", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Methods list
        method1 = Text("1) Folding of Cords", font_size=30).next_to(title, DOWN, buff=0.7).align_to(title, LEFT)
        method2 = Text("2) Drawing Fish Figure", font_size=30).next_to(method1, DOWN, buff=0.4).align_to(method1, LEFT)
        
        self.play(Write(method1))
        self.play(Write(method2))
        self.wait(2)
        
        # Part 1 Title
        part1_title = Text("1) Cord Folding / Folding of Cords", font_size=36, color=BLUE).to_edge(UP)
        
        self.play(ReplacementTransform(method1, part1_title), FadeOut(method2), FadeOut(title))
        
        # Step 1 Text
        step1_text1 = Text("Step 1: Take two points A and B represented in form of nails", font_size=24)
        step1_text2 = Text("along east-west direction to which cord is tied up.", font_size=24)
        step1_text3 = Text("The points A and B are present on a circular arc.", font_size=24)
        
        step1_group = VGroup(step1_text1, step1_text2, step1_text3).arrange(DOWN, aligned_edge=LEFT)
        step1_group.next_to(part1_title, DOWN, buff=0.5)
        
        self.play(Write(step1_group))
        self.wait(1)
 
        self.play(FadeOut(part1_title), FadeOut(step1_group))
        arc = ArcBetweenPoints(start=UP * 3, end=DOWN * 3, angle=5*PI/6, color=WHITE)

        point_A = Dot(arc.point_from_proportion(0.25), color=YELLOW)
        label_A = Text("A", font_size=24).next_to(point_A, LEFT + UP * 0.2)
        
        point_B = Dot(arc.point_from_proportion(0.75), color=YELLOW)
        label_B = Text("B", font_size=24).next_to(point_B, LEFT + DOWN * 0.2)
        cord = DashedLine(point_A.get_center(), point_B.get_center(), color=GREY)
        visual_group = VGroup(arc, point_A, label_A, point_B, label_B, cord)
        visual_group.move_to(ORIGIN)
        
        self.play(Create(arc))
        self.play(FadeIn(point_A), Write(label_A), FadeIn(point_B), Write(label_B))
        self.play(Create(cord))
        self.wait(2)
        
        # Step 2 Text
        step2_text1 = Text("Step 2: Take a rope which is twice the size of AB", font_size=24)
        step2_text2 = Text("and then mark the center of the free rope.", font_size=24)
        step2_text3 = Text("Do this by folding the rope.", font_size=24)
        
        step2_group = VGroup(step2_text1, step2_text2, step2_text3).arrange(DOWN, aligned_edge=LEFT)
        step2_group.to_corner(UL)
        
        self.play(Write(step2_group))
        self.wait(1)
        self.play(visual_group.animate.scale(0.6).shift(RIGHT * 2.5))
        
        # Step 2: Extract a copy of the dotted line AB
        pa_original = point_A.get_center()
        pb_original = point_B.get_center()

        point_A_copy = Dot(pa_original, color=YELLOW)
        point_B_copy = Dot(pb_original, color=YELLOW)
        label_A_copy = Text("A", font_size=24).next_to(point_A_copy, LEFT + UP * 0.2)
        label_B_copy = Text("B", font_size=24).next_to(point_B_copy, LEFT + DOWN * 0.2)
        cord_copy = DashedLine(pa_original, pb_original, color=GREY)
        
        rope_group = VGroup(cord_copy, point_A_copy, label_A_copy, point_B_copy, label_B_copy)
        self.play(FadeIn(rope_group))
        target_center = LEFT * 3.5 + DOWN * 0.5
        self.play(rope_group.animate.move_to(target_center))
        self.wait(0.5)
        self.play(FadeOut(step2_group))
        self.wait(0.5)
        self.play(FadeOut(label_A_copy), FadeOut(label_B_copy), FadeOut(point_A_copy), FadeOut(point_B_copy))

        self.play(cord_copy.animate.scale(2),run_time=1.5)
        self.wait(0.5)
        pa_new = cord_copy.get_start()
        pb_new = cord_copy.get_end()
        point_A_copy.move_to(pa_new)
        point_B_copy.move_to(pb_new)
    
        mid1 = pa_new * 0.75 + pb_new * 0.25 + RIGHT * 1.5
        mid2 = pa_new * 0.5 + pb_new * 0.5 + LEFT * 0.5
        mid3 = pa_new * 0.25 + pb_new * 0.75 + RIGHT * 1.5
        
        wavy_base = VMobject().set_style(stroke_width=4)
        wavy_base.set_points_smoothly([pa_new, mid1, mid2, mid3, pb_new])
        
        center_pos = wavy_base.point_from_proportion(0.5)
        wavy_rope = DashedVMobject(wavy_base, num_dashes=30, color=GREY)
        
        self.play(Transform(cord_copy, wavy_rope), run_time=1.5)
        self.wait(1)
        label_A_copy.next_to(point_A_copy, LEFT + UP * 0.2)
        label_B_copy.next_to(point_B_copy, LEFT + DOWN * 0.2)
        self.play(FadeIn(point_A_copy), FadeIn(point_B_copy), FadeIn(label_A_copy), FadeIn(label_B_copy))
        
        center_mark = Dot(center_pos, color=RED, radius=0.1)
        center_label = Text("Center", font_size=20, color=RED).next_to(center_mark, RIGHT)
        self.play(FadeIn(center_mark), Write(center_label))
        self.wait(1)
        
        full_wavy_group = VGroup(cord_copy, point_A_copy, point_B_copy, label_A_copy, label_B_copy, center_mark, center_label, wavy_rope)
        self.play(full_wavy_group.animate.shift(UP * 0.6))
        self.wait(1)
        
        step3_center = RIGHT * 2.5
        
        self.play(FadeOut(visual_group), full_wavy_group.animate.move_to(step3_center), run_time=1)
        self.wait(1)
        
        # Step 3 Text
        step3_text1 = Text("Step 3: Pull the Curved Rope such that ", font_size=24)
        step3_text2 = Text("One side is north and other side is south.", font_size=24)
        step3_text3 = Text(" This gives the perpendicular to the east-west axis, ", font_size=24)
        step3_text4 = Text("passing through the center.", font_size=24)
        step3_group = VGroup(step3_text1, step3_text2, step3_text3, step3_text4).arrange(DOWN, aligned_edge=LEFT)
        step3_group.to_corner(UL)
        
        self.play(Write(step3_group))
        self.wait(1)
    
        original_AB_len = np.linalg.norm(pb_original - pa_original)
        ew_axis_len = original_AB_len
        
        east_pos = step3_center + RIGHT * ew_axis_len / 2
        west_pos = step3_center + LEFT * ew_axis_len / 2
        
        h_dist = original_AB_len * np.sqrt(3) / 2
        north_pos = step3_center + UP * h_dist
        south_pos = step3_center + DOWN * h_dist
        
        point_A_copy.set_z_index(2)
        point_B_copy.set_z_index(2)
        center_mark.set_z_index(2)
        
        pulled_rope = VGroup(
            DashedLine(west_pos, north_pos, color=GREY, z_index=0),
            DashedLine(north_pos, east_pos, color=GREY, z_index=0),
            DashedLine(east_pos, south_pos, color=GREY, z_index=0),
            DashedLine(south_pos, west_pos, color=GREY, z_index=0)
        )
        
        self.play(
            point_A_copy.animate.move_to(west_pos),
            label_A_copy.animate.next_to(west_pos, LEFT),
            point_B_copy.animate.move_to(east_pos),
            label_B_copy.animate.next_to(east_pos, RIGHT),
            Transform(wavy_rope, pulled_rope),
            Transform(cord_copy, pulled_rope), 
            center_mark.animate.move_to(step3_center),
            center_label.animate.next_to(step3_center, DOWN+RIGHT, buff=0.1),
            run_time=2
        )
        self.wait(1)
        ew_axis = Line(west_pos + LEFT * 0.8, east_pos + RIGHT * 0.8, color=RED).set_z_index(-1)
        ew_label_e = Text("E", font_size=20).next_to(ew_axis, RIGHT)
        ew_label_w = Text("W", font_size=20).next_to(ew_axis, LEFT)
        
        ns_axis = Line(north_pos + UP * 0.8, south_pos + DOWN * 0.8, color=BLUE).set_z_index(-1)
        ns_label_n = Text("N", font_size=20).next_to(ns_axis, UP)
        ns_label_s = Text("S", font_size=20).next_to(ns_axis, DOWN)
        
        north_mark = Dot(north_pos, color=YELLOW).set_z_index(2)
        south_mark = Dot(south_pos, color=YELLOW).set_z_index(2)
        
        point_A_copy.set_z_index(2)
        point_B_copy.set_z_index(2)
        center_mark.set_z_index(2)
        
        self.play(Create(ew_axis), Write(ew_label_e), Write(ew_label_w),FadeIn(north_mark), FadeIn(south_mark))
        self.play(Create(ns_axis), Write(ns_label_n), Write(ns_label_s))
        self.wait(2)
        
        # --- Part 2: Fish Figure Method ---
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        part2_title = Text("2) Drawing Fish Figure", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(part2_title))

        fish_text1 = Text("Create two circular arcs from two points (N and S).", font_size=24)
        fish_text2 = Text("With an appropriate radius (greater than half the distance),", font_size=24)
        fish_text3 = Text("the intersections will give the perpendicular bisector line EW.", font_size=24)
        
        fish_group = VGroup(fish_text1, fish_text2, fish_text3).arrange(DOWN, aligned_edge=LEFT)
        fish_group.next_to(part2_title, DOWN, buff=0.5)
        
        self.play(Write(fish_group))
        self.wait(2)
        
        self.play(FadeOut(fish_group), FadeOut(part2_title))

        dist_NS = 5.0
        fish_radius = 3.5
        center_offset = UP * 0.6
        
        n_pos = center_offset + UP * (dist_NS / 2)
        s_pos = center_offset + DOWN * (dist_NS / 2)
        
        axis_ns = Line(n_pos + UP * 0.5, s_pos + DOWN * 0.5, color=BLUE)
        
        n_dot = Dot(n_pos, color=YELLOW, z_index=2)
        s_dot = Dot(s_pos, color=YELLOW, z_index=2)
        
        n_label = Text("N", font_size=24).next_to(n_dot, UP + RIGHT, buff=0.1)
        s_label = Text("S", font_size=24).next_to(s_dot, DOWN + RIGHT, buff=0.1)
        
        self.play(Create(axis_ns), FadeIn(n_dot), FadeIn(s_dot), Write(n_label), Write(s_label))
        self.wait(1)
        

        arc_n = Arc(radius=fish_radius, angle=2*PI/3, start_angle=-5*PI/6, arc_center=n_pos, color=GOLD, stroke_width=2)
        arc_s = Arc(radius=fish_radius, angle=2*PI/3, start_angle=PI/6, arc_center=s_pos, color=GOLD, stroke_width=2)
        
        self.play(Create(arc_n), run_time=1.5)
        self.play(Create(arc_s), run_time=1.5)
        self.wait(1)
        
        # Math: circle equation x^2 + y^2 = R^2 if at origin.
        # By symmetry, intersection y = 0.
        # x = sqrt(R^2 - y_dist^2)
        int_x = np.sqrt(fish_radius**2 - (dist_NS / 2)**2)
        e_pos = center_offset + RIGHT * int_x
        w_pos = center_offset + LEFT * int_x
        
        e_dot = Dot(e_pos, color=YELLOW, z_index=2)
        w_dot = Dot(w_pos, color=YELLOW, z_index=2)
        
        bisector_ew = Line(w_pos + LEFT * 0.8, e_pos + RIGHT * 0.8, color=RED, z_index=1)
        e_label = Text("E", font_size=24).next_to(bisector_ew, RIGHT)
        w_label = Text("W", font_size=24).next_to(bisector_ew, LEFT)
        
        self.play(FadeIn(e_dot), FadeIn(w_dot))
        
        final_text1 = Text("The line passing through the intersection of the", font_size=24)
        final_text2 = Text("two arcs gives the east-west direction.", font_size=24)
        final_group = VGroup(final_text1, final_text2).arrange(DOWN)
        final_group.to_edge(DOWN, buff=0.5)
        
        self.play(
            Create(bisector_ew), 
            Write(e_label), 
            Write(w_label),
            Write(final_group)
        )
        
        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
        
        # --- Bodhayana's Method of Constructing a square ---
        
        # Main Title
        bod_title = Text("Bodhayana's Method of Constructing a square", font_size=36, color=ORANGE).to_edge(UP)
        self.play(Write(bod_title))
        self.wait(1)
        
        # Step 1 Text
        bod_step1_text2 = Text("Rope will have two end points P and Q.", font_size=24)
        bod_step1_text1 = Text("Step 1 : Take rope same as side of square you want.", font_size=24)
        bod_step1_group = VGroup(bod_step1_text2, bod_step1_text1).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bod_step1_group.to_corner(UL).shift(DOWN * 0.5)
        
        self.play(Write(bod_step1_group))
        self.wait(1)
        
        rope_len = 2.5
        center_offset = RIGHT * 3.0
        p_pos = center_offset + UP * (rope_len / 2)
        q_pos = center_offset + DOWN * (rope_len / 2)
        
        rope_pq = Line(p_pos, q_pos, color=BLUE)
        
        p_dot = Dot(p_pos, color=YELLOW)
        q_dot = Dot(q_pos, color=YELLOW)

        p_label = Text("P", font_size=24).next_to(p_dot, LEFT)
        q_label = Text("Q", font_size=24).next_to(q_dot, LEFT)
        
        self.play(Create(rope_pq))
        self.play(
            FadeIn(p_dot), Write(p_label),
            FadeIn(q_dot), Write(q_label),
        )
        self.wait(1)
        self.play(FadeOut(bod_title), FadeOut(bod_step1_group))
        self.wait(1)
        
        # Step 2
        bod_step2_text1 = Text("Step 2: Take mid point of PQ as O and fix a nail,", font_size=24)
        bod_step2_text2 = Text("draw a circle with radius as PO.", font_size=24)
        bod_step2_group = VGroup(bod_step2_text1, bod_step2_text2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bod_step2_group.to_corner(UL).shift(DOWN * 0.5)
        
        self.play(Write(bod_step2_group))
        self.wait(1)
        
        o_pos = center_offset
        o_dot = Dot(o_pos, color=RED)
        o_label = Text("O", font_size=24).next_to(o_dot, LEFT)
        
        self.play(FadeIn(o_dot), Write(o_label))
        self.wait(1)
        
        radius_len = rope_len / 2
        h_rad_pos = o_pos + RIGHT * radius_len
        rad_line = Line(o_pos, h_rad_pos, color=BLUE)
        rad_dot = Dot(h_rad_pos, color=YELLOW)
        
        self.play(Create(rad_line), FadeIn(rad_dot))
        self.play(FadeOut(rope_pq))
        
        bod_circle = Circle(radius=radius_len, color=GREY).move_to(o_pos)
        self.play(Create(bod_circle), run_time=2)
        
        self.wait(2)
        
        # --- Step 3 ---
        bod_step3_text1 = Text("Step 3: Take PQ as the diameter. Place a nail at P ", font_size=20)
        bod_step3_text2 = Text("and a nail at Q, draw a circle with diameter PQ ", font_size=20)
        bod_step3_text3 = Text("from both points P and Q. Draw a inner circle which ", font_size=20)
        bod_step3_text4 = Text("tangents both P and Q. ", font_size=20)

        bod_step3_group = VGroup(bod_step3_text1, bod_step3_text2, bod_step3_text3, bod_step3_text4).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bod_step3_group.to_corner(UL).shift(DOWN * 0.5)
        
        self.play(ReplacementTransform(bod_step2_group, bod_step3_group))
        self.wait(1)
        
        circ_p = Circle(radius=rope_len, color=RED).move_to(p_pos)
        angle_p = PI/6
        rad_p_end = p_pos + np.array([np.cos(angle_p), np.sin(angle_p), 0]) * rope_len
        rad_p_line = Line(start=p_pos, end=rad_p_end, color=BLUE)
        rad_p_dot = Dot(rad_p_end, color=YELLOW)
        
        self.play(Create(rad_p_line), FadeIn(rad_p_dot))
        self.play(Create(circ_p), run_time=2)
        
        circ_q = Circle(radius=rope_len, color=RED).move_to(q_pos)
        rad_q_end = q_pos + DOWN * rope_len
        rad_q_line = Line(start=q_pos, end=rad_q_end, color=BLUE)
        rad_q_dot = Dot(rad_q_end, color=YELLOW)
        
        self.play(Create(rad_q_line), FadeIn(rad_q_dot))
        self.play(Create(circ_q), run_time=2)
        self.play(FadeOut(bod_step3_group), FadeOut(rad_p_line), FadeOut(rad_p_dot), FadeOut(rad_q_line), FadeOut(rad_q_dot))
        self.wait(1)
        
        # --- Step 4 ---
        bod_step4_text1 = Text("Step 4: Name two points E and F which are the ", font_size=20)
        bod_step4_text2 = Text("intersection of the circles drawn from P and Q. ", font_size=20)
        bod_step4_text3 = Text("While connecting the points E and F, name the ", font_size=20)
        bod_step4_text4 = Text("points R and S which will be intersection of the ", font_size=20)
        bod_step4_text5 = Text("inner circle and line EF.", font_size=20)

        bod_step4_group = VGroup(
            bod_step4_text1, bod_step4_text2, bod_step4_text3, bod_step4_text4, bod_step4_text5
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bod_step4_group.to_corner(UL).shift(DOWN * 0.5)

        self.play(Write(bod_step4_group))
        self.wait(1)

        e_pos = o_pos + LEFT * (np.sqrt(3) / 2) * rope_len
        f_pos = o_pos + RIGHT * (np.sqrt(3) / 2) * rope_len
        
        e_dot = Dot(e_pos, color=YELLOW)
        f_dot = Dot(f_pos, color=YELLOW)
        e_label = Text("E", font_size=24).next_to(e_dot, LEFT)
        f_label = Text("F", font_size=24).next_to(f_dot, RIGHT)

        self.play(FadeIn(e_dot), Write(e_label), FadeIn(f_dot), Write(f_label))
        
        line_ef = Line(e_pos, f_pos, color=BLUE)
        self.play(Create(line_ef))
        
        r_pos = o_pos + LEFT * (rope_len / 2)
        s_pos = o_pos + RIGHT * (rope_len / 2)
        
        r_dot = Dot(r_pos, color=RED)
        s_dot = Dot(s_pos, color=RED)
        r_label = Text("R", font_size=24).next_to(r_dot, UP+LEFT, buff=0.1)
        s_label = Text("S", font_size=24).next_to(s_dot, UP+RIGHT, buff=0.1)

        self.play(FadeIn(r_dot), Write(r_label), FadeIn(s_dot), Write(s_label))
        self.wait(1)

        # --- Step 5 ---
        bod_step5_text1 = Text("Step 5: Fix nail at P, R, S, Q. Draw circles from ", font_size=20)
        bod_step5_text2 = Text("all 4 points wherever any two of circles intersect", font_size=20)
        bod_step5_text3 = Text(" make a point A,B,C,D. Connect all the intersecting", font_size=20)
        bod_step5_text4 = Text(" points of circle to finally draw a square named ABCD.", font_size=20)

        bod_step5_group = VGroup(
            bod_step5_text1, bod_step5_text2, bod_step5_text3, bod_step5_text4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bod_step5_group.to_corner(UL).shift(DOWN * 0.5)

        self.play(FadeOut(bod_step4_group))
        self.play(Write(bod_step5_group))
        self.wait(1)

        dashed_circ_p = DashedVMobject(Circle(radius=rope_len/2, color=GRAY).move_to(p_pos))
        dashed_circ_q = DashedVMobject(Circle(radius=rope_len/2, color=GRAY).move_to(q_pos))
        dashed_circ_r = DashedVMobject(Circle(radius=rope_len/2, color=GRAY).move_to(r_pos))
        dashed_circ_s = DashedVMobject(Circle(radius=rope_len/2, color=GRAY).move_to(s_pos))

        self.play(
            Create(dashed_circ_p), 
            Create(dashed_circ_q),
            Create(dashed_circ_r),
            Create(dashed_circ_s),
            run_time=3
        )

        a_pos = o_pos + UP * (rope_len/2) + LEFT * (rope_len/2)
        b_pos = o_pos + UP * (rope_len/2) + RIGHT * (rope_len/2)
        c_pos = o_pos + DOWN * (rope_len/2) + RIGHT * (rope_len/2)
        d_pos = o_pos + DOWN * (rope_len/2) + LEFT * (rope_len/2)

        a_dot = Dot(a_pos, color=YELLOW)
        b_dot = Dot(b_pos, color=YELLOW)
        c_dot = Dot(c_pos, color=YELLOW)
        d_dot = Dot(d_pos, color=YELLOW)

        a_label = Text("A", font_size=24).next_to(a_dot, UP+LEFT, buff=0.1)
        b_label = Text("B", font_size=24).next_to(b_dot, UP+RIGHT, buff=0.1)
        c_label = Text("C", font_size=24).next_to(c_dot, DOWN+RIGHT, buff=0.1)
        d_label = Text("D", font_size=24).next_to(d_dot, DOWN+LEFT, buff=0.1)

        self.play(
            FadeIn(a_dot), Write(a_label),
            FadeIn(b_dot), Write(b_label),
            FadeIn(c_dot), Write(c_label),
            FadeIn(d_dot), Write(d_label),
        )

        square = Polygon(a_pos, b_pos, c_pos, d_pos, color=GREEN)
        self.play(Create(square), run_time=2)

        self.wait(2)
        
        elements_to_fade = [
            circ_p, circ_q, bod_circle, o_dot, o_label,
            e_dot, e_label, f_dot, f_label, line_ef,
            r_dot, r_label, s_dot, s_label,
            dashed_circ_p, dashed_circ_q, dashed_circ_r, dashed_circ_s,
            p_dot, p_label, q_dot, q_label, bod_step5_group, rad_line, rad_dot
        ]
        self.play(*(FadeOut(mob) for mob in elements_to_fade))
        self.wait(1)

        square_group = VGroup(
            square,
            a_dot, a_label, b_dot, b_label,
            c_dot, c_label, d_dot, d_label
        )
        
        self.play(square_group.animate.move_to(ORIGIN))
        self.wait(1)

        #THANK YOU
        thank_you_text = Text("THANK YOU!", font_size=48, color=GOLD)
        self.play(ReplacementTransform(square_group, thank_you_text))

        self.wait(3)
