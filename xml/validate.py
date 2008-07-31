#!/usr/bin/python -u

# Parse/Validate using libxml2

import sys
import libxml2

filename = "test.xml"
ctxt = libxml2.createFileParserCtxt(filename)
ctxt.validate(1)
ctxt.parseDocument()
doc = ctxt.doc()
if doc.name != filename:
    print "doc.name failed"
    sys.exit(1)
root = doc.children
if root.name != "doc":
    print "root.name failed"
    sys.exit(1)
valid = ctxt.isValid()
if valid != 1:
    print "document not valid"
    sys.exit(1)
doc.freeDoc()
