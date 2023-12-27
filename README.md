# Caesar Cipher

Simple Encryption, Decription, Bruteforce and Frequency Attacks using the Caesar cipher.

## Usage

### Help

Command:
```bash
python caesar_cipher.py -h
```

Output:
```bash
usage: Caesar Chiper [-h] [-e] [-d] [-b] [-f] [-t TEXT] [-s SHIFTMENT]

Encryption, Decription using the caesar cipher.

options:
  -h, --help            show this help message and exit
  -e, --encrypt
  -d, --decrypt
  -b, --bruteforce
  -f, --frequency
  -t TEXT, --text TEXT
  -s SHIFTMENT, --shiftment SHIFTMENT

Encryption, Decription using the caesar cipher.
```

### Encrypt Text

Command:
```bash
python caesar_cipher.py --encrypt --text 'hello world' --shiftment 3
```

Output:
```bash
Encrypted: khoor zruog
```

### Decrypt Text

```bash
python caesar_cipher.py --decrypt --text 'khoor zruog' --shiftment 3
```

Output:
```bash
Decrypted: hello world
```

### Bruteforce Attack

```bash
python caesar_cipher.py --bruteforce --text 'khoor zruog'
```

Output:
```bash
Shiftment 1; Decrypted: jgnnq yqtnf
Shiftment 2; Decrypted: ifmmp xpsme
Shiftment 3; Decrypted: hello world
Shiftment 4; Decrypted: gdkkn vnqkc
Shiftment 5; Decrypted: fcjjm umpjb
Shiftment 6; Decrypted: ebiil tloia
Shiftment 7; Decrypted: dahhk sknhz
Shiftment 8; Decrypted: czggj rjmgy
Shiftment 9; Decrypted: byffi qilfx
Shiftment 10; Decrypted: axeeh phkew
Shiftment 11; Decrypted: zwddg ogjdv
Shiftment 12; Decrypted: yvccf nficu
Shiftment 13; Decrypted: xubbe mehbt
Shiftment 14; Decrypted: wtaad ldgas
Shiftment 15; Decrypted: vszzc kcfzr
Shiftment 16; Decrypted: uryyb jbeyq
Shiftment 17; Decrypted: tqxxa iadxp
Shiftment 18; Decrypted: spwwz hzcwo
Shiftment 19; Decrypted: rovvy gybvn
Shiftment 20; Decrypted: qnuux fxaum
Shiftment 21; Decrypted: pmttw ewztl
Shiftment 22; Decrypted: olssv dvysk
Shiftment 23; Decrypted: nkrru cuxrj
Shiftment 24; Decrypted: mjqqt btwqi
Shiftment 25; Decrypted: lipps asvph
```

### Frequency Attack

```bash
python caesar_cipher.py --frequency --text 'khoor zruog'
```

Output:
```bash
Shiftment 3; Decrypted: hello world
```