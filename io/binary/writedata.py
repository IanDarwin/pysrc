import struct
open('/tmp/x.y','wb').write(struct.pack('!i',123))
