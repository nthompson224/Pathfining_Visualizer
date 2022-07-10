from PyQt6.QtWidgets import QApplication

# Main entry point for application

if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet('QLabel{font-size: 20pt; color: #45A5FF}')
    
    from GUI import MainWindow
    
    main = MainWindow()
    main.show()
    app.exec()