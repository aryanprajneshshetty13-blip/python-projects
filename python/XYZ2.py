import turtle
import math
import random

# --- INTERACTIVE GLOBAL STATE VARIABLES ---
current_pitch = math.radians(30)
current_yaw = math.radians(45)
electron_time = 0.0  # Controls the continuous animation of orbiting electrons

# --- SYSTEM & GRAPHICS SETUP ---
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor('#08090a')  # Cosmic dark vacuum background
screen.colormode(255)
screen.tracer(0)  

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# --- PRE-CALCULATE NUCLEUS PARTICLES ---
# Protons (Red/Orange) and Neutrons (Blue/Cyan) packed into a central sphere
nucleus_particles = []
random.seed(42)  # Lock particle positions so they don't jitter randomly
for _ in range(40):
    # Spherical coordinate random distribution
    theta = random.uniform(0, 2 * math.pi)
    phi = random.acos(random.uniform(-1, 1))
    r = random.uniform(0, 35)  # Dense central packing radius
    
    nx = r * math.sin(phi) * math.cos(theta)
    ny = r * math.sin(phi) * math.sin(theta)
    nz = r * math.cos(phi)
    
    # FIXED: Added the list inside the brackets so it functions correctly
    p_type = random.choice([0, 1])
    nucleus_particles.append((nx, ny, nz, p_type))

# --- GENERATE ELECTRON ORBIT PATH VECTORS ---
# Defines the tilt and orientation planes of 4 distinct electron shells
orbit_planes = [
    (math.radians(0),   math.radians(0)),    # Flat horizontal plane
    (math.radians(60),  math.radians(30)),   # High angle cross tilt
    (math.radians(-60), math.radians(45)),   # Opposite deep cross tilt
    (math.radians(90),  math.radians(120))   # Vertical polar alignment
]

# --- MOUSE INTERACTION TRACKER ---
def handle_mouse_move(x, y):
    global current_pitch, current_yaw
    current_yaw = (x / 450.0) * math.pi
    current_pitch = (y / 450.0) * (math.pi / 2)

canvas = screen.getcanvas()
canvas.bind('<Motion>', lambda event: handle_mouse_move(event.x - 450, 450 - event.y))

# --- CORE 3D PROJECTOR FUNCTION ---
def project_3d(x3d, y3d, z3d, alpha, beta):
    """ Transforms 3D spatial vectors into 2D camera viewport pixels """
    # Pitch Matrix (X-axis)
    y1 = y3d * math.cos(alpha) - z3d * math.sin(alpha)
    z1 = y3d * math.sin(alpha) + z3d * math.cos(alpha)
    
    # Yaw Matrix (Y-axis)
    x2 = x3d * math.cos(beta) + z1 * math.sin(beta)
    z2 = -x3d * math.sin(beta) + z1 * math.cos(beta)
    
    # Camera distance perspective tracking
    distance = 6.0
    perspective = distance / (distance - (z2 / 150.0))
    
    screen_x = x2 * perspective
    screen_y = y1 * perspective
    return screen_x, screen_y, z2

# --- GENERATIVE ATOM RENDERING LOOP ---
def draw_frame():
    global electron_time
    t.clear()
    
    alpha = current_pitch  # Bound to Mouse Y
    beta = current_yaw    # Bound to Mouse X
    
    # --- STEP 1: PROJECT AND DRAW ELECTRON ORBIT RINGS ---
    for plane_idx, (tilt_x, tilt_z) in enumerate(orbit_planes):
        t.pensize(2)
        # Unique glowing color assignment per orbital track
        if plane_idx == 0: t.color(0, 255, 200)      # Aqua
        elif plane_idx == 1: t.color(255, 0, 255)    # Fuchsia
        elif plane_idx == 2: t.color(255, 255, 0)    # Neon Yellow
        else: t.color(0, 150, 255)                  # Electric Blue
        
        t.penup()
        for step in range(101):
            angle = (step * math.pi * 2) / 100
            ox = 220 * math.cos(angle)
            oy = 90 * math.sin(angle)
            oz = 0
            
            # Rotate target point directly into its designated orbital plane angle
            oy1 = oy * math.cos(tilt_x) - oz * math.sin(tilt_x)
            oz1 = oy * math.sin(tilt_x) + oz * math.cos(tilt_x)
            ox2 = ox * math.cos(tilt_z) + oz1 * math.sin(tilt_z)
            oz2 = -ox * math.sin(tilt_z) + oz1 * math.cos(tilt_z)
            
            sx, sy, _ = project_3d(ox2, oy1, oz2, alpha, beta)
            
            if step == 0: 
                t.goto(sx, sy)
                t.pendown()
            else: 
                t.goto(sx, sy)
            
    # --- STEP 2: CALCULATE ELECTRON POSITIONS ---
    render_queue = [] # Queue to process painter's sorting so depth is accurate
    
    for plane_idx, (tilt_x, tilt_z) in enumerate(orbit_planes):
        curr_angle = electron_time * (1.2 + plane_idx * 0.2)
        
        ex = 220 * math.cos(curr_angle)
        ey = 90 * math.sin(curr_angle)
        ez = 0
        
        # Apply plane transformations
        ey1 = ey * math.cos(tilt_x) - ez * math.sin(tilt_x)
        ez1 = ey * math.sin(tilt_x) + ez * math.cos(tilt_x)
        ex2 = ex * math.cos(tilt_z) + ez1 * math.sin(tilt_z)
        ez2 = -ex * math.sin(tilt_z) + ez1 * math.cos(tilt_z)
        
        sx, sy, sz = project_3d(ex2, ey1, ez2, alpha, beta)
        render_queue.append((sz, 'electron', sx, sy, plane_idx))

    # --- STEP 3: CALCULATE NUCLEUS POSITIONS ---
    for nx, ny, nz, p_type in nucleus_particles:
        sx, sy, sz = project_3d(nx, ny, nz, alpha, beta)
        render_queue.append((sz, 'nucleus', sx, sy, p_type))
        
    # --- STEP 4: DEPTH SORTING (PAINTER'S ALGORITHM) ---
    render_queue.sort(key=lambda item: item[0])
    
    # --- STEP 5: RASTERIZE ELEMENTS ONTO VIEWPORT ---
    for sz, item_type, sx, sy, variant in render_queue:
        t.penup()
        t.goto(sx, sy)
        
        depth_scale = max(3, int(12 + (sz / 35.0)))
        
        if item_type == 'nucleus':
            if variant == 0: # Proton
                t.color((240, 60, 60)) 
                t.dot(depth_scale + 4)
                t.color((255, 120, 120)) 
                t.dot(depth_scale // 2)
            else: # Neutron
                t.color((40, 140, 255)) 
                t.dot(depth_scale + 4)
                t.color((140, 200, 255)) 
                t.dot(depth_scale // 2)
                
        elif item_type == 'electron':
            t.pensize(1)
            if variant == 0: t.color(0, 255, 200)
            elif variant == 1: t.color(255, 0, 255)
            elif variant == 2: t.color(255, 255, 0)
            else: t.color(0, 150, 255)
            
            t.dot(depth_scale + 8) 
            t.color(255, 255, 255)
            t.dot(depth_scale + 2) 
            
    screen.update()
    electron_time += 0.08  
    screen.ontimer(draw_frame, 16)

# Start the interactive system loop
draw_frame()
turtle.done()
