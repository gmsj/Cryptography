# Cifra de Cesar
# Cifra de Vigenere
# Cifra de Atbash
# Cifra da palavra-chave

# Deixar as funções com parametros opcionais para case sensitive, start, end

import collections
import base64

def frequencyAnalysis(msg):
	# Recomendado com msgs de pelo menos 50 caracteres
	return collections.Counter(msg.upper()).most_common()

def caesarDec(msg):
	start = 97
	end = 122
	colection = []
	msg = msg.lower()	

	for i in range(start, end+1):
		colection.append(chr(i))

	for i in range(0,(end-start)+1):
		msgDec = ''
		for char in msg:
			if char in colection:
				num = ord(char)
				if (num + i) > end:
					num = ((num + i) % end) + (start - 1)
				else:
					num = num + i
				msgDec = msgDec + chr(num)
			else:
				msgDec = msgDec + char
		print('Rot [' + str(i).zfill(2) + '] : ' + msgDec)

def caesarEnc(msg, rot):
	start = 97
	end = 122
	msg = msg.lower()
	msgEnc = ''
	colection = []

	for i in range(start, end+1):
		colection.append(chr(i))

	for char in msg:
		if char in colection:
			num = ord(char)
			if (num + rot) > end:
				num = ((num + rot) % end) + (start - 1)
			else:
				num = num + rot
			msgEnc = msgEnc + chr(num)
		else:
			msgEnc = msgEnc + char
	print('MsgEnc: ' + msgEnc)
	return msgEnc

def vigenereEnc(msg, key):
	start = 97
	end = 122
	msg = msg.lower()
	msgEnc = ''
	colection = []
	size = len(key)

	for i in range(start, end+1):
		colection.append(chr(i))

	i = 0
	for char in msg:
		if char in colection:
			num = ord(char)
			if i >= size:
				i = 0
			if (num + ord(key[i]) - start) > end:
				num = ((num + ord(key[i]) - start) % end) + (start - 1)
			else:
				num = num + ord(key[i]) - start
			msgEnc = msgEnc + chr(num)
			i = i + 1
		else:
			msgEnc = msgEnc + char
	print('MsgEnc: ' + msgEnc)
	return msgEnc

def vigenereDec(msg, key):
	start = 97
	end = 122
	msg = msg.lower()
	msgDec = ''
	colection = []
	size = len(key)

	for i in range(start, end+1):
		colection.append(chr(i))

	i = 0
	for char in msg:
		if char in colection:
			num = ord(char)
			if i >= size:
				i = 0
			if (num - ord(key[i]) + start) < start:
				num = (num - ord(key[i]) + end + 1)
			else:
				num = num - ord(key[i]) + start
			msgDec = msgDec + chr(num)
			i = i + 1
		else:
			msgDec = msgDec + char
	print('MsgDec: ' + msgDec)
	return msgDec

def atbashEnc(msg):
	start = 97
	end = 122
	msg = msg.lower()
	msgEnc = ''
	for char in msg:
		if (ord(char) >= start) and (ord(char) <= end):
			dif = ord(char) - start
			msgEnc = msgEnc + chr(end - dif)
		else:
			msgEnc = msgEnc + char
	print('MsgEnc: ' + msgEnc)
	return msgEnc

def atbashDec(msg):
	start = 97
	end = 122
	msg = msg.lower()
	msgDec = ''
	for char in msg:
		if (ord(char) >= start) and (ord(char) <= end):
			dif = end - ord(char)
			msgDec = msgDec + chr(start + dif)
		else:
			msgDec = msgDec + char
	print('MsgDec: ' + msgDec)
	return msgDec

def keywordEnc(msg, key):
	start = 97
	end = 122
	msg = msg.lower()
	key = key.lower()
	msgEnc = ''
	colection = list(key)

	for i in range(0, len(colection) - 1):
		if colection[i] in colection[0:i]:
			colection.pop(i)
	
	for i in range(start, end+1):
		if chr(i) not in colection:
			colection.append(chr(i))

	for char in msg:
		if (ord(char) >= start) and (ord(char) <= end):
			dif = ord(char) - start
			msgEnc = msgEnc + colection[dif]
		else:
			msgEnc = msgEnc + char
	print('MsgEnc: ' + msgEnc)
	return msgEnc

def keywordDec(msg,key):
	start = 97
	end = 122
	msg = msg.lower()
	key = key.lower()
	msgDec = ''
	colection = list(key)

	for i in range(0, len(colection) - 1):
		if colection[i] in colection[0:i]:
			colection.pop(i)

	for i in range(start, end+1):
		if chr(i) not in colection:
			colection.append(chr(i))

	for char in msg:
		if (ord(char) >= start) and (ord(char) <= end):
			dif = colection.index(char)
			msgDec = msgDec + chr(start + dif)
		else:
			msgDec = msgDec + char
	print('MsgDec: ' + msgDec)
	return msgDec

# Ainda não está funcionando
def oneTimePad(msg, key):
	# convertendo string para bytes e dps para base64
	msg = base64.b64encode(msg.encode('utf-8'))
	key = base64.b64encode(key.encode('utf-8'))
	result = msg ^ key
	print('Msg: '+ result)