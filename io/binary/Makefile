all:	write read

write:	writedata.py
	python $?

read:	x.y ReadData.class
	java ReadData

x.y:	write

ReadData.class: ReadData.java
	javac ReadData.java

clean:
	@rm -f ReadData.class x.y
