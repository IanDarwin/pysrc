all:	write read

write:	writedata.py
	python $?

read:	x.y ReadData.java
	@echo "It should print 123 then -1 for EOF (End Of File)"
	java ReadData.java

x.y:	write

clean:
	@rm -f x.y
