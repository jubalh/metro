[section target]

arch: amd64

[section portage]

CFLAGS: -O2 -march=opteron -pipe
CHOST: x86_64-pc-linux-gnu
HOSTUSE: mmx sse sse2 3dnow 3dnowext
