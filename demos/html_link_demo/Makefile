

all: mainwindow_ui.py

clean:
	rm -f mainwindow_ui.py
	rm -f *.pyc

mainwindow_ui.py: mainwindow.ui
	pyuic4 -o mainwindow_ui.py mainwindow.ui
