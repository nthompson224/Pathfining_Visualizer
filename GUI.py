from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton,
    QSizePolicy, QStackedWidget, QSlider,
    )

import pyqtgraph as pg

from PyQt6.QtCore import Qt, QThreadPool
from Worker import Worker
from sorts import Sort

from random import randint

check_color = '#E6E6E6'
good_color = '#45D56D'
swap_color = '#F74141'

def is_sorted(lst: list):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


main_button_style = (
    'QPushButton{background-color: #262626; color: #73BCFF; font-size: 24pt}',
    'QPushButton::hover{background-color: #4E93BF; color: #262626}',
    'QPushButton::hover::pressed{color: #121212}'
)
sub_button_style = (
    'QPushButton{color: #E6E6E6; font-size: 18pt; border: none}',
    'QPushButton:checked{color: #45A5FF}',
    'QPushButton::hover{color: #5BACDE}',
    'QPushButton::hover::pressed{color: #45A5FF}'
)
slider_style = (
    'QSlider::groove{height: 10}'
    'QSlider::handle:horizontal{background: #5BACDE}',
    'QSlider::handle:horizontal:hover {background: #45A5FF}'
)

class MainWindow(QMainWindow):
    frame_container = QStackedWidget()
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #121212')
        self.move(260, 180)
        
        self.sort = SortFrame()
        
        self.setCentralWidget(self.sort)


