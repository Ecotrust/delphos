all: resources_rc.py
	cd gui; $(MAKE)

clean:
	rm -f resources_rc.py
	rm -f *.pyc
	rm -f *~
	rm -f *#
	rm -rf dist
	rm -rf build
	cd gui; $(MAKE) clean
	cd core; $(MAKE) clean

resources_rc.py: resources.qrc
	pyrcc4 -o resources_rc.py resources.qrc
