all: resources_rc.py
	cd gui; $(MAKE)

 #Remove pyc files, leftovers from builds and other cruft that is dynamically created
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

#Create a new translation file the first time for your project.  Use update_translate if you just need to update an existing translation file
build_translate:
	qmake -project -o delphos.pro
	pylupdate4 -verbose delphos.pro
	pylupdate4 -verbose  core/*.py gui/*.py util/*.py -ts i18n/es_MX.ts

#Update existing translation file with new entries while maintaining past translations
update_translate:
	pylupdate4 -verbose  core/*.py gui/*.py util/*.py -ts i18n/es_MX.ts

#Create release of translation (qm file).  Updates if it already exists
release_translate:
	lrelease i18n\es_MX.ts -qm i18n\es_MX.qm

#Compile list of static resources (in qrc file) to python with binary
doc: resources_rc.py

resources_rc.py: resources.qrc
	pyrcc4 -o resources_rc.py resources.qrc
