import hashtable

# create a mapping of name to phone number
phonebook = hashtable.new()
hashtable.set(phonebook, 'John Smith', '070 456382')
hashtable.set(phonebook, 'Lisa Smith', '073 193872')
hashtable.set(phonebook, 'Sam Doe',   '073 235454')
hashtable.set(phonebook, 'Sandra Dee', '070 343955')
hashtable.set(phonebook, 'John Smith', '777 456382')

op = hashtable.new()
hashtable.set(op, '070 456382', 'Mobile Inc.')
hashtable.set(op, '073 193872', 'Sky Line')
hashtable.set(op, '073 235454', 'Sky Line')
hashtable.set(op, '070 343955', 'Mobile Inc.')

print '-' * 10
print "John Smith's number is: %s" % hashtable.get(phonebook, 'John Smith')
print "Lisa Smith's number is: %s" % hashtable.get(phonebook, 'Lisa Smith')

print '-'*10
print 'The hole phonebook:'
hashtable.list(phonebook)

print '-' * 10
print "Sam Doe's phone company  is: %s" %  hashtable.get(op, hashtable.get(phonebook, 'Sam Doe'))
print "Sandra Dee's phone company is: %s" % hashtable.get(op, hashtable.get(phonebook, 'Sandra Dee'))

print '-' * 10
print 'Phone number belong to company:'
hashtable.list(op)

print '-' * 10
name = hashtable.get(phonebook, 'Luke Sky')

if not name:
  print "No Luke Sky in phonebook."

print '-' * 10
phonebook = hashtable.get(phonebook, 'Ted Baker', 'Not found in the phonebook')
print " 'Ted Baker': %s" % phonebook
