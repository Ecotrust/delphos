all: resources_rc.py
	cd gui; $(MAKE)

clean:
	rm -f resources_rc.py
	rm -rf dist
	rm -rf build
	cd gui; $(MAKE) clean
	cd core; $(MAKE) clean
	cd data; $(MAKE) clean
	cd core; cd evamix; $(MAKE) clean
	cd util; $(MAKE) clean
cleandoc:
	rm -f resources_rc.py

doc: resources_rc.py

resources_rc.py: resources.qrc
	pyrcc4 -o resources_rc.py resources.qrc
