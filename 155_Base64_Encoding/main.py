# 1 byte = 8 bits
# 1 bit = 0 or 1

# 10011010 = 8 bits = 1 byte
# 10011010 10101010 01011010 = 3 * 8 bits = 3 bytes
# 100110 101010 101001 011010 = 4 * 6 bits

"""
Base64 is a group of binary-to-text encoding schemes that represent binary data (more specifically, a sequence of 8-bit bytes) in sequences of 24 bits that can be represented by four 6-bit Base64 digits.
"""

"""
Base64 table from RFC 4648

Index	Binary	Char		Index	Binary	Char		Index	Binary	Char		Index	Binary	Char
0	    000000	A	        16	    010000	Q	        32	    100000	g	        48	    110000	w
1	    000001	B	        17	    010001	R	        33	    100001	h	        49	    110001	x
2	    000010	C	        18	    010010	S	        34	    100010	i	        50	    110010	y
3	    000011	D	        19	    010011	T	        35	    100011	j	        51	    110011	z
4	    000100	E	        20	    010100	U	        36	    100100	k	        52	    110100	0
5	    000101	F	        21	    010101	V	        37	    100101	l	        53	    110101	1
6	    000110	G	        22	    010110	W	        38	    100110	m	        54	    110110	2
7	    000111	H	        23	    010111	X	        39	    100111	n	        55	    110111	3
8	    001000	I	        24	    011000	Y	        40	    101000	o	        56	    111000	4
9	    001001	J	        25	    011001	Z	        41	    101001	p	        57	    111001	5
10	    001010	K	        26	    011010	a	        42	    101010	q	        58	    111010	6
11	    001011	L	        27	    011011	b	        43	    101011	r	        59	    111011	7
12	    001100	M	        28	    011100	c	        44	    101100	s	        60	    111100	8
13	    001101	N	        29	    011101	d	        45	    101101	t	        61	    111101	9
14	    001110	O	        30	    011110	e	        46	    101110	u	        62	    111110	+
15	    001111	P	        31	    011111	f	        47	    101111	v	        63	    111111	/
Padding	        =	

"""

# Base64 converts binary data to text data
# certain bytes might act as escape characters when the bytes are being sent over a protocol
# converting it to text solves this issue

# This is not Encryption, anyone can decode a base64 encoding

import base64

myText = 'Hello World'

myText = myText.encode("ascii")
myText_b64 = base64.b64encode(myText)

print(myText_b64)

print(base64.b64decode(myText_b64))