H = list(__import__('string', fromlist=['printable']).printable[10:62] + __import__('string', fromlist=['printable']).printable[0:10] + __import__('string', fromlist=['printable']).printable[74] + __import__('string', fromlist=['printable']).printable[88])
def cryptPassword(pwd, key) -> str:
	loc4 = '#1'
	for loc5 in range(0, len(pwd)):
		loc6 = ord(pwd[loc5])
		loc7 = ord(key[loc5])
		loc8 = __import__('math').floor(loc6 / 16)
		loc9 = loc6 % 16
		loc4 = loc4 + (H[(loc8 + loc7 % len(H)) % len(H)] + H[(loc9 + loc7 % len(H)) % len(H)]) # 64
	return loc4
def decryptPassword(_hash) -> str:
	if _hash.startswith('#1'): _hash = _hash[2:]
	HC, _pass, valid = [], [], False
	for i in [(i, i+1) for i in range(len(_hash)) if i % 2 == 0]:
		for _all in range(0, 144001): # all unicode
			_loc6 = ord(chr(_all))
			if valid is False:
				for k in __import__('string', fromlist=['printable']).printable:
					_loc7 = ord(k)
					_loc8 = __import__('math').floor(_loc6 / 16)
					_loc9 = _loc6 % 16
					_loc1 = H[(_loc8 + _loc7 % 64) % 64]
					_loc2 = H[(_loc9 + _loc7 % 64) % 64]
					try:
						if _loc1 == _hash[i[0]] and _loc2 == _hash[i[1]]: # even
							_pass.append(chr(_loc6))
							HC.append(chr(_loc7))
							valid = True; break
					except: break
			else: valid = False; break
	return (''.join(_pass), ''.join(HC))
if __name__ == '__main__': print(decryptPassword(input('Hash [#1 are not required]: '))) #1RO32730X