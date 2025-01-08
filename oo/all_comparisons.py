# PEP 8 recommends mplementing all 6 relational comarators,
# even though sorted() only uses __lt__.

class MusicalInstrument:

	def MusicalInstrument(self, name, key):
		self.name = name;
		self.key = key;

	def __eq__(self, mi):
		return self.name == mi
	def __ne__(self, mi):
		return self.name != mi
	def __lt__(self, mi):
		return self.name < mi
	def __gt__(self, mi):
		return self.name > mi
	def __le__(self, mi):
		return self.name <= mi
	def __ge__(self, mi):
		return self.name >= mi

	
def main():
	piano = MusicalInstrument('Piano', 'C');
	violin = MusicalInstrument('Violin', 'G');

	if piano > violin or \
		not piano < violin:
		print("<> fail")
	if not piano == piano:
		print("== fail self")
	if piano == violin:
		print("== fail different")
	# More cases, left as an exercise for the reader.

if __name__ == "main":
	main()
	
