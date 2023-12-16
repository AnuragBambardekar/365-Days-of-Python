import pygame
import random,math

pygame.init()

class DrawInformation:
    BLACK = 0,0,0,
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    GREY = 128,128,128
    BACKGROUND_COLOR = WHITE
    FONT = pygame.font.SysFont('comicsans',30)
    LARGE_FONT = pygame.font.SysFont('comicsans',40)

    GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst) -> None:
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2,5))

    controls = draw_info.FONT.render("R = Reset | SPACE = Start Solving | A = Ascending | D = Descending ", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2,55))

    sorting = draw_info.FONT.render("I = Insertion Sort | B = Bubble Sort | M = Merge Sort ", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2,90))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
                      draw_info.width - draw_info.SIDE_PAD, 
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i,val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i%3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x,y,draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        min_index = i

        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending):
                min_index = j

            draw_list(draw_info, {i: draw_info.RED, j: draw_info.GREEN, min_index: draw_info.GREEN}, True)
            yield True

        lst[i], lst[min_index] = lst[min_index], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED}, True)
        yield True

    return lst

def Bubble_Sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j+1:draw_info.RED}, True)
                yield True
    return lst

def Insertion_Sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1,len(lst)):
        current = lst[i]
        while True:
            ascending_sort = i>0 and lst[i-1] > current and ascending
            descending_sort = i>0 and lst[i-1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i-1]
            i=i-1
            lst[i]=current
            draw_list(draw_info, {i:draw_info.GREEN, i-1:draw_info.RED}, True)
            yield True
    return lst

def merge_sort(draw_info, ascending=True):
    def merge(lst, left, middle, right):
        left_list = lst[left:middle + 1]
        right_list = lst[middle + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_list) and j < len(right_list):
            if (left_list[i] <= right_list[j] and ascending) or (left_list[i] >= right_list[j] and not ascending):
                lst[k] = left_list[i]
                i += 1
            else:
                lst[k] = right_list[j]
                j += 1

            draw_list(draw_info, {k: draw_info.GREEN, left + i: draw_info.RED, middle + 1 + j: draw_info.RED}, True)
            yield True
            k += 1

        while i < len(left_list):
            lst[k] = left_list[i]
            draw_list(draw_info, {k: draw_info.GREEN, left + i: draw_info.RED}, True)
            yield True
            i += 1
            k += 1

        while j < len(right_list):
            lst[k] = right_list[j]
            draw_list(draw_info, {k: draw_info.GREEN, middle + 1 + j: draw_info.RED}, True)
            yield True
            j += 1
            k += 1

    def merge_sort_recursive(lst, left, right):
        if left < right:
            middle = (left + right) // 2

            yield from merge_sort_recursive(lst, left, middle)
            yield from merge_sort_recursive(lst, middle + 1, right)

            yield from merge(lst, left, middle, right)

    lst = draw_info.lst
    yield from merge_sort_recursive(lst, 0, len(lst) - 1)
    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n=50
    min_val = 0
    max_val = 100
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = Bubble_Sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60) # set speed

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting==False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = Insertion_Sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = Bubble_Sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_m and not sorting: 
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"

    pygame.quit()

if __name__ == "__main__":
    main()