#  RULES:
#  ********
# 1) Any live cell with <2 live neighbors dies (under population)
# 2) Any live cell with 2 or 3 live neighbors survives
# 3) Any live cell with >3 live neighbors dies (over population)
# 4) Any dead cell with 3 live neighbors gets reborn

import sys, pygame, random, tkinter

pygame.init()
pygame.font.init()

game_state = "menu"

root = tkinter.Tk()
root.title("Main Menu!")
root.geometry("800x800")
root.configure(bg="green")

mode_var = tkinter.StringVar(value="initialize") 

def Game_of_Life(width, height, mode):
    cell_size = 10
    board_size = (width * cell_size, height * cell_size)
    dead_color = (0, 0, 0)
    live_color = (255, 255, 255)

    screen = pygame.display.set_mode(board_size)
    pygame.display.set_caption("Conway's Game of Life!")

    grid = []
    num_cols = width
    num_rows = height
    Generation = 0

    def create_grid():
        rows = []
        for r in range(num_rows):
            list_of_columns = [0] * num_cols
            rows.append(list_of_columns)
        return rows

    grid.append(create_grid())
    grid.append(create_grid())
    active_grid = 0
    
    def set_grid_random(Grid=0):
        for r in range(num_rows):
            for c in range(num_cols):
                grid[Grid][r][c] = random.choice([0, 1])
                
    def set_grid_initial():
        setting = True
        while setting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    c = x // cell_size
                    r = y // cell_size
                    if 0 <= r < num_rows and 0 <= c < num_cols:
                        grid[0][r][c] = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        setting = False
            draw_grid()
        
    def clear_screen():
        screen.fill(dead_color)

    def draw_grid():
        clear_screen()
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[active_grid][r][c] == 1:
                    pygame.draw.rect(screen, live_color, (c * cell_size, r * cell_size, cell_size - 1, cell_size - 1))
        pygame.display.flip()

    def get_cell_value(r, c):
        if 0 <= r < num_rows and 0 <= c < num_cols:
            return grid[active_grid][r][c]
        return 0

    def check_neighbors(row_index, col_index):
        num_alive_neighbors = 0
        num_alive_neighbors += get_cell_value(row_index - 1, col_index - 1)
        num_alive_neighbors += get_cell_value(row_index - 1, col_index)
        num_alive_neighbors += get_cell_value(row_index - 1, col_index + 1)
        num_alive_neighbors += get_cell_value(row_index, col_index - 1)
        num_alive_neighbors += get_cell_value(row_index, col_index + 1)
        num_alive_neighbors += get_cell_value(row_index + 1, col_index - 1)
        num_alive_neighbors += get_cell_value(row_index + 1, col_index)
        num_alive_neighbors += get_cell_value(row_index + 1, col_index + 1)
        
        if grid[active_grid][row_index][col_index] == 1:
            if num_alive_neighbors < 2 or num_alive_neighbors > 3:
                return 0
            return 1  
        else:
            if num_alive_neighbors == 3:
                return 1 
            return 0
    
    def update_generation():
        nonlocal Generation, active_grid
        Generation += 1
        inactive_grid = (active_grid + 1) % 2
        
        for r in range(num_rows):
            for c in range(num_cols):
                grid[inactive_grid][r][c] = check_neighbors(r, c)
                
        active_grid = inactive_grid
        return Generation

    if mode == "randomize":
        set_grid_random(active_grid)
    else:  
        set_grid_initial()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.set_mode((1, 1), pygame.HIDDEN)
                running = False
                
        update_generation()
        draw_grid()
        clock.tick(10)

def start_game():
    global size_w_entry, size_h_entry
    w = int(size_w_entry.get())
    h = int(size_h_entry.get())
    
    mode = mode_var.get()
    
    root.withdraw()
    Game_of_Life(w, h, mode)
    root.deiconify()

def QUIT():
    quit()
    
def main_menu():
    global size_w_entry, size_h_entry
    
    title = tkinter.Label(root, text="Conway's Game of Life!", bg="black", fg="white", font=("Arial", 36, "bold"))
    title.pack(pady=50)
    universe_size = tkinter.Label(root, text="Size of universe: ", bg="yellow", font=("Arial", 25, "normal"))
    universe_size.place(x=100, y=150)
    mode = tkinter.Label(root, text="Initialize grid or randomize grid? ", bg="yellow", font=("Arial", 25, "normal"))
    mode.place(x=50, y=200)
    width_label = tkinter.Label(root, text="Width: ", bg="orange", font=("Arial", 15, "normal"))
    width_label.place(x=425, y=155)
    height_label = tkinter.Label(root, text="Height: ", bg="orange", font=("Arial", 15, "normal"))
    height_label.place(x=575, y=155)

    size_w_entry = tkinter.Entry(root, font=("Arial", 15), width=5)
    size_h_entry = tkinter.Entry(root, font=("Arial", 15), width=5)
    size_w_entry.place(x=500, y=150)
    size_h_entry.place(x=650, y=150)

    initialize_label = tkinter.Label(root, text="Initialize: ", bg="orange", font=("Arial", 15, "normal"))
    initialize_label.place(x=575, y=200)
    randomize_label = tkinter.Label(root, text="Randomize: ", bg="orange", font=("Arial", 15, "normal"))
    randomize_label.place(x=575, y=250)

    initialize_radio = tkinter.Radiobutton(root, variable=mode_var, value="initialize")
    initialize_radio.place(x=695, y=203)

    randomize_radio = tkinter.Radiobutton(root, variable=mode_var, value="randomize")
    randomize_radio.place(x=695, y=253)

    start = tkinter.Button(root, text="Start Simulation!", font=("Arial", 25), bg="red", fg="white", command=start_game)
    start.place(x=250, y=400)

    quit_button = tkinter.Button(root, text="Quit!", font=("Arial", 25), bg="blue", fg="white", command=QUIT)
    quit_button.place(x=325, y=500)
    
main_menu()
root.mainloop()
