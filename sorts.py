from pyqtgraph import BarGraphItem

import time

# Standard sorting algorithms, some differences to allow visualization
class Sort():
    check_color = '#E6E6E6'
    good_color = '#45D56D'
    swap_color = '#F74141'
    
    def __init__(self, sort_graph: BarGraphItem, graph_colors: dict()):
        self.sort_graph = sort_graph
        self.graph_colors = graph_colors

    def selection_sort_fn(self, arr):
        temp_colors = self.graph_colors.copy()
       
        arr_size = len(arr)
        sort_speed = 4 / arr_size
        
        for i in range(arr_size):
            temp_colors[i] = self.good_color
            
            min_index = i
            for j in range(i + 1, arr_size):
                colors = temp_colors.copy()
                if min_index != i:
                    colors[min_index] = self.swap_color
                colors[i] = self.check_color
                colors[j] = self.check_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
                time.sleep(sort_speed)
                
                if arr[min_index] > arr[j]:
                    min_index = j
                    colors[min_index] = self.swap_color
                    self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
                    time.sleep(sort_speed)
            
            (arr[i], arr[min_index]) = (arr[min_index], arr[i])
                
                
                
    def bubble_sort_fn(self, arr):
        temp_colors = self.graph_colors.copy()
        
        arr_size = len(arr)
        sort_speed = 4 / arr_size
        
        for i in range(arr_size):
            temp_colors[arr_size - i] = self.good_color
            for j in range(0, arr_size - i - 1):
                colors = temp_colors.copy()
                colors[j] = self.check_color
                colors[j + 1] = self.check_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
                time.sleep(sort_speed)
                
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
                    
                    colors[j] = self.swap_color
                    colors[j + 1] = self.swap_color
                    self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
                    time.sleep(sort_speed)
                    
                    
        
    def merge_sort_helper_fn(self, arr, start, end, arr_size, i = 0):
        if end - start > 1:
            middle = start + ((end - start) // 2)
            
            self.merge_sort_helper_fn(arr, start, middle, arr_size, i + 1)
            self.merge_sort_helper_fn(arr, middle, end, arr_size, i + 1)
            
            self.merge_sort(arr, start, middle, end, arr_size, i)
            
    def merge_sort(self, arr, start, middle, end, arr_size, i):
        temp_colors = self.graph_colors.copy()
        
        length = middle - start
        temp_arr = [arr[start + index] for index in range(length)]
       
        merge = length > 1
        
        if merge:
            sort_speed = 2.5 / arr_size
        else:
            sort_speed = 4 / arr_size
       
        i = 0
        j = middle
        k = start
        
        if merge:
            while k < middle:
                while j < end:
                    if j == k:
                        break
                    colors = temp_colors.copy()
                    
                    if arr[j] < arr[k]:
                        shift_arr = arr[k:j]
                        
                        index = k
                        while index <= j:
                            colors[index] = self.swap_color
                            index += 1
                            
                        arr[k] = arr[j]
                        
                        k += 1
                        j += 1
                        
                        arr[k:j] = shift_arr
                        self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
                        time.sleep(sort_speed)
                    else:
                        k += 1
                    
                j = middle
                k += 1
        else:
            while i < length and j < end:
                colors = temp_colors.copy()
                
                colors[k] = self.check_color
                colors[j] = self.check_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
                time.sleep(sort_speed)
                
                if temp_arr[i] <= arr[j]:
                    i += 1
                    k += 1
                else:
                    (arr[k], arr[j]) = (arr[j], arr[k])
                    
                    colors[k] = self.swap_color
                    colors[j] = self.swap_color
                    self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
                    j += 1
                    k += 1
                    
                time.sleep(sort_speed)
    
    
    def quick_sort_fn(self, arr, low, high):
        if low < high:
            p_index = self.partition(arr, low, high)
            
            self.quick_sort_fn(arr, low, p_index - 1)
            self.quick_sort_fn(arr, p_index + 1, high)
    def partition(self, arr, low, high):
        temp_colors = self.graph_colors.copy()
        
        sort_speed = 4 / len(arr)
        
        pivot = arr[high]
        index = low - 1
        
        for j in range(low, high):
            colors = temp_colors.copy()
            colors[high] = self.check_color
            colors[index + 1] = self.check_color
            colors[j] = self.check_color
            self.sort_graph.setOpts(brushes = [colors[index] for index in range(len(arr))])
            
            time.sleep(sort_speed)
            if arr[j] < pivot:
                index += 1
                
                (arr[index], arr[j]) = (arr[j], arr[index])
                
                colors[high] = self.check_color
                colors[j] = self.swap_color
                colors[index] = self.swap_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(len(arr))])
                
                time.sleep(sort_speed)
                
                
                
        self.sort_graph.setOpts(brushes = [temp_colors[index] for index in range(len(arr))])
        
        (arr[index + 1], arr[high]) = (arr[high], arr[index + 1])
        
        colors[index + 1] = self.swap_color
        colors[high] = self.swap_color
        self.sort_graph.setOpts(brushes = [colors[index] for index in range(len(arr))])
        
        time.sleep(sort_speed)
        
        return index + 1
            
            
    def heap_sort_fn(self, arr):
        temp_colors = self.graph_colors.copy()
        
        arr_size = len(arr)
        sort_speed = 4 / arr_size
        
        for i in range(arr_size // 2 - 1, -1, -1):
            self.heapify_fn(arr, arr_size, i, sort_speed)
            
        for i in range(arr_size - 1, 0, -1):
            colors = temp_colors.copy()
            
            (arr[i], arr[0]) = (arr[0], arr[i])
            
            colors[i] = self.swap_color
            colors[0] = self.swap_color
            self.sort_graph.setOpts(brushes = [colors[index] for index in range(len(arr))])
            
            time.sleep(sort_speed)
            self.heapify_fn(arr, i, 0, sort_speed)
            
    def heapify_fn(self, arr, n, i, sort_speed):
        temp_colors = self.graph_colors.copy()
        largest = i
        
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[largest] < arr[left]:
            largest = left
        
        if right < n and arr[largest] < arr[right]:
            largest = right
            
        temp_colors[i] = self.check_color
        temp_colors[largest] = self.check_color
        self.sort_graph.setOpts(brushes = [temp_colors[index] for index in range(len(arr))])
            
        time.sleep(sort_speed)
            
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])
            
            temp_colors[largest] = self.swap_color
            temp_colors[i] = self.swap_color
            self.sort_graph.setOpts(brushes = [temp_colors[index] for index in range(len(arr))])
            
            time.sleep(sort_speed)
            self.heapify_fn(arr, n, largest, sort_speed)
            
    def cocktail_sort_fn(self, arr):
        temp_colors = self.graph_colors.copy()
        
        arr_size = len(arr)
        sort_speed = 4 / arr_size
        
        start = 0
        end = arr_size - 1
        
        swap = True
        while swap:
            swap = False
            for i in range(start, end):
                colors = temp_colors.copy()
                colors[i] = self.check_color
                colors[i + 1] = self.check_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
                time.sleep(sort_speed)
                if arr[i] > arr[i + 1]:
                    (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
                    
                    colors[i] = self.swap_color
                    colors[i + 1] = self.swap_color
                    self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
                    time.sleep(sort_speed)
                    
                    swap = True
                    
                
            
            temp_colors[end] = self.good_color
            self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
            if swap == False:
                break
            
            swap = False
            
            end -= 1
            
            for i in range(end - 1, start - 1, -1):
                colors = temp_colors.copy()
                colors[i] = self.check_color
                colors[i + 1] = self.check_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
                time.sleep(sort_speed)
                if arr[i] > arr[i + 1]:
                    (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
                    
                    colors[i] = self.swap_color
                    colors[i + 1] = self.swap_color
                    self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                    
                    time.sleep(sort_speed)
                    
                    swap = True   
                
                    
            temp_colors[start] = self.good_color
            
            start += 1
            
    def gnome_sort_fn(self, arr):
        temp_colors = self.graph_colors.copy()
        
        arr_size = len(arr)
        sort_speed = 4 / arr_size
        
        index = 0
        
        while index < arr_size:
            if index == 0:
                index += 1
                
            colors = temp_colors.copy()
            colors[index] = self.check_color
            colors[index - 1] = self.check_color
            self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
            time.sleep(sort_speed)
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                (arr[index], arr[index - 1]) = (arr[index - 1], arr[index])
                
                colors[index] = self.swap_color
                colors[index - 1] = self.swap_color
                self.sort_graph.setOpts(brushes = [colors[index] for index in range(arr_size)])
                
                time.sleep(sort_speed)
                
                index -= 1
            