class SortFrame(QWidget):
    thread_pool = QThreadPool()
    bttn_list = [] #to keep track of buttons and which one is currently checked
    
    back_bttn = QPushButton("Back")
    back_bttn.setStyleSheet(' '.join(sub_button_style))
    
    selection_sort = QPushButton('Selection Sort')
    selection_sort.setCheckable(True)
    selection_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(selection_sort)
    
    bubble_sort = QPushButton('Bubble Sort')
    bubble_sort.setCheckable(True)
    bubble_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(bubble_sort)
    
    merge_sort = QPushButton('Merge Sort')
    merge_sort.setCheckable(True)
    merge_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(merge_sort)
    
    quick_sort = QPushButton('Quick Sort')
    quick_sort.setCheckable(True)
    quick_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(quick_sort)
    
    heap_sort = QPushButton('Heap Sort')
    heap_sort.setCheckable(True)
    heap_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(heap_sort)
    
    cocktail_sort = QPushButton('Cocktail Sort')
    cocktail_sort.setCheckable(True)
    cocktail_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(cocktail_sort)
    
    gnome_sort = QPushButton('Gnome Sort')
    gnome_sort.setCheckable(True)
    gnome_sort.setStyleSheet(' '.join(sub_button_style))
    bttn_list.append(gnome_sort)
    
    
    sort_bttn = QPushButton('Sort!')
    sort_bttn.setStyleSheet(' '.join(sub_button_style))
    
    def __init__(self):
        super(SortFrame, self).__init__()
        self.initUI()
     
    def initUI(self):
        self.grid_layout = QGridLayout()
        
        frame_title = QLabel(text = "Sorting Algorithms")
        frame_title.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        
        self.size_slider = QSlider(Qt.Orientation.Horizontal)
        self.size_slider.setRange(3, 50)
        self.size_slider.setStyleSheet(' '.join(slider_style))
        self.slider_label = QLabel('3')
        self.size_slider.valueChanged.connect(self.update_label)
        
        self.arr_size = self.size_slider.value()
        
        self.grid_layout.layout().addWidget(self.back_bttn, 0, 0)
        self.grid_layout.layout().addWidget(frame_title, 0, 3, 1, 2)
        self.grid_layout.layout().addWidget(self.sort_bttn, 0, 7)
        
        self.grid_layout.layout().addWidget(self.selection_sort, 2, 0, 1, 2)
        self.grid_layout.layout().addWidget(self.bubble_sort, 2, 2, 1, 2)
        self.grid_layout.layout().addWidget(self.merge_sort, 2, 4, 1, 2)
        self.grid_layout.layout().addWidget(self.quick_sort, 2, 6, 1, 2)
        self.grid_layout.layout().addWidget(self.heap_sort, 3, 1, 1, 2)
        self.grid_layout.layout().addWidget(self.cocktail_sort, 3, 3, 1, 2)
        self.grid_layout.layout().addWidget(self.gnome_sort, 3, 5, 1, 2)
        
        self.grid_layout.layout().addWidget(QLabel('Array Size:'), 4, 2)
        self.grid_layout.layout().addWidget(self.size_slider, 4, 3, 1, 3)
        self.grid_layout.layout().addWidget(self.slider_label, 4, 6)
        
        self.create_graph()
        
        self.sort = Sort(self.sort_graph, self.graph_colors)
        
        self.selection_sort.clicked.connect(lambda: self.button_checked(self.selection_sort))
        self.bubble_sort.clicked.connect(lambda: self.button_checked(self.bubble_sort))
        self.merge_sort.clicked.connect(lambda: self.button_checked(self.merge_sort))
        self.quick_sort.clicked.connect(lambda: self.button_checked(self.quick_sort))
        self.heap_sort.clicked.connect(lambda: self.button_checked(self.heap_sort))
        self.cocktail_sort.clicked.connect(lambda: self.button_checked(self.cocktail_sort))
        self.gnome_sort.clicked.connect(lambda: self.button_checked(self.gnome_sort))
        
        self.sort_bttn.clicked.connect(self.sort_bttn_clicked)
        
        self.setLayout(self.grid_layout)
        
    def create_graph(self):
        y = [randint(1, 500) for i in range(self.arr_size)]
        x1 = [x for x in range(self.arr_size)]
        
        self.graph_colors = {i: '#6BC7FF' for i in range(51)}
        
        self.plot = pg.GraphicsLayoutWidget()
        self.view = self.plot.addViewBox(border = '#45A5FF', enableMouse = False, enableMenu = False)
        
        self.plot.addLabel('Select an Algorithm', 1, 0, size = '16pt', color = '#6BC7FF')
        
        self.sort_graph = pg.BarGraphItem(x = x1, height = y, width = 0.5,
                                brushes = [self.graph_colors[index] for index in range(self.arr_size)])
        
        self.view.addItem(self.sort_graph)
        
        self.grid_layout.layout().addWidget(self.plot, 5, 1, 1, 6)
        
    def button_checked(self, bttn):
        for b in self.bttn_list:
            if b != bttn:
                b.setChecked(False)
        self.plot.removeItem(self.plot.getItem(1, 0))
        self.plot.addLabel(bttn.text(), 1, 0, size = '16pt', color = '#6BC7FF')
    
    def update_label(self, value):
        self.slider_label.setText(str(value))
        self.arr_size = self.size_slider.value()
        self.view.setBorder('#45A5FF')
        y = [randint(1, 500) for i in range(self.arr_size)]
        self.sort_graph.setOpts(x = [x for x in range(self.arr_size)],
                        height = y,
                        brushes = [self.graph_colors[index] for index in range(self.arr_size)])
        
    def sort_bttn_clicked(self):
        self.size_slider.blockSignals(True)
        self.sort_bttn.blockSignals(True)
        
        arr = self.sort_graph.getData()[1]
        
        if self.selection_sort.isChecked():
            worker = Worker(self.sort.selection_sort_fn, arr)
        elif self.bubble_sort.isChecked():
            worker = Worker(self.sort.bubble_sort_fn, arr)
        elif self.merge_sort.isChecked():
            worker = Worker(self.sort.merge_sort_helper_fn, arr, 0, len(arr), len(arr))
        elif self.quick_sort.isChecked():
            worker = Worker(self.sort.quick_sort_fn, arr, 0, len(arr) - 1)
        elif self.heap_sort.isChecked():
            worker = Worker(self.sort.heap_sort_fn, arr)
        elif self.cocktail_sort.isChecked():
            worker = Worker(self.sort.cocktail_sort_fn, arr)
        elif self.gnome_sort.isChecked():
            worker = Worker(self.sort.gnome_sort_fn, arr)
        else:
            self.size_slider.blockSignals(False)
            self.sort_bttn.blockSignals(False)
            return
        
        worker.signals.finished.connect(self.sort_complete)
        self.thread_pool.reserveThread()
        self.thread_pool.startOnReservedThread(worker)
        
    def sort_complete(self):
        self.view.setBorder(good_color)
        colors = {i: good_color for i in range(51)}
        self.sort_graph.setOpts(brushes = [colors[index] for index in range(self.arr_size)])
        self.size_slider.blockSignals(False)
        self.sort_bttn.blockSignals(False)
