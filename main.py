from manim import *
from math import sqrt
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class AmpLaw(ThreeDScene, VoiceoverScene):
   def construct(self):
         self.set_speech_service(GTTSService())
         self.set_camera_orientation(phi=90*DEGREES, theta=-90*DEGREES, distance=10)

         #Mobjects/Groups
         infiniteWire1 = Cylinder(height=8, radius=1, fill_opacity=0.5, color=BLUE, direction=[0,1,0], show_ends=False)  # create a cylinder    
         infiniteWire2 = Cylinder(height=8, radius=1, fill_opacity=0.5, color=BLUE, direction=[0,1,0], show_ends=False)  # create a cylinder     
         infiniteWire3 = Cylinder(height=8, radius=1, fill_opacity=0.5, color=BLUE, direction=[0,1,0], show_ends=False)  # create a cylinder      
         wire = Cylinder(height=8, radius=1, fill_opacity=0.5, color=BLUE, direction=[0,1,0], show_ends=False)  # create a cylinder
         wireCap1 = Cylinder(height=0.01, radius=1, fill_opacity=0.25, color=BLUE, direction=[0,1,0])
         wireCap2 = Cylinder(height=0.01, radius=1, fill_opacity=0.25, color=BLUE, direction=[0,1,0])
         loop = Cylinder(height=0.05, radius=2, fill_opacity=0, color=WHITE)  # create a circle
         pointP = Dot3D(color=WHITE)
         current = Arrow3D(start=[0,-4,0], end=[0,-6,0], thickness=0.05, base_radius=0.1, height=0.5, color=WHITE)
         radiusArrow = Arrow3D(start=[0,0,0], end=[sqrt(2),0,sqrt(2)], thickness=0.05, base_radius=0.1, height=0.5, color=WHITE)
         texRadius = Tex("r", font_size=70)
         texCurrent = Tex("I", font_size=70)
         wireGroup = Group(wire, wireCap1, wireCap2, loop, pointP, current, texCurrent, radiusArrow, texRadius)
         radiusArrow2 = Arrow3D(start=[0,-8,0], end=[sqrt(0.125),-8,sqrt(0.125)], thickness=0.025, base_radius=0.05, height=0.25, color=WHITE)
         totalArrow = Arrow3D(start=[0,-8,0], end=[1,-8,0], thickness=0.025, base_radius=0.05, height=0.25, color=WHITE)
         texRadiusArrow2 = Tex("r", font_size=40)
         texTotalArrow = Tex("a", font_size=40)

         #creating infinite wire
         self.next_section(skip_animations=False)
         with self.voiceover(text="Let's assume we have an infinitely long current carrying wire."):
            wireCap1.move_to([0,-4,0])
            wireCap2.move_to([0,4,0])    
            infiniteWire1.move_to([0,8,0])
            infiniteWire2.move_to([0,16,0])
            infiniteWire3.move_to([0,24,0])
            self.add_fixed_in_frame_mobjects(texCurrent)
            texCurrent.shift(LEFT*3+DOWN*2)
            self.remove(texCurrent)
            self.play(FadeIn(wire, infiniteWire1, infiniteWire2, infiniteWire3, wireCap1, current))
            self.move_camera(phi=80*DEGREES, theta=-75*DEGREES, distance=10)
            self.wait(0.5)
            self.play(FadeIn(texCurrent))
         
         #infinite wire to part of wire
         self.next_section(skip_animations=False)
         with self.voiceover(text="However, let's cut it down to just a small piece for simplicity's sake."):
            self.play(FadeOut(infiniteWire1, infiniteWire2, infiniteWire3), FadeIn(wireCap2)) 
            self.wait(1)

         #showing magnetic field
         self.next_section(skip_animations=False)
         with self.voiceover(text="According to the Right Hand Rule, we can deduce that the magnetic field is revolving around the wire in a counterclockwise manner"):
            def spiral_function(t):
               x = 2*np.cos(3 * t)
               y = -0.5 * t
               z = 2*np.sin(3 * t)
               return np.array([x, y, z])
            spiral = ParametricFunction(spiral_function, t_range=[-2*TAU, 2 * TAU, 0.01], color=RED, stroke_width=2)
            self.play(Create(spiral))
            self.wait(3)

         #creating pointP
         self.next_section(skip_animations=False)
         with self.voiceover(text="Now we have a point named point P. And we want to find the magnetic field at point P, some distance away from the wire."):
            pointP.next_to(wire, RIGHT*7+UP*6)  # set the position
            self.play(FadeIn(pointP))
            self.play(pointP.animate.move_to([sqrt(2),0,sqrt(2)]), run_time=1)
            self.wait(1)
            self.play(FadeOut(spiral))

         #creating and centering circle
         self.next_section(skip_animations=False)
         with self.voiceover(text="Using Ampere's Law, we can place a loop that is concentric to the wire and line it up with point P"):
            loop.move_to(wire).rotate(axis=X_AXIS, angle=90*DEGREES)  # set the position
            self.play(FadeIn(loop))  # show the shapes on screen
            self.wait(1)

         #creating radius
         self.next_section(skip_animations=False)
         with self.voiceover(text="We'll call the distance from the wire to point P r, which is the same as the radius of the loop"):
            self.add_fixed_in_frame_mobjects(texRadius)
            texRadius.shift(UP*0.5)
            self.remove(texRadius)
            self.play(FadeIn(radiusArrow, texRadius))  # show the shapes on screen
            self.wait(1)

         #revolving around wire
         self.next_section(skip_animations=False)
         with self.voiceover(text="With this current setup, we can now perform Ampere's Law and derive the magnitude of magnetic field at point P"):
            self.play(FadeOut(texCurrent, texRadius))
            self.begin_ambient_camera_rotation(rate=30*DEGREES, about="theta")
            self.wait(4)
            self.stop_ambient_camera_rotation()

         #moving wire to left
         self.next_section(skip_animations=False)
         self.move_camera(phi=80*DEGREES, theta=-75*DEGREES, distance=10, run_time=3)
         self.play(FadeIn(texCurrent, texRadius))
         self.play(wireGroup.animate.shift(LEFT*3), run_time=2)

         #displaying Ampere's Law
         self.next_section(skip_animations=False)
         texTitle = MathTex(r"Ampere's Law", font_size=40)
         tex1 = MathTex(r"\oint_{}^{}\overrightarrow{B}\space\bullet\space d\overrightarrow{s}\space=\space\mu_oI_{total}", font_size=40)
         tex2 = MathTex(r"\oint_{}^{}\overrightarrow{B}\space\bullet\space d\overrightarrow{s}\space=\space\mu_oI", font_size=40)
         tex3 = MathTex(r"\overrightarrow{B}\oint_{}^{}d\overrightarrow{s}\space=\space\mu_oI", font_size=40)
         tex4 = MathTex(r"\overrightarrow{B}(2\pi r)\space=\space\mu_oI", font_size=40)
         tex5 = MathTex(r"\overrightarrow{B}\space=\space\frac{\mu_oI}{2\pi r}", font_size=70)

         texTitle.rotate(axis=X_AXIS, angle=90*DEGREES).rotate(axis=Z_AXIS, angle=15*DEGREES)
         tex1.rotate(axis=X_AXIS, angle=90*DEGREES).rotate(axis=Z_AXIS, angle=15*DEGREES)
         tex2.rotate(axis=X_AXIS, angle=90*DEGREES).rotate(axis=Z_AXIS, angle=15*DEGREES)
         tex3.rotate(axis=X_AXIS, angle=90*DEGREES).rotate(axis=Z_AXIS, angle=15*DEGREES)
         tex4.rotate(axis=X_AXIS, angle=90*DEGREES).rotate(axis=Z_AXIS, angle=15*DEGREES)
         tex5.rotate(axis=X_AXIS, angle=90*DEGREES).rotate(axis=Z_AXIS, angle=15*DEGREES)

         texTitle.shift(RIGHT*3+OUT*2)
         tex1.shift(RIGHT*3+OUT*2)
         tex2.shift(RIGHT*3+OUT*1)
         tex3.shift(RIGHT*3+OUT*0)
         tex4.shift(RIGHT*3+OUT*-1)
         tex5.shift(RIGHT*3+OUT*0.5)

         with self.voiceover(text="We'll begin with the basic formula for Ampere's Law, integral of B dot d A equals mu not times I total"):
            self.play(Write(texTitle))
            self.wait()
         with self.voiceover(text="We know that I is all the current enclosed within the loop so I total equals I"):
            self.play(Transform(texTitle, tex1))
            self.wait()
         with self.voiceover(text="We also know that the wire is concentric to the loop so magnetic field is constant throughout the loop so we can take it out of the integral"):
            self.play(Transform(tex1, tex2))
            self.wait()
         with self.voiceover(text="Now we integrate over d s which is simply the circumference of the loop or 2 pi r"):
            self.play(Transform(tex2, tex3))
            self.wait()
         with self.voiceover(text="With some simplification, we get our formula for magnetic field r distance away from an infinitely long current carrying wire"):
            self.play(Transform(tex3, tex4))
            self.wait()
            self.play(FadeOut(texTitle, tex1, tex2, tex3), ReplacementTransform(tex4, tex5))

         #scaling the wire
         self.next_section(skip_animations=False)
         with self.voiceover(text="Now let's consider that the wire has significant thickness and we want to find the magnetic field inside of it."):
            self.play(FadeOut(tex5))
            self.play(wireGroup.animate.shift(RIGHT*3), run_time=2)
            self.play(FadeOut(texRadius, radiusArrow, texCurrent, current))
            self.move_camera(phi=90*DEGREES, theta=-90*DEGREES, distance=5, run_time=2)
            self.add_fixed_in_frame_mobjects(texRadiusArrow2, texTotalArrow)
            self.remove(texRadiusArrow2, texTotalArrow)
            texRadiusArrow2.shift(LEFT*3.5+UP*0.5)
            texTotalArrow.next_to(LEFT*3.25+DOWN*0.25)
            self.play(wireCap1.animate.move_to([0,-8,0]), wireCap2.animate.move_to([0, 0, 0]), wire.animate.move_to([0, -4, 0]), loop.animate.move_to([0,-8,0]).scale(0.25), pointP.animate.move_to([sqrt(0.125),-8,sqrt(0.125)]))
         
         #Moving the wire
         self.next_section(skip_animations=False)
         self.play(FadeIn(radiusArrow2, totalArrow))
         self.play(wireCap1.animate.shift(LEFT*2), wireCap2.animate.shift(LEFT*2), wire.animate.shift(LEFT*2), loop.animate.shift(LEFT*2), radiusArrow2.animate.shift(LEFT*2), pointP.animate.shift(LEFT*2), totalArrow.animate.shift(LEFT*2))
         self.play(FadeIn(texRadiusArrow2, texTotalArrow))

         #displaying Ampere's Law
         self.next_section(skip_animations=False)
         texTitle2 = MathTex(r"Ampere's Law", font_size=40)
         tex6 = MathTex(r"\oint_{}^{}\overrightarrow{B}\space\bullet\space d\overrightarrow{s}\space=\space\mu_oI_{total}", font_size=40)
         tex7 = MathTex(r"\oint_{}^{}\overrightarrow{B}\space\bullet\space d\overrightarrow{s}\space=\space\mu_o\frac{Ir^2}{a^2}", font_size=40)
         tex8 = MathTex(r"\overrightarrow{B}\oint_{}^{}d\overrightarrow{s}\space=\space\frac{\mu_oIr^2}{a^2}", font_size=40)
         tex9 = MathTex(r"\overrightarrow{B}(2\pi r)\space=\space\frac{\mu_oIr^2}{a^2}", font_size=40)
         tex10 = MathTex(r"\overrightarrow{B}\space=\space\frac{\mu_oIr}{2\pi a^2}", font_size=70)
         tex11 = MathTex(r"I_{total}\neq I", font_size=40)
         tex12 = MathTex(r"I_{total}=J\space\bullet\space area", font_size=40)
         tex13 = MathTex(r"I_{total}=\frac{I}{\pi a^2}\space\bullet\space \pi r^2", font_size=40)
         tex14 = MathTex(r"I_{total}=\frac{Ir^2}{a^2}", font_size=40)

         texTitle2.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex6.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex7.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex8.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex9.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex10.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex11.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex12.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex13.rotate(axis=X_AXIS, angle=90*DEGREES)
         tex14.rotate(axis=X_AXIS, angle=90*DEGREES)

         texTitle2.shift(RIGHT*2.5+OUT*2)
         tex6.shift(RIGHT*2.5+OUT*2)
         tex7.shift(RIGHT*2.5+OUT*1)
         tex8.shift(RIGHT*2.5+OUT*0)
         tex9.shift(RIGHT*2.5+OUT*-1)
         tex10.shift(RIGHT*2.5+OUT*0.5)
         tex11.shift(LEFT*3.5+OUT*2.5)
         tex12.shift(LEFT*3.5+OUT*2.5)
         tex13.shift(LEFT*3.5+OUT*2.5)
         tex14.shift(LEFT*3.5+OUT*2.5)

         with self.voiceover(text="Again, we'll begin with the basic formula for Ampere's Law, integral of B dot d A equals mu not times I total"):
            self.play(Write(texTitle2))
            self.wait()
         with self.voiceover(text="But since we're now inside the wire, I total doesn't include all of I"):
            self.play(Write(tex11))
            self.wait()
         with self.voiceover(text="I total is going to be a fraction of the whole I which can be calculated with current density times area of our Amperian loop"):
            self.play(ReplacementTransform(tex11, tex12))
            self.wait()
         with self.voiceover(text="Current density is equal to I over the total area of the wire which is pi a squared"):
            self.play(ReplacementTransform(tex12, tex13))
            self.wait()
         with self.voiceover(text="Simplifying this down gives us our I total that is contained within the loop"):
            self.play(ReplacementTransform(tex13, tex14))
            self.wait()
         with self.voiceover(text="Now we can replace our I total with I r squared over a squared"):
            self.play(Transform(texTitle2, tex6))
            self.wait()
         with self.voiceover(text="Similarly, we also know that the wire is concentric to the loop so magnetic field is constant throughout the loop so we can take it out of the integral"):
            self.play(Transform(tex6, tex7))
            self.wait()
         with self.voiceover(text="Now we integrate over d s which is simply the circumference of the loop or 2 pi r"):
            self.play(Transform(tex7, tex8))
            self.wait()
         with self.voiceover(text="Finally, we get our formula for magnetic field r distance away within an infinitely long current carrying wire"):
            self.play(Transform(tex8, tex9))
            self.wait()
            self.play(FadeOut(texTitle2, tex6, tex7, tex8), ReplacementTransform(tex9, tex10))

         #showing the two final solutions and placing them
         self.next_section(skip_animations=False)
         tex5.rotate(axis=X_AXIS, angle=-90*DEGREES).rotate(axis=Z_AXIS, angle=2*DEGREES)
         tex5.shift(LEFT*0.5+UP*2.5)
         self.play(FadeOut(tex14, tex10, texRadiusArrow2, texTotalArrow, totalArrow, radiusArrow2, wireCap1, wireCap2, wire, loop, pointP))
         self.move_camera(phi=0*DEGREES, theta=-90*DEGREES, distance=5, run_time=0.5)
         tex10.shift(LEFT*5+UP*2.5).rotate(axis=X_AXIS, angle=-90*DEGREES)
         with self.voiceover(text="Now we have our two solutions for magnetic field, we can create a graph to visual how magnetic field varies with distance or r"):
            self.play(FadeIn(tex5, tex10))

         #showing graph of the two solutions
         self.next_section(skip_animations=False)
         axes = Axes(x_range = [0, 6, 1], y_range = [0, 3, 1], 
                           x_length=6, y_length=3,
                           axis_config={"include_tip": False} 
                           )
         axis_labels = axes.get_axis_labels(x_label="r", y_label="B(r)")
         axis_r = MathTex(r"a", font_size=40)
         axis_r.shift(DOWN*2+LEFT*2)
         axis_max = MathTex(r"\frac{\mu_oI}{2\pi a}", font_size=40)
         axis_max.shift(LEFT*3.5)
         graph_vary1 = MathTex(r"r", font_size=40)
         graph_vary1.shift(LEFT*2.5+UP*0.5)
         graph_vary2 = MathTex(r"\frac{1}{r}", font_size=40)
         graph_vary2.shift(UP*0.5)
         graph = axes.plot(lambda x : 2*x if x<1 else 2/x, x_range = [0,6], color = WHITE)
         graphGroup = VGroup(axis_labels, axis_r, graph_vary1, graph_vary2, graph, axes)
         graphGroup.shift(DOWN*1)
         with self.voiceover(text="As we're inside the wire, or when r is less than a, magnetic field varies linearly with r. And as we're outsidee the wire, or when r is greater than a, the magnetic field varies by one over r"): 
            self.play(DrawBorderThenFill(axes), Write(axis_labels))
            self.play(Create(graph))
            self.play(FadeIn(axis_r, axis_max, graph_vary1, graph_vary2))

class BiotSavartLaw(ThreeDScene, VoiceoverScene):
   def construct(self):
      self.set_speech_service(GTTSService())
      self.set_camera_orientation(phi=90*DEGREES, theta=-90*DEGREES, distance=10)