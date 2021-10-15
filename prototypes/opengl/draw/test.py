from numpy.random import rand
import moderngl_window as mglw
import moderngl
import numpy as np
import time as t


class Example(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "ModernGL Example"
    window_size = (500, 500)
    aspect_ratio = 1 / 1
    resizable = True
    


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def run(cls):
        mglw.run_window_config(cls)

def point(coords: list, color: list, change: float):
    #[x,y,filler,filler]
    tmp = []
    tmp2 = []
    for x in color:
        tmp += [x/255]

    for n in range(int(len(coords)/2)):
        countCoords = 2*(n)
        countColor = 3*(n)
        tmp2 += [coords[0+countCoords],coords[1+countCoords],change,tmp[0+countColor],tmp[1+countColor],tmp[2+countColor]]


    return tmp2


def pointf(coords: list, color: list):
    #[x,y,filler,filler]
    tmp = []
    tmp2 = []
    for x in color:
        tmp += [x/255]

    for n in range(int(len(coords)/2)):
        countCoords = 2*(n)
        countColor = 3*(n)
        tmp2 += [coords[0+countCoords],coords[1+countCoords],tmp[0+countColor],tmp[1+countColor],tmp[2+countColor]]


    return tmp2


class Particles(Example):
    title = "Particle System (reverse engineered to become plotter)"
    gl_version = (3, 3)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec2 in_vert;
                in vec3 in_color;
                out vec3 color;

                void main() {
                    gl_Position = vec4(in_vert,0.0,1.0);
                    color = in_color;
                    
                }
            ''',
            fragment_shader='''
                #version 330
                out vec4 f_color;
                in vec3 color;
                void main() {
                    f_color = vec4(color, 1.0);
                }
            ''',
        )

        self.transform = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec3 in_vert;
                in vec3 in_color;

                out vec2 out_vert;
                out vec3 color;

                float change;

                void main() {
                    change = in_vert[2];
                    out_vert = vec2(in_vert[0]*sin(change),in_vert[1]*cos(change));
                    color = in_color;
                    
                }
            ''',
            varyings=['out_vert','color']
        )


        #add start pos the points to buffer
        #vbo -> vertex based object -> layer$
        self.color = [128, 255, 159]
        self.color2 = [128, 255, 200]
        tmp = []
        tmp2 = []
        self.dx = 500
        self.idx = 0
        self.change1 = 0
        self.change2 = 0
        self.centre = [0,0]

        for x in range(self.dx):
            tmp += [x/self.dx,x/self.dx]

        self.vbo1 = self.ctx.buffer(np.array(point(tmp * 2  , self.color * self.dx * 2, self.change1)).astype('f4'))
        self.vbo2 = self.ctx.buffer(reserve=self.vbo1.size)

        self.vao1 = self.ctx.simple_vertex_array(self.transform, self.vbo1, 'in_vert', 'in_color')
        
        self.prevState = [False]*2

        #append points to programm (vert shader)
        self.render_vao = self.ctx.vertex_array(self.prog, [
            (self.vbo2, '2f 3f', 'in_vert', 'in_color'),
        ])


        


    def render(self, time, frame_time):
        #sets bg color
        self.ctx.clear(0, 0, 0)
        #sets point size
        self.ctx.point_size = 1

        
        tmp = []
        tmp2 = []

        for x in range(self.dx):
            tmp += [x/self.dx, x/self.dx]




        #every frame execute write to buffer
        if self.wnd.frames % 1 == 0:
            self.vbo1.write(np.array(point(tmp , self.color * self.dx, self.change1)+point(tmp , self.color * self.dx, (self.change2))  ).astype('f4'))
        
        #every n seconds increment
        #used time module, since given time not accurate
        times = t.perf_counter()
        timesns = t.perf_counter_ns()
        #change increments in radians
        
        if times%1 < 0.01 and not self.prevState[0]:
            self.change1 += np.pi/12
            print(self.change1)
            self.prevState[0] = True

        elif times%1 > 0.01 and self.prevState[0]:
            self.prevState[0] = False

            
        if times%1 < 0.01 and not self.prevState[0]:
            self.change2 += np.pi/2
            self.prevState[1] = True

        elif times%1 > 0.01 and self.prevState[0]:
            self.prevState[1] = False
        
        print(timesns%100.0)
 
        
        

        #renders
        self.render_vao.render(moderngl.POINTS, self.dx*2)
        
        self.vao1.transform(self.vbo1, moderngl.POINTS, self.dx*2)
        self.ctx.copy_buffer(self.vbo2, self.vbo1)
        


if __name__ == '__main__':
    Particles.run()