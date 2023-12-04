# CRC - How?

- Message and Polynomial:

The data to be transmitted or stored is considered as a message, which is treated as a binary number.
A fixed-size polynomial is chosen, often represented as a binary number. This polynomial is a key part of the CRC algorithm.

- Appending CRC Bits:

A certain number of bits (the CRC bits) are appended to the end of the message.
The number of CRC bits is determined by the chosen CRC polynomial.

- Division:

The combined message and CRC bits are treated as one large binary number.
The polynomial is used as a divisor, and a binary division is performed (usually XOR operations).
The remainder of this division is the CRC value.

- Transmission or Storage:

The original message along with the calculated CRC value is transmitted or stored.

- Verification:

At the receiving end or during data retrieval, the received message and CRC value are combined.
The same polynomial used for encoding is applied to the combined data.
If the remainder of this division is zero, the data is considered intact. Otherwise, an error is detected.

