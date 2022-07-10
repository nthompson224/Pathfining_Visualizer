from PyQt6.QtCore import QRunnable, QObject, pyqtSignal
import traceback, sys

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(int)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            ex, value = sys.exc_info()[:2]
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()