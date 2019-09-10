#!/usr/bin/env python

# Parse/Validate using libxml2

import sys
import libxml2

if len(sys.argv) == 1:
	filename = "test.xml"
else:
	filename = sys.argv[1]

ctxt = libxml2.createFileParserCtxt(filename)
ctxt.validate(True)
ctxt.parseDocument()
doc = ctxt.doc()
if doc.name != filename:
    print("doc.name failed")
    sys.exit(1)
root = doc.children
if root.name != "doc":
    print("root.name failed")
    sys.exit(1)
valid = ctxt.isValid()
if valid != 1:
    print("document not valid")
    sys.exit(1)
doc.freeDoc()
