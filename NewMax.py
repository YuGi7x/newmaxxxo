import sys

# Check version
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
if PYTHON_VERSION != bytes([51, 46, 57]).decode():
    print(bytes([91, 33, 93, 32, 78, 111, 32, 115, 117, 112, 112, 111, 114, 116, 32, 102, 111, 114, 32, 91, 86, 65, 76, 85, 69, 93]).decode().replace(bytes([91, 86, 69, 82, 83, 73, 79, 78, 93]).decode(), sys.version.split(bytes([32]).decode())[0]))
    exit(0)

import marshal
exec(marshal.loads(b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00s\xce\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa0\x05e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa0\x07e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x03d\x06\x85\x02\x19\x00\xa1\x01Z\x08e\x08e\x03g\x00d\x07\xa2\x01\x83\x01\xa0\x04\xa1\x00k\x03r\xb4e\te\x03g\x00d\x08\xa2\x01\x83\x01\xa0\x04\xa1\x00\xa0\ne\x03g\x00d\t\xa2\x01\x83\x01\xa0\x04\xa1\x00e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa1\x02\x83\x01\x01\x00e\x0bd\x02\x83\x01\x01\x00d\x02d\x03l\x0cZ\x0ce\re\x0c\xa0\x0ed\n\xa1\x01\x83\x01\x01\x00d\x03S\x00)\x0bF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N\xe9.\x00\x00\x00\xe9 \x00\x00\x00\xe9\xff\xff\xff\xff)\x03\xe93\x00\x00\x00r\x02\x00\x00\x00\xe99\x00\x00\x00)\x1a\xe9[\x00\x00\x00\xe9!\x00\x00\x00\xe9]\x00\x00\x00r\x03\x00\x00\x00\xe9N\x00\x00\x00\xe9o\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x0b\x00\x00\x00r\x0f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00\xe9V\x00\x00\x00\xe9A\x00\x00\x00\xe9L\x00\x00\x00\xe9U\x00\x00\x00\xe9E\x00\x00\x00r\t\x00\x00\x00)\tr\x07\x00\x00\x00r\x12\x00\x00\x00r\x16\x00\x00\x00\xe9R\x00\x00\x00\xe9S\x00\x00\x00\xe9I\x00\x00\x00\xe9O\x00\x00\x00r\n\x00\x00\x00r\t\x00\x00\x00s\xb81\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00s\xce\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa0\x05e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa0\x07e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x03d\x06\x85\x02\x19\x00\xa1\x01Z\x08e\x08e\x03g\x00d\x07\xa2\x01\x83\x01\xa0\x04\xa1\x00k\x03r\xb4e\te\x03g\x00d\x08\xa2\x01\x83\x01\xa0\x04\xa1\x00\xa0\ne\x03g\x00d\t\xa2\x01\x83\x01\xa0\x04\xa1\x00e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa1\x02\x83\x01\x01\x00e\x0bd\x02\x83\x01\x01\x00d\x02d\x03l\x0cZ\x0ce\re\x0c\xa0\x0ed\n\xa1\x01\x83\x01\x01\x00d\x03S\x00)\x0bF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N\xe9.\x00\x00\x00\xe9 \x00\x00\x00\xe9\xff\xff\xff\xff)\x03\xe93\x00\x00\x00r\x02\x00\x00\x00\xe99\x00\x00\x00)\x1a\xe9[\x00\x00\x00\xe9!\x00\x00\x00\xe9]\x00\x00\x00r\x03\x00\x00\x00\xe9N\x00\x00\x00\xe9o\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x0b\x00\x00\x00r\x0f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00\xe9V\x00\x00\x00\xe9A\x00\x00\x00\xe9L\x00\x00\x00\xe9U\x00\x00\x00\xe9E\x00\x00\x00r\t\x00\x00\x00)\tr\x07\x00\x00\x00r\x12\x00\x00\x00r\x16\x00\x00\x00\xe9R\x00\x00\x00\xe9S\x00\x00\x00\xe9I\x00\x00\x00\xe9O\x00\x00\x00r\n\x00\x00\x00r\t\x00\x00\x00s;/\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00@\x00\x00\x00sz\x01\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02d\x02d\x03l\x03Z\x03d\x02d\x03l\x04Z\x04e\x05g\x00d\x04\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x05\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x06\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x07\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x08\xa2\x01\x83\x01\xa0\x06\xa1\x00g\x05Z\x07e\x03\xa0\x08e\x04j\t\xa0\ne\x05g\x00d\t\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x02j\x0b\xa1\x02e\x05d\nd\x0bg\x02\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x0c\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\r\xa2\x01\x83\x01\xa0\x06\xa1\x00g\x04\xa1\x01\xa0\x06e\x05g\x00d\x0e\xa2\x01\x83\x01\xa0\x06\xa1\x00\xa1\x01\xa0\x0ce\x05d\x0fg\x01\x83\x01\xa0\x06\xa1\x00\xa1\x01Z\rd\x10d\x11\x84\x00e\rD\x00\x83\x01Z\re\x07D\x00]nZ\x0ee\x0ee\rv\x01r\xf4zTe\x03\xa0\x0fe\x04j\t\xa0\ne\x05g\x00d\t\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x02j\x0b\xa1\x02e\x05d\nd\x0bg\x02\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x0c\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x12\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x0eg\x05\xa1\x01\x01\x00W\x00q\xf4\x01\x00\x01\x00\x01\x00Y\x00q\xf40\x00q\xf4e\x10d\x13d\x14\x84\x00d\x15e\x11\x83\x02\x83\x01\x01\x00d\x03S\x00)\x16F\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N)\x08\xe9r\x00\x00\x00\xe9e\x00\x00\x00\xe9q\x00\x00\x00\xe9u\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9t\x00\x00\x00r\x06\x00\x00\x00)\x08\xe9p\x00\x00\x00\xe9y\x00\x00\x00\xe9f\x00\x00\x00\xe9i\x00\x00\x00\xe9g\x00\x00\x00\xe9l\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00)\x03\xe9b\x00\x00\x00r\x06\x00\x00\x00\xe94\x00\x00\x00)\tr\x07\x00\x00\x00r\x03\x00\x00\x00r\x02\x00\x00\x00\xe9m\x00\x00\x00\xe9c\x00\x00\x00\xe9o\x00\x00\x00r\r\x00\x00\x00r\x12\x00\x00\x00r\x02\x00\x00\x00)\x08r\x11\x00\x00\x00r\x12\x00\x00\x00r\r\x00\x00\x00r\x12\x00\x00\x00r\x02\x00\x00\x00\xe9a\x00\x00\x00r\x10\x00\x00\x00r\x13\x00\x00\x00)\x11\xe9P\x00\x00\x00\xe9Y\x00\x00\x00\xe9T\x00\x00\x00\xe9H\x00\x00\x00\xe9O\x00\x00\x00\xe9N\x00\x00\x00\xe9_\x00\x00\x00\xe9E\x00\x00\x00\xe9X\x00\x00\x00r\x1b\x00\x00\x00\xe9C\x00\x00\x00\xe9U\x00\x00\x00r\x16\x00\x00\x00\xe9A\x00\x00\x00\xe9B\x00\x00\x00\xe9L\x00\x00\x00r\x1b\x00\x00\x00\xe9-\x00\x00\x00r\x10\x00\x00\x00)\x03r\x08\x00\x00\x00r\x0b\x00\x00\x00r\x08\x00\x00\x00)\x06r\n\x00\x00\x00r\x02\x00\x00\x00r\x03\x00\x00\x00r\x03\x00\x00\x00\xe9z\x00\x00\x00r\x03\x00\x00\x00)\x05r\x05\x00\x00\x00r\x07\x00\x00\x00r\n\x00\x00\x00r"\x00\x00\x00\xe98\x00\x00\x00\xe9\n\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00C\x00\x00\x00s*\x00\x00\x00g\x00|\x00]"}\x01|\x01r\x04|\x01\xa0\x00t\x01d\x00d\x00g\x02\x83\x01\xa0\x02\xa1\x00\xa1\x01d\x01\x19\x00\x91\x02q\x04S\x00)\x02\xe9=\x00\x00\x00r\x01\x00\x00\x00)\x03\xda\x05split\xda\x05bytes\xda\x06decode)\x02\xda\x02.0\xda\x03lib\xa9\x00r,\x00\x00\x00\xda\x06string\xda\n<listcomp>\x0f\x00\x00\x00s\x04\x00\x00\x00\x06\x01\x06\xffr.\x00\x00\x00)\x07r\x0b\x00\x00\x00\xe9n\x00\x00\x00r\x06\x00\x00\x00r\x07\x00\x00\x00r\x13\x00\x00\x00r\r\x00\x00\x00r\r\x00\x00\x00c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00C\x00\x00\x00sD\x00\x00\x00|\x01t\x00d\x01d\x02\x84\x00t\x01g\x00\x83\x01\xa0\x02\xa1\x00g\x00d\x03\xa2\x01t\x03\x83\x03\x83\x01|\x00\x83\x01t\x01g\x00d\x04\xa2\x01\x83\x01\xa0\x02\xa1\x00t\x01g\x00d\x05\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x03S\x00)\x06Nc\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00r,\x00\x00\x00r,\x00\x00\x00)\x02r*\x00\x00\x00Z\x03___\xa9\x01\xda\x01_r,\x00\x00\x00r-\x00\x00\x00r.\x00\x00\x00\x1a\x00\x00\x00\xf3\x00\x00\x00\x00z.<lambda>.<locals>.<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r1\x00\x00\x00r,\x00\x00\x00r0\x00\x00\x00r-\x00\x00\x00\xda\x08<lambda>\x1a\x00\x00\x00r2\x00\x00\x00z\x1a<lambda>.<locals>.<lambda>)\x1dr\x1a\x00\x00\x00r\x1a\x00\x00\x00r\x0b\x00\x00\x00r\x10\x00\x00\x00r\x08\x00\x00\x00r\x12\x00\x00\x00r\x02\x00\x00\x00r\x07\x00\x00\x00r\x1a\x00\x00\x00r\x1a\x00\x00\x00\xe9(\x00\x00\x00\xe9"\x00\x00\x00r#\x00\x00\x00r\r\x00\x00\x00r\x0b\x00\x00\x00r\x0e\x00\x00\x00r8\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00\xe9d\x00\x00\x00r\x03\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00r\x10\x00\x00\x00r\x08\x00\x00\x00r\x02\x00\x00\x00r\x03\x00\x00\x00r\x06\x00\x00\x00r\x06\x00\x00\x00)\x08\xe9<\x00\x00\x00\xe9M\x00\x00\x00\xe9R\x00\x00\x00\xe9G\x00\x00\x00r\x17\x00\x00\x00r\x18\x00\x00\x00\xe9S\x00\x00\x00r\x16\x00\x00\x00)\x04r\x03\x00\x00\x00\xe9x\x00\x00\x00r\x03\x00\x00\x00r\x11\x00\x00\x00)\x04\xda\x04evalr(\x00\x00\x00r)\x00\x00\x00\xda\x03chr)\x02Z\x05_____Z\x06______r,\x00\x00\x00r,\x00\x00\x00r-\x00\x00\x00r6\x00\x00\x00\x1a\x00\x00\x00r2\x00\x00\x00r6\x00\x00\x00s\xbb\'\x00\x00x\x9cU\\\t[\x14\xcb\xb2\xfc+\x80"\xa0\x80\xd5{\x15"\x8a\x80\xa0\xb2\x08\x02\x1ee\x10\xba\xba\xba\x94Ud\x13\x11\xfc\xed\xaf##G\xef\xbb\xdf=\x083=\xdd\xb5dFFFfM{\xd36\xa3\xa3\xc7\xf5\x89\x0f\xf5\xc0\x1e\xfe7\xce\x7f\xf6\x06\xa6\xf4\x97\xd1\xf6\xba>\xfe\x7f\xd7\x8c\xe3\xff\xfa\xfe\xe4\xe1\xf7\x83\xd3\xd1\x9d\xbd\xd1\xee\xf7\xb1\x81\xf8\xfd\x1c\xaf\x0e\x1c\x9cv\xff\xec\x8e\x8d\x8d\x8e\x8c\x8c\xef\xb8b|\x00\xff%F~\xb8\xeeG\x92\xe2G\x82\x1f9~\x94\xbc\x02\xff\xe5f| \xc3\x8b)\xae1V?\xe7,_\xce\xbb\x0f\xe5%^4\xf8\xd1\xfd\xe5\\\xff^\xffs\xeb\\\xdfL\x92B~\xec\x8e7\xdf\xce\xbb\xf1\xc8\x8c\xc6\xc6\x87\xa6W6\x16\x97\xd6>l\x0e\x8d\x0f\xb5\xdd\x12\x0cuo\xf9\x91\x9b\xde\x8dk\xb6vz7\xa6\xea~\x84\xa6w\xe3\xeb\xdeM\x92\xf6nbx\xd2\xfd\xc8\xbb?\xca\xee]\xdb]\xd7\xbd\x18\xaa\xee\xb5\xf2\xed\xcb\xdeM\xdd\xbdb\x93\xee]s\x8b\xeb\xbb\x1f\xae\xf4\xbd\x9b\xc6m\xf4nZ\xfb\xbc\xfbH\xfe\xaa\xbb\xd6u\x7f\x85\xb5\xaf\x11\x1f\xeb~-\xba\xfb\x87\xeew\xbf\xcb{z\x7f\xd4}\xa6\xfb\\\xe8n\xee\xf2\xeckw\xd3\xb6{\xb9{l\x9b\x8cu\x17\xeaS\xe4\xbf\xee\xb2\xb6\xe6\xa5\xa1\xd8\xea>\xd7\r&\xe9\xde\x88\xdd\'\x12\xbc\xd9=\xa1\x8a\xb8\xc3T\xf7&\x1e\xd7\xdd\xc6F~:\x9a\xff\xbag\xc6n\x82!v\xa3h2\xdc|o\xa6\xfb\x19o\xae\xefo\x0b\\\xd1\xfd\x97}\x1b\xc0\xd4\xbb\xf1\x07\xcb\xbb\xd7\xdd\rZ\x8c\xdf\x9c\xf2\x91\xad\xeb\x9e\x1d\xbb\x81\xb4\xd5\xfe\xd9YwA\xf79\x1f\xf9h\x8c\xb7\xae&\xbaG\x96\xcfx\xc7\xba{P\x82\xbbw\xd3\xf6)>\xddM\xb4\xbbK\xd3\xe2\xfdw\xdd\x0b\xd9G\x0cyox\x8f\x03u\xb1\xd7\xeb\x9d\xff\xcc\xf16\xc6^\x1eae\xba\xff0\x89n\x96u\x83\xb5\xe9n\x86\xad\xc8.?|\xe9\xfeLW\xba\x0b\x8b=\xbd;\x16\xb9\xc0\xbaw\xff\xca\xf2|\xc5\x96\xf4z\xdddC\xce\r\xae\xcd\x1e\xb6\\\xd7\xa1\xc5RMv\x7ft\x9f\xb0\xd5vna\t\x85~\xba\xe6\xd8\xb1Im\xca\xbf\xb1\xa6\xb8\xb6n9\x14\xfc\xeb\xccr\xf7)\x83\xc7\xcf\x9c\xe3#k\xdd\xeb\xa17\xd2]\xe1u\xb0\xe5\xce\x1a\xf7\xa5.\xf78\x0c,W\xa8o\xbb\xebm\xf8\xa8\xbbSt\xa6\x14\xd3_\xf8\xdc\x1b.\x9d\xecm71\x8f\xb1\xe6\x8bx\xf1Qwa\xb6x\x85\xbbL\xdf\xfbe\x0c\xeb\xd9\xd1n\xaf\xbbQ\x8d\x85\xab\xb6\xba\x9b\xd4\x8e;\xd0\xc6K\xbcD\xfb\x08\xe5*\x1f\xdddWX?\x98\xe0c<\xe2m\xf7#n\xc9\x98\xbb\x1d\xec\xa6a\xfft\xa3J\xd7\xb0\x11^\x0ct\x11\x9f\xc6\xe0\x7f\xe2\xafn*\xd6b\\\x98\x7f\xc2\xb5\xb2X\xd0\x88\x1b}^\xbb\xca\xee\xb9ou\xc1\x95\x0e\x1e&\xf2\x827\xc1\xee\xe3)\xbeo\xfa\xa1\x9bQk\xe8d\x0eFT\xae\xf3\x8a$\xeep\x9c\xc6\xce\xa8c\xb4\xfc\x8c-\xc4\x16\x97p\x9b\x1a~\xec\xbb\x11\x9b\xe2\xcf\x1c\xdeZ\xc3{\x9fqc\xee\xaf\xb5\x07\xf8H\xb8\xbc\xe7\x16b4\x1e\x0b\x94\xe8\x9a\xe2E\xdc\xddu/\x06|\x00f\xe6~a\xc3\xba\xdfL\x89M\xc1\x83\xfe\xc0b\x7f\x1c\xdfb\xe7\xbb7j\xff\x02.}\xd8]\x87\x1b\x84\xc9\xdd\xc7\xf4\x041\xae\x06\xfe\x15v0\xb6@\xb3O\xec\xaf\xa1\xc7||\x03\xf4(\x8et\x89d\xae\x80\x9e\x88\xdf\xbb\x8f\xf8\x06\xcfni\x15I\xa6s\x8e\xbc\x8d\x8b\xc4\x8f6\xe3:\x88s\xe0N) \x08\xaf\xbf\x967F\xfc:\xa7\x84\x0b\xbb\x87\x9e\xab\x0f\xbb\x8c\xb3\x85\xf9\xe3\xef\x10aP\xdd=\x8d\xf9\x81\x91\xe1\xe5\xeem\x93\xd2\x81\x83\xe3p\x05\x1b\xfd\x05\xcd\x11\xff\xd9\xb0\xfdd\x17[\xf2\x9d\xd8\x88{4a\xb8{@{\xc5Q&XK\xf3\x82\xc3\x17L\x0c\x18kqp\x81!\x84\xce\x1a\xe1\xe5\xf0Wl\xbb\x98T\xdb\xed\x91\xcd\x08x2(\xbcX4\\\x1f\xdc&f\x8f\xf7O\xb8\x10\xa1\xd9\xe4\xda\t2Y\xaeB\xa8\xe9\xe9\xb8\x89\x07\x8cU/\x14-3\x0c{\x82;$\xc6\xd9\xae\xc0\xd6\xb8\xb0\xa6 \xdaa\xa6u~E\x9b\x80A\xe2jo0|l\xa0\xf8\xc8\xa9ng\\\xa4\xdd\xda*\x87\x17\xdag3\xf0\x03G\xa8\x12\x9f\xe9\x96\x88\xb6\xe3\xc2\x18\xdd\x040\x08\x0c\x8eU\xee\xe9\n6\xbe\x1a\xa7=\xfa\xf4v\xb6\xc3?B\xa7\xe7\x8a\xfbz\x95\xdb\xd0\xe4[7X\x1f\x00n\xf8\x0e \n\xba\xed\xa6w\xfaz\x94\xe1\xa6\x96\x05\xa7\x19`f\x9d\xe7\xf7\x14Y\r\xb6\xd1\x10\xb1mu\xb6\x82\xa1\x0fn\x12\xea\xdb\xec\x06\x08\xf3\xc5?\xc4\xcd\x0f8\xe1P\xdf=\xdb%\xa2\x1a8d\xeb\x0e\xf7~\x9ca \xe7\xe3|\xba-\xb9\xfc\x82dE\xb7\xcc-\xfc&\xee\xf7\x17m\x8e\xbb\xd1\xb4\xb2\xd1\xb7\xdc\x8f\x88E\xce\xb6\x15\xa2`\x17\xf1F\x9d\x1c\xd6\x1fu+\x93\xee_\xd3\xd2Y\xea\x9a\x8e`k\xce\xccE\x05\x10\x18\xb3\x87\xf1tv\xebj\x19\xeb9\xf6\xe5\x17W\x16\x0fG\x18\x14w\xf4\x84mS]\xbf\x86s\xfe\xa9\xaf\x19\x92\xe15\xa6\xc1\x02\x01\x10\x10\xcf1\xf7\n\x90\x94\xfdG\x07k\xc2\x11n\xb4\xec\xf8HL\xdb\xf2\x025\xfc\xe4\x02\xb7lh4\x8d\x84\xc1}xK\xa3aEHD\xc1H)Q\xaa\x9e\xde\x9b\x87\x9f\x80/4[\xc3\xf4\x0b\xd8\x7f#\xa3\x98Z\xd9\xf8\x80\x8f\x0c\xc2\xca\xfc3\xd0\x14\x1a\x16\xe0\xb3-\t\xb6\xde\x8cOp\x0c\x89\xb8\xc0\x14a\x03\x8c\x05\xb1*\xa9@I\x92\x00\x82\x82\xf0\x96\x9f\x8d\x13>\xad\x19cX1\xf1\xe91\x17\xa8\xa9\'\xb9\xa2\x16\xbc\xc3\x95\xab/\x1e\xd0\xe1\x10F\x11\x00\x8d\xe1J\x87\x80\x9d\xc6\xfe\xaerYc\xd1\xbe}\xb5;#Xz\nX|N7\xc2\x00C{\xa4.\xd3g>0\x1a\x04\xb2\x04^\x9dd\xfb\xcf\xf8\xbew\xa7p\xe6f\x18\x11\xe4?\xdaS#h\xd3\x85\xd0\x11\x8e\x1a \x91\x88)\x826\xc48\xcd-\x85i$ F>\xfe\xa6\x9b\x0b\xeb*\x86\xb8\xd8\x1e+\xdf.q\xa7\xe1\xb3p\x1f\t\xfbB*&\xf8\x86x\x0e\xcc\x11\x06#\xc6\x12\xcf\x80\x7f\xf5\x89\x19\xd5\xb5o\xb7\xd67\xb9\xd9N\x07g2b\x0c\xfeu\xf0\x0f\xef\xda\xd5\x9f[\xe7tB0\xc4\xa6\x1f7\n\x05\xd0\xcc=~BD\xb6x\x1dQ\x06w\x83W\xc0\xf6\xe1\x19m\xfa\x9c{\n?\x00\x0e\x08\xcd\xac\x89\xc26Y\xac7h\xe9\x82\x95XV?\xbdM#\xc5\x165)\x01\xc6\x9a\xcf[3\x7f0C,lzL\xf4\x12\xeb\xc8\x00%\x129\xcc\x04vf\x88(\xdd\x96\xdf\x17\xdd7\xdc{\xfd\x0e\xe0\xf3\x90\x86\x14\xd2\xcb^ou\xf6\xdfp\xb0:XT\x80)\xc8\x18\xd6\x916\xcbg\x18\xf3\x19\x93\x98+h\xf5\x1d\x82\x8f\xf0\x02\xdb\xda;\xa2zR\xd0\t\xaa8\xc9Q#\xbeb\x06!\xbd\x1b\xc2\xca}\x83\'\x1ba\xc3\xaf\x15i[\xd2\xf2\x80e\x04\xc8D\xf5\x07!\x1e\xf98A\x0fc\xe8\x0c\xf6\\\xe1\x1e{U\xf2\xb3\xa1\x19\x83\xef\xec1\xee\t\xab\x8b\xdcX\x10\xf3XN\xd0Z\xa2Y\xae\t\x06m\xa4\x19w\xd6\xd9\xfb\x1f\xfc\ttT\x0c\xb8\xb6\xeb\xdc(\xdfr\x07\xbd2\x9b`\xe6I"\x1a\x89\x04\xd9\xe3\xe7}p\x07v&\xd7\x1c]S\x9b\x0b@\xb0;\xd2Q&\xb4\x11\xa0\xad\x90o\x984\xe2\xb8\x90\x0fK\xf2\x0fS\xc3\x16\x9b\xec\xf4\x9a\xbe\xd8\xb6\xcf\xe0\xb8f\x83\xe9\x0b\xd6\xc8+\xef\x17\xa2_~\xe2|\xacy\x85\r\x91\xd5\xbf\xe4\x98a\xc3.\x9b\xa3\x07\x86\xf2\xc7\xe69\x10\xe7\x0b\xdf\xb0f\xe9?\xe0\x93\x82ru<Fr)9A\x9aqF\x18\x92\xadO0p\xe0\x85`\xbe\xbd\x1bH\x18\xb4q[\x100\x97\xeb-\xd3\x1ftY\xcc\x02\xd1\xcd\xcav\xfd\x17?\x7f\xe2v\x18\x10\xdb\xb6>\x85\x95\xac\xdd\xe1\xc9\x87C\xb4Ba\xfd\xfe\xdd\xf2\xf5\x9fW\x8c_bP5\xd1\xd8\xa7\xc2\x95\xe0\x1e\xf9\x11\xb1&TN\xd8pz\xdb\xe4FA\xaf9y\xf7\x83\xfb\xea\xa3R\x9f\xc8\x85\x12\xd2\xeb\xd7\xffpd1Y`,\xb0\x85Q\x87/\x8d\xda\x8bRF\xec\x8d\xd0\x92\xe4=Q\xb1\xa9g\x98\xba\tS\x837\x9b\xce)\x8dZ\n\xf0\x12\xae\n\xa0M\xdam\xf1\xd0\x11\xeeOg\xb5\xa7\xeb\x04K\xcc\xb1N\xa6\xd5vZ\x1d\x9bD\x90\x8c&R\xc5\x1fX$\xf3\x94[\no\x14_O\xf8ao\x86\xf8Bco0\x9a]\x04\x98\xf2\x07\xd7ZL=\xd5(\x84\x95\xc3\xe0\x82\xddT+2+\xff\xb0\xd3\xa6\xcaw\x84\x93b\x9bs\xb1\xcd]\x9a8(Qc\x80\xa8~\x07\x06?A\xf7@X\xf6vg\x8fn\x83\xbbcy\xfb\x1c\xd0W7\x9az\xc1I\xcc\xd9=g\xe6\xb2/+\xdc\x1e,F\x0b\xe3\x82\xc5\xd8\xf4-lon\x05\xf8Vv\x16\x99\x00\x9f\xdd\x11\xd8{\x91\xff\xe0R\x8b\xf1\xb9\x7f\xf4O\x02\x1d\xb6\xc0\x1d\x08W\xea\x06\xe1\xb9\xee\xb2\xba\xbam\x80\x89\xda\x12v\xea\xc2qq\xb1z\xa68\x04n\rj\xa0\x91\x14\xfc1F\xb8\xac\x83\xab\xc8\xc2\xc0\x9d\xeb8\xf0\x16\xb0 \x1bjp\xe3\xad"%\xb69e.`-AP\xe3%\x8c\xe0t\xf1|\xf2\xd3\xfa\x19\x9e\xff\xf0h\xf7\xcd\xfe\xdb\t\x98E\xadiL\xa5I\x80Wv\x83P\xe5\xc7\xee\x17\x90X\xb6C\xef\xaa\xb8M\x8e\x0f\x8fj\x95\xfb{38O\xa2$\x9c\xb8\xfd\x89\x01\x05\xfb\x0c\xaeP\xd2L\x9bp\n+\x19\xd3\xb4\x0c[Z,\x9fi\xb4\xcb%\\D\xfa8VE\xe0\x12\xe0\x8d?`n\xd6"\xd3\xf7\x0f\xb0\x9a\xb1\x9f\x91p\xad\x85Bv\x1cy\xa4\xd7\xd34\xc2\xaa\xd3\x0b\xcb\xcat\x87pU\xa6d\xd0\xda1\x86\xcb:9dj\x01\xdb\x88\xe9\x03L\x00\xcc0\x1f\xed\xb3\xc6\xa3Z ZHv\xb5Z9N1Q\xb7o\xda\xef\xe749\xc9OR\x1a\x1b\xecT\xd6^\t\x900\xf9\xf0\x06\xb9\xcd\xdar\x9f\xa9L\xee\xb4\xf3\x88Ro\x01\xdc\xab\x044\x81\xb8\x8a7\x08\xe9&m\x08\xee\xd5\xad\xc7\xc8\x1d\xbd!\x98\xd9o\x00\xe18\xfb\x14#\xfb\xb5\xa0\xe2@3\xbf\xd6G\x13I\x06\x071\xefe\xee\x91s;\x9a\xf5\xe0}\xf3\xb1w\t\xc3\xce`d\x1d\x8c\xf4\x9c2^\xd8\x99\xbf\x86\x7f\xe2\xd6\xf8  \xdc\x14\x9d\xbb@\x83\x908\xad\xd1\x00{\x12\x9b\xff\x88W\x80#\t\xb9\xb8\xbb\xc4\xc2\xc3j\x00\xd4\xa0(\x16Up\x80YT\xa3$^\xbe\xfcH^\n_p\x95J\x0b\xd8RG_\xeb\xfb\x98,\xca9^\x93H[\x04\x02D]\x0e\xe0\xd2\xdfs\x97\x08\x82?t\xada|1\x99&\x91\xb1\x89\x12\xf3\xb6>\'g\x04\x88:\xb7\xfa\x1eS}\xc6l_\x18HN\xd3\xf0j\x80u+\x19\xe39\xc1R\xb8\x08\xb6\xdb\xff\x01~\xd9\x0f\xc2\x83\xbf3\x8f\x97\xa4\xd5\xd6K\xb8\xc9\x0e\xf3\xd6\x98-\xe2\x82MD\x88\xf2\x17W\xcd:7s\xb6\xf9^!\x19\x9ei\x07i2A\xd6{\x0c\x8f8bX\x05\x97\x82\xe3\t\x9f\xa9\xd7\t\x8e\xf0\xden\xa5\xce\x89W\x89 \xfc]\x14\xd5\xab\xfeE*\x00\xa3\x03\xc1q\x80c\x89d\x89\xe6l \x7fY\xad\x90#p\xbc\x0f\x13z\xc6ya\xb3D\xc7\x83\xd0%\xe1T\xee\x92s\x04I\xb1h\xee\xc8\xba\x83\x8a\x1d\x8d\x1f\xe7f&\xea\xa4\x92p\xc0~r\xe1VF\x9c\xb7dt2\x9d\xa1u8\xbbL\xd3k\xc2\xc5\xe3!\x06\x8a\x90\xf6\xa9\xcf\xf7[\xee5l\xa4\x0e\xbb\xdc\x0f\x89#\xadB\xa5\x9fT\xb7\x90\xadu\xd8\xbaf\xca+\xd2&j\x7f\x86\xfe\x1e\xf4N\xa2\xc9\xd1z\xba\xe7\x0b<\x1cV\xca\x0c\xf3\xdd\x8f\xc7XE\xbf\x87\xc5\x98\xe6\xce\'\x92\x83\x7fT1\xc3+\xc7\x15\xa1\xacw\xfa\xa0}\x85G\x81\x1a9\xa1\x17\xd3\\\xd7P\xf6\xe5)\x12\xb7\x06s7\xd9\x94\xe6l\xa9l\xf2\x08\xa7\x84\x91\x86x\xbc\x82y?\x82An|\xa4\r\xd4\xed\x1a=\xdcct\x1ep\x04\xb3\x8c\x89\xa8\x99\xd3\x8cr\xc1~\xfa\x04\xbc\xbb\x7fy\xb2\x1f\x87\x19\x14d\xbe\xed\x10\xbc\x082Cu\xc4<?&Pc\xed\xf1\xae\xe6)9]F\x02KB\x00I\xe2+\xac1\xb4\xb3(\xcb\xfe\x07Q!\xbe\xfe\xa8\x046[WH\xb4_\xe9\x99!CT\xce\x7f#X=\xd4\xf4\x94\xf9\xe4\xa9fL\x06s\xcao\x14m\xfd\x17<\xacf\xbcC$\x94\x98"\xb9\xda\'zY[\xa6d\x16F\xc6\x87\x87U\xf5&\x81\xf6\x86#\x96\x9c\x04\x0c\xd6\xd5\x8f0#`\x0c^\x97\xd0\x93\x03\x9d\xe7G\xa7\x18\x051I\xaf\x89u\xad\x13N\x12z\xa4<@L\x05B\xb9\x9bb\x8e\x00\xb4\x93\x00\x9c\xcd\xf4\x03\'\x98Y\xf2\x8e\x19r\x17\x93\xce\xe7H\xae%\x1fm\xe8\x00\xa6\xaf\x80\xc6\xf6R\xd1\x10\x82G\xd8\x14\xbdaS\x07\x00]\x11A\xdd\'\x8f^\xf0\xb3\xb5\xdde\x8e\x81\x97%\xe5\x83\xb54{4!lIS}S\r\xb0\xd1\xf8g\xf8\t\\)X\x98\xa9\xc5\xd7\x9a\x1b4\xed\x03%\x9f\xb0\xb3\xe4j\x03\xd8\x85\r\x93\xf2@I\x93n\xd5\xe8M9qE\xef\x10}\xc2\xab\xb6Y\x13+b^>\x11+\xbe\\\xb8\xdc\xffM\x91\xb8)\x7f*\xf7K\xaa\xe9\xaf}~\xa4\xbb\x99\xf0^\xa1Z\x19\xfc\x8f\xf8\x11\xdbC,\xc6\x03\x1ao\xc7t\x7f\xaa\n\x16\xe8N\x8e\xea\xfb\xa5\x1f\xe0\xe6\t\x87i\xe7oyCa\xb3\xd9\x07:|\x84\x89a\xe5\x81\xd01\x14\xaf\x11\xd7e\xfd~j\xea!lx\x10rV"|\xea7Q+\xb1\x0f\xd7\x8e5D\xaa\x12#\xb2fF\xe5\xc6\xe4\x0b\xe3\xf4&\xef\xff\xb10Q5\x85v\x8b\x90\x9e!/\t\x0f\x88\xb9X\xa3V\xa3\xba\x14\\R\xeep\xd5\xc5n\xda\x81E\x9c\xf4\xad\n%\xb6\x1f\xbc\xea\xe6\x101\xf4\xbd\xde\xa6\xe2-@8A\xbe%z*\x05\nZ*iE\x1b\x99\xfe\x8e\x9fck/f\x14\xc4#-$\x81\xf2\xe8Dl\\\xc0\x10\x96\x81\x00\xee\xba\x8f\x1bL\xb6\xda\xe2=\xf2\x93\xd8\x1e\x0f]\xaafg\xe7\x89n\xb2$\x99\xea\x80q]\x17\xbc~\xaey\x83\x9b$V\xd4nL\xc1\x04\x0cZ>\xa0\xb5\r\xd7n\xfd)\x81L\xe5\x83!A\xb0\x05N\x07\x9fr\xa2\x03\xa7\x80\x14\xb7sq"a\xe7\x92C\x12\xee\nz\xdb\x9c\xd2\xf6qs\x9bN)\xad\xf0\x8c\x14\x89\xc0\xe7\xc4\xe4\x82\xf2%\x0c\xd2<\x9e\x9e\xe8\x9d\x1eak\n\xe6\xb3\x92\x91K\xc8\xdb\xd7\x08_0\x00\xd9\xf4\xbdjc2\xa2\xea\x17\x15\x0fa\xa50\xd4v\xf1\x9bb|\x01\'\x93<\xc5\x7f\x87c\xff\xa1-%\xc9\xe7\xcf\x15wZJF\x8a\x9a\xb5\x96\xdb\x84\xadf\x10 \xac\x16\t\x84\xe9\xe5\x0c\xee\x80\x1a\x1f\xcf\x1ec\x1c\x0b\x1c<P]4\x16\xcf\t\x99j\x89!Mbhvqp5\x0cR\xd4\xbe\x81}.\x8d}\xb8\xd0\xc4=\x90\xb3\xc7\x84~\xe7%\x1dxy\xd2;\xc58\xeb/\xaf\x96D\xba{{\x83\xb9-\x11\x15B\xfdU4\xca}\xda0\xa6\xd0\xaarcM\xf1\x8c\x132\xed\xc3\xef\x8c\xe9\xa0\xda&\xbe\xd7@\x9f\xc0\x10\xdcK\x00\xba9f\x0e\x82u\xad\x95\xa54"\xe2\xac\xf3\x05\x89\xf8\x9d+vO\x95\xa8\xd7\xcc=\xc4\x94\x93\xcf4]Q@=i\x08\xf4\x10\xf8\x1d\xb2WSL\xc0h\xe7\xb6\xbeH\x82\xd2\xe8*\xc3\x9a\xe5\xb2\x12\x01\xbf\x9a\xfa\xf1U\t\x80\xed\'\x06\xfc\xb7KCz*0\xe2\x86\xc9\x8e\xa6\x97\xd8\xe7\x06\xf8\x0c\xc5[tN\x91A\x9f\xbf\xdd\x84\xb7M\xdf\xd9\xd1;\xaa#\x89y4#\x08y\xaa\xa8)\x9e\xae\x0c#(\xa3m\xb3y-\x93`U\xc2\xf26\x9f\xe2\xe3S\xads\xf8\xa1\x01\x15<\x84?\xad\xe2\x8e\xcb\n%*\xb0\xdab\x98h\x1c\xb2\x82d@\xc8\x17\xf8Fu\x0e\xc4|F\x0c\xc4\\\xa4\xc6P}\xc5._s$56\xd0d*\xd8\xc2I\x84\xd85\xa8\x8f1\x7f\x07\xed\xc4b\xd9\xb2/z\xdc\xff\x9a\xefi\x81\x8d\xe8#\xf49\xf9\xc6\x00\x06\xde\xeaJ\x8e_\x9e\xab\xd4\x1f\x1ed\xa1\xa6\x81\xdcJ\xd9\x10\xb7@\x98\xb0BU\xc4\x00\x82\x1b\xd2\x8c\xdc\xd3\x92Eh\x8a\x9c\xa9\x8f\x13:\xc1d\xd0\x12\xe0EVi\xbe*v\x08\xd3\xfb\xcd5\x14\xb5\xba\x94q\\a\xf9\xe0\x9b\xf6\xcbW\x1a\xb7d\x8a\xb0\xc8\xf2\\s\xf9\x969YR\xed\xf1\n\xf807\x1b\xae\x88m+\xae\xf5qXC\x0c\xb3)a\x94f\xeb%\xe3z\xa2\xea\x8e\xf3w0\x05\x18\x89s\xefh$L-\x17\xf4\xe1\x88\x1au\xbb\xb1\xcd\xcf\x99v\x8b\xb1\xb7\xf5\xe3\xfa\x9b\x00pA\xad\xc2\xb7\x03\xd8\xf4\x19\x98c\x93\xe5\x9aK\t\xd5\xf0\x13X\x97\xa5\x9e\xd4\xa8\x10\x19\x81\xc9\xc1\xae\xfeR]\x0e\xa5\xc7\xb6:\xc3\'~\t\x19l6O\x15\xf8`\x91\x12\xdb\x1b\xcd\xe0\xec\xe3\xbe\x99\xc2`%1.`\xbf\xe6Jel\xdf\x12\xf3\xf0\xe9X\x8f]\x02\x99\xea\xaf(\xc0\x96\xf3\x00\x1c\x08@\xe9\xe2\x17&\n\xa1\x9a\x97Hx\x89\xe0zK;h\x9a\xc7z\xa7\xdaml\xfd\xc9\x9f3V\x1a\xd4\xab\x05\xf5\xe3\xb1*>\xf6\x96A\xbe\xee\xe7|\xf0\xc7\xb4Tv\x92(u\xcc\xe6\xc2\xd3\xe1T\x81\x18&\x05\x95\xc2$\xd0\xc5r\x88\xa5\xe5C\xcc~v\x14\xcb\xf9~\x91\xb1O,._\\\xc0\xbeNa\x05\xf7a\x9f/1N\xebqe\x98\xe3\xaa\x07\xbf\xf4T\x83`e\xd4\xa6\x0b\xa2\x83u\x1ba\x90\xa1\x15\xb6\x8f\xab\xc1\x8e\xa4\xf8]3\xf6\xfb\xc8\xbfa\x83u\xad\x89\xb8(\xfeQ\xc3uQ\xa8FS\xd0\xfe`\xfc"\x1c!=\xed\x93\\\x04w\xa9+#\xeb\x93\x98Sn2\xa1l\xf3\xf7\xb0\xe9\x17\n{\xf9\x81bx\xc9G\x01\xed\x83T\\p\x97\xe4\x05\xb6>L"}\xa9o\xc7\x06\x19\x94\x01(mv\x86\xb0\xbd?\xcb\xad\x00\xf4\xba\x8c\xd6*U\xc1\x9a{\x10\xa4B\xf2\x11!fyci\x98|:\xb1\'\xd8\x90\x84\x97\xfad~,%wJ$u?Tt\x88\x1a\x8e\x95\x8cY\x84\x80&=\x01\xccT\x8c\xae\xe0\'\x88U2\xdb\x96\x86\x1f\xed\x05\x89Z\x12O\t\xe9\xd8\xfa\xd6\xcc.\x0b*\x8b\xbe\xa0dA\xaaZ%\xfd\xc6\xe5Z_\xc0lD\x1c\xb7\xaa\xbaJ\x92f\xdfj\x8dB\x84\xff5\xde\x03\xb0\x97\xd8I\xf5x\x15*E\x91(\xde\\a\xf5\x9e\xdci\x80\xd2\x07YQ\\d\xe3\xc0\xac\xa4\xd2\x0b\xef\x02\xeaF}\xa5\xd6 \x1e]=\xdf;\x1d\xfd\xfcQU\xa5\xea\xf9\x8b\x17\xab+\xffj\x1c!\xfbr\xfc\x88\x03\xb2\xf5\xdd\xfd\x0e\xccf\x8837Z\xda\xefnw\x89\xe1J\xa6|\rBv\xd1\xbb\xdc\xb8$\xae\x02\x8b\\)\x08\xb0\x87D\xb1\\ R&\xc5S\xcd-\x14F\xc52a\x80\xa84\x8b6\xee\x14\x04@\x89\x84\x02Z\xd5W\xd1\xc8\xe3\xb5w$H\xe7\x89\xd4\xa5DU+fU\xccS)Zt#)\xbeV\xb3=\xaa\xcem\x8e\xbawS`.\xee\x97L\xae\xdc\xfc\xb0\xa1\xb9\x97\xff\xc0\xb4\xa8\x89S\x8cHR+\x08\xd9\x96\x86\x84\x08\\\x05\xab\xf2\xd2|2\x04\xc9\xb3\xfd\x81\x81\x94\xbf\xb9\xc4\xb6\xd6\xf5\x82\x9e(x\x1b\x8dV\\<\xf2\x92D+\xc6\x01;-ux\xc4G\xa1 bl\x9f\x80\xd4h;\x02\xbc\x99V\xd9\xad\x98\x05\xaa>\x92\x94$t\xc8$\x03\xabM\xafa\x82q\xfa\x9c\xb7KR\xf1\x06(\xbe\xe0\xb8\xa0\xf7MD\x12\xdb\xfc\xc1\xe6\x04\x15\t\xc5\x0b\xec\x0cfR\x00Zst\x8b\xe4\xb30\xcfK\xb53\x8f\x122`\xd5\xb67$\xdb\xb1\xe2\x07\xa5\xe2\x07Xk\x87n\xe0\x1c\x0b\xcb(\x0f\xe6\xd32\x82^\xefo\xdfOk\xc6\xc6\xd75\\\xe4\x83p\xbf%\x06ckw\x8e\x9f\xc0\xdd\x07Q<\x029\xf8[^n\xda\x9f\xf03\x916_\xe8\x96\xd7\xf3\x9f4&\xd6\x9f\xb0\x8d\xa3\xc3\xa8\xaf\xa3V\xea\xdc\x94\x88-@U\x00\x8fl|\xf1n\x10\x08Z\xbez\x8c\x95iOv\x86\xfb\xcc\x80>a\x92ksE\x94\x11\xe7S%T2h\x11ZU\xe7q\xee)\xd1!\x84\xb5\x8b\x1f\x9b\x7f\xae\t\x02mq\x80\x0f#\xa8C:\x043\x03E\x12\x15\xc9\xfe\xe2\xa3L\x1an1\xa1\xf9U\x80\xbe\xb4\xc3@\xe0\x17&\x8aMJ\xd6PI\xc6\xa2\xb7Zc\x91\x82\xa0Y\xba\xdc\x14C\x0e\xcb48SRh\xa1n\xf4\xb7\xa0\x85\xe7\xdf\xa88\x97\x16}\xf6\xf5L\x19\xa9kF\xa7\x864\xaa\x01\x19$\x8bp*#\x1a\xed\x153\x065\xc4\xe6\xb8\xa7%It1E\xa3\x89CR\r\xa9\xacS\xab\x14o\xe2;-N`\x15Ei\xac\x8e\xe7\xe0Yg\x98>*gvg\\s\xbc\xc8\xa1\x85x\xa7\xf4*ey\xfdt\x12\xfeQ\xbe\xd4\xa6\xb8\xb6]\xfaJb\xef\x8bo\x08\xb5\xd9\xd9\xb4\xb2\xba\xa2\xa7\rvB\x82\xae\x94c\xf6\xf9\xa32\x19l\x9c\x90#Do\x8b\x0c6\xddVr\x9di\x06\x86\xd0\x00\xb0\x94\x02/\\\x19\xe25\xdc\xb3\x8a{\xf8\xd1.\xcdad[\xb8\xfa\x80\x97H\xf1\x1cx\x1aF\xe1\t\xd2\xce\xa7\xe2\xbd\xf0~\xaf\xd9>\xd2*\x8au\xbf{#\xbb\xca]\x8d\x92\xebD\x0b\x17R\x88; a\xf1Zup\xda\xf4f\n(\xf6\xe13\xa0\xfd\x1d\xc6\\}\xd8\xa8\x94jY\xc5.\xb3\xa6[ \x85\xacaU\x0b\xa4\xfd\xf1\xaeOc\xbf\x12\xd3\xdbp\xb1/p@_\x95E\x89_\xae~\xf6\xb4q\x0e#z4\xfd\x90\xcb(\xca`6\xd6\xfb[\x1dn\xc2\x7f\x88\xf0\x0b\xbbC\x9cf\x9d\xfd!\x00&\xed\xbf\xc5n\x85u\xa3KH\x8a\xcb\xf5\xf50\xafq\xc9\xbe\x06\xaa\xbfm\r\xc2\x19\xc2K\xb5@\xa7e\x89*\xce*?\xb4\xcb\xaa\xa5\xaa\x98 \xca.\x98\x9a,\x1bR\x81f\x9e\xc6\xda\xf8\xd9-.@\xeb\xb5\x83EZ\xee:D\x1d\xc99x\xa4+\xfd\xee\x93`@\x0b\x13\x8f\xa47\x1d\xea\xfd\xed\xaf\x91\xeah?\xf5\x04M\x15}\x17\r\x071,\xeajk\xe1\xd6\x80\t\xdb\xe4\xd7\xff(\x96\xce\x7f{\x00\xff\xc0\xa0:\x17\x1b\xe1"%\xdd\x83G\xc8\x0e\xa4\xc5\xa7z;{\xf2\x07\x96&\x99t\xc5\xa9\x8a\t\x1a\xe5\x1e\xec\xa8<\xe7\xe8\xb1g_1/Q\x9b\xa4\xf5h\xc1\xa3\x03\xc7\x15\x9c\x8bd\xd1\x89\xcai\xc5\xf7\x07\xf0\x05\xa9p\xee?\xe2\xbdji\xb5\x18\xfd\x97^\xb4RB\xac\xef\x95\xc9\x82\x94T\xdb\xbd\xbf\xddr1\xbcCLC\xb5\x1a\xb8\x86g"s\x97\x06,\xb8\xb6\xd3\xd7!{X\xe5\x94\x9d-\x9e\x03k\x92\xf5s\xa2T\x0c@c\xc42)\x01j%$\xda\x9b\xf9Kf\x19R\x96\x17\xb99\xc9~\xebg*\xfa\xa0\x90\x1e\xec\x94\x1b\xe5\xbe\xf7{\xc5\x047\xb4\xf9\x04HZ\x17\xff\xd8Z\xd3\xec\xad\xe0\xb1\x82\x85\xea\xfb\xa2\x9f\x84\xc3m\xcc\xdf\xfe\xd4\xdc\xb8d\x9c\xb5\x9a/K\x7f`\xb0\x03\xb2\xde-\x95\x97\x0b\x0eO\xc8\x1dbn\x80\\\x90\x9c\xdd(A\x93\xae\xd7wS\xb8\xdeK\xa2\x81\xe1\x98\xc3;\xc64x\xb1\x04\x12$\\N\x92\x839\x98\xee\x89.]\x9d\xden\xaa3\xa6\xcd A\x8e\xca\xf2\x1d\x8d\xb0n\xf6U\xd9\x14AF\n-\xbe\xf9s6\xa1\x8a\xa6P\xf9\xcb\xde\xdf\x92\x82\x8b[\x1b3\xf3\\`i\x7fS\x12$\xcdh\x89\x98\xa1;\xa4\x13K\xbf\x11\xa8\xb7\rD_\x89\xaa\xb5\xfe\x9e3\x9c4\xe8Z\rZ\xb3\x88\x16M\xd0 Y\xce\xff\x10\x03\x00kC\xcd\xc6jHI\xfc\x13\xc4\xf7\xf4\xf3-`z\xea#\x91OB\xb9U\xa5\xae-&\x9ec\xe0\x1f\xf0\xe4\xb6\xdf\x82!j\x8b6\x968t\xcfI\xd3DA&\xe7\xd1\xe2!r1\xec\xba\xa9\x17\x99\xea9\x0cX\xd4\xc8\xf4\x89R\x0cp`)\xf0\xa7\xaf\t[\xc2Ka\xc7\xd5{zv[k\xec\xaeV\t\xaeF$\xe8\xde\xc8#X&Z$\xd2\x0fL\xd6\x12\xe9\xf8H\x08]\x92\xbd\x95\x0b\xd7\x83\x18\xa6\xa1\x07{\xed\xf3\xb1,Nt\x96\xf7\x98\xb1#h\xa1K\xba\x0f\xe27L\x068\xe2\x9a\t\x19\xc3\xe9\x93\x07X\xbe\xb6~\xcf]\x8d\xd5!DF\x94\xc9\\u\x00:\xeb\x0f\x96H/mu\xa9\xf9\xa8M^\xab\xfe\x97)rb\x95\x82\x064X\x10h,\x96EX\xa1\x99\xe2/p\xa5\xb6\xcc\x01\xe2\xf9\x9d\xe6wv\x11{\x84P+\x8d[\xcd\x80\x8aD\x81-\x16\x10\x10\xdc+:Z"\x8dPj\x1bR\xbaJ\xcf9/\xaak\xe3\xdc\xd7\xa6\xd0<\xbfi\xb2a\x80\xf0\x14\x19\x8e\xf4\xe0u\xb8\x05\x81\x07\xdat\xe8S\x97\xf8\x0e\x1e\xf5\xebi?\xfb\x16\xf2\xf9\x98\x8fi`\xcf\xd2\x85\x85\x1e\xd7\xa0]\x1cm\xfakK\xf3O\xab\xecXDU\xf3\xedZ\x99\xb8QU\xa6\xe2\xbb.\x1dW\x01 \xf1\xf7hx\xf13\xf7\\\xbdZ\xbb\xbe\xa5\xeb3YP\xe9\x87\xd9t\xe98j/\xcciw\x85K\x16\xb5i\xd5)^\xb4\xd2\x94(\xe5\x86%\x15vsBD\xab\x08%\xfd\x0e}\xfd\x12\x93\xaa\xd7\x1e\xa8bT\xd3j\x849\x08\xafp\xaf\xc9\x93\xdaf`V*\xf0Cp\x99\x85\x17\xbd\xbfM\x10IZ\xa1$\x7f\x0f\xd8\xc8\'\x08\x8e\xe2\xed)g"\xa5L\xe9\xfe=z\xae:ZM&\x8e5\x92\xb6T\x18Sku\xef4\r\xc6\xe3\xfb\xf4(\xd1\xd4\xa5\xd5l#I\xe6\x95P\xc2\xf1\xcb\x97\x98\x9aU\x85\xad\x8b\xfc#\x9eI]4;7h\x0e\r\x87\xabK\x8c\xcd\xad\xea\xcb\xa2\x83\t\xc6\xcd+i\x08\x0fU\xa7\x16\xce\xf8\\\xb7,\xd9\xc2\x84\x8a\x8f\xff))\xad\xb7\xb7T \x13Y\xfb\t\xac\x1e5\x13h\xd1l\xd8\x84\xf1\x0e\r\xff\xd8\'\xa2\x9d\xf0\xb1\x92\x17\x8a\x1a\xee\x80J\x11\xee\xd26K\x9c`\xd0\xc8\xd4enD\x01\xa1\xa5R"\x7f\xfds\\\t\x93\xe5"H\x19$\x9d.\xccC\x0cA\x97\xd1\xa2"(\xbdq\xc9\x1d7\xdb&s\x8c]^K\xa7\xd6r\xd8\x8c!D\x0e\x0f\xe0k\xab\x97\xbf\x19n\xb0`A\x1aR@\xd2\x10S\xa5\xc1\x0cYl\x01\x95/\xd1\xa6p\xd1\xc1\x00cA\xeb\xbf\xd2^S\xcc\xeb&\xe7\xdf1\xd5\xdfk\xb3\x1cl\x88\xcf\x14\xa74c1\xba\xe76\xa0\x81L\xcaV\xdaA\x1e\x94\xdb\x8b\x1e\xa9\x1c\xca\x94\'\xaf\'\x15\xc4\xc4\xa6pM\xd0\x9cA{\xb3;\x02si\x08\x97\xa2)\x02\x0c\x9a+\x95\x8aE-i\xb5\x99\x92\xad\x06ST\x9a@\x98\x12s\xf4\xb8\x8b\t#G_6N\x9e|A\xf4\x82t\x00\x13\x0f\x88\xa4\x12\xd1\xa5\xcc \x94\xfc\xd3&nx\x88\xdev\xd4UM\xb6\x82x\x1d\xd6{\xda\xdc\xe9z\xdaW\xf0\x96\xb4\x1f\x13\x12!\xa1Q\xb0\x016\x80\xdcIo\xbdj\xc0I}E\xb3\xe9w\xf0\xc8\xc9\x85\x9cA\xd2:\xd2\x00\xdc\xc5\xb9A\x8c\xba}\xa4|5\x14S\xa8\xe6:\xbb6H\'\x11li\xa56\x0f^b\xa5\xa0X\xbc\xc1F\x0bCs\x13\xab\xd2\x93\x9dS|\x81\x05\x0b\x87)\x96z\x7f\x95\xffn\x95\xd0\xc7\x9c\xfe\x80\xa8`\x16\xc50{tXkEw\x8e4\xa0\xa6\xee\xe3\x1d\x9c\x08\x99E\x1c\xbd\xb8c\xdc\xae\xf3>-\x89d\xa1lt\x9b\x9b|\xbc\xa5JH\xf3|\x81\x03\xb1\xc9\xe4\xbd\xeak\xbc\xe8\xe9\x13\xfb@3\xee(}\x10\xf0\xc2\xf4\x0eA5\x7fPk,A\x02\x886\xe8P\xbf\xbe\xab\xe7\xde\xaf\x9d\xce\xbc\xc5\xf5k;c\xb4\x0e)\x98k\xb9^r\xd4\xa89\xad\xdb\x06\xb2\xc8\xee\xc3\x1b]\xab\'(Z\x1c\x88\xc2C\xa5;\x19\xb6\x9d\xdf\xcdqr\xd2/\x80}+QM\t\x1f`\xab\xcf\xfbo:q\xa3\x97p\xc1\xd5i\xe5P\xa8\x02X\x15\xa1\x9d\xb0\xa5/\xcaV\xfc,0\x03\x9dj\r\x1a\x84\xfc\xc2\xbd\xa6\xcf\x18F\x1b7~KG\xc7\xb5\x065gfv\x94\xadc\x1a~\x0e\x16\x87s[i\xb3@\xdf\xf2\x7fu\xe8\x81k\xf2\x86DZF\xc2OM\xaeA\x03\xf2\xcb\x8f\'\'\xaa\xecZ\xc5\xdc\xc4\x9c\x03\xac\x8bJ95i1\xa58p\xc1\xda\xdf0\xea\xc2=#\xbav\xe4\xa0\x82\\>\xbb\x82N\xae\x12\xe9\x1a4\xe5\xee3\x98/\x9aG\xea~I\xc8,\xe8\xc5\x95\x11I\x1a\xdc\xd1\x82\xedJ)\xc2\x88\x11J\xed\t~\x91p\xabIKT\xc2\x84\xa6&=\xbdzdLZ\xec\xfa\x1d\x9d\xe9\x06\x1al\xdc\xc1\x1eZ\xca\xea\xec\xbcR\x81:\x85\xc9\xbaO\x8f\xb6\xa63\xa9\xb7\xfemp{6\xc5\xf1{\xed\x99\xed\x97\xdeb\x84\xe4\xc2\xa6\xfbW/5\x1a\xb5\xb34\x1fW=Q\xd4,\xe8\x1d\xd2,\xe8i\xe0!\x8cc`\xe8I@Z\xd5\xc8\x91\x14Ir\x10m\xdc\xb8\xca\xc79\xd9]]~#\xa8\xb9z\x98\x0b\x8dx\'\xb2&\n\x93\x16*\x9f\xa4\x9c\xa2\xd4\x95?\x9f\x90W\x86f\x9d\xba\\\xab\xc9\xbf\xc0\xab\x1c\x9b*%\x17[Q\x88l\xb6\xd6\xeb#\\/\xc7~\x8e\x19t%\t\xc5x\xdb\xec3\xf6KQ\xd8\x85\xa9\xe3\x9b\x05]\x08\xd1=\xbdf&"j\xf0\xf4\x05\xbd\xae\x02\r\x92\x86$\xb0\x0es\x80\xcd\xad\x1f\xbcS>\xa3\xfd\xf4\x8d\x9ecp\xcd\xad\xe2\x9d\x88\x1a\x15\x9d\xb4U\x8b\xc0JH\xff\x83\x1c)\x1b\x04\x15Z\x9e[\x06\\\xb8\xf8\x89a\xb7\xd16\xf9\xa4\xf9\xadI\x86\xca\xf5r\xa8\xc1M~\xff\xb5\xcf\xa1\x854\'v\x05#\xea\xdb3~\xae-?\xeb\xc8\xb0\xd3\xc9\xd8\x01v\xf5\x01\x8aS\xd0\xc6D\xfat\xc8\x80l\xa1\xe2\xabC\x83\x8253S\x9a\xbc\xe8\xa1\x9d\n\x8a\xb9O\x01\x9b\xa21H\xccY\xc2q\x9b*\x10\x0c\xa4\x90o\xe5H\xcf\r\xc7.\xbd\xd4\x89V\xd1ZM6\x82\x16%Z\xe9Xy5\xfc\xea\xc7\x04\x01\x1f\xd6%%k)\xdc\xfd\xc1\xf9\xb6\x04=\x81\x11\xfbW\x07\x9cUJ\x94Y\xb9~Wu\x0e\xe5\xce-\xaf\xd6\x9a@8:w\xd4\xa3%\xc2\xa5\xe1\xdb\xd5\x13l?\xba\teMaj\xf5\x83\xde\xbfC\x8cR\xb6\xfc\xa5\xa2r;%%"\xd1\xf0o{\xe7\xa5\x8ao^\x14\xb5\x0f\x88\x02\xee\x8cs\xb0\x8a\xe3\x8d\xe4\x15h\xbf\xec\xacm\x8b\xac%\xa0\xf3\xcb\xc9F=\xbc\xa1O7\xee\xb1\xe8\x954\r\x9f\xe3\x94]\xe3v\xd0\xa2\x80skA\xba\x95\xdc<a\xb2\xd18a\x84~Li\x8e\xa2\'\x8a\x1a;S\x02BjT\x03\xad\xd6eE_\x90t\xac\xe1\x93\x13m\x18\x90dZ*m\xbbo\xe0\x92~Cn\r|\x8akX\x8a\xeb\x01\xeeS\x92\xdc\xf7\x05\x1c\x12a\xa9U\xa3"\x85\xd5\xe6\x01\xbb\xfc\x92C\xa8\x8bu\x02\x8c\x91\xec\x0f\x08\x15V\xa4F8F7\xb0\x01\xaa\x1f\xb8X\x07%\x97 `\xe5\xc0\xaerl\xadh\x06\xdb\x17m\x1eVt\xeeD\xe5\x8c\xd0?\xee\x16)\xa8\xd5\xe9\x9fIyw\x84;\xc3\x0e}i\x8e\xde\x1f\x9c\xed/\xe8?5N\\\xa6\xf8-\x10\n\xe9\x06\xaa\x9f\xc9\xf7{<\xe2\x1b\xb4d\x1b\x9b\x87==\x02[>\x02\xc8wC\x906\xe2\xfd\xe7\xc7X\x17tF!\xc1\xf3\xda\\\x19U\x99\xb0\x8a\xc5B_\x11\x9eQ\xce\xc0\xa2\x04)[6\x84s\xf1\xddnP\x97\xcb\x8bt\xdd\xa0\x9a\x97\xf7\x8bd\xb8\xec\xc9\x98\xf8D+\x14\xe9\xca\x88I\xa4\xcah#\n\xde\xf1P\xb1\x99g\xa92\xbam\xd3o\xe3\xc9IACz\xaa\x0c\x00\x10\x84\xe2\xba4)i\x96\x13\xd5\x0bC\xf3bWS\x084\xeeH\xadOr]iw\x9e\x9cg\xd8\xefn\x03SvW\xdfIlb\x82\xb6\xb0\xfe\xde\x88\x07F\x9aT\xa8\x9fI\xc5vB\xd3\x99\x96@\xee\xb2\x13zd\xd4\xce\x05\xc9\xb4E\xb2@c\x90\x1cA\xd2\x9cN\n\x088\xe3k\xdd>L\xba\xcfbc\xbf\xf9\xbaQ\xf5\xb7\x0b\xa8\xf1H\x95\xf1J\xba\x0b\xff\x83P\xdaL\x9fM-\x80\xba\xba\xf4):O\x9b\x97X\x074\x81z-eHTq\xaa4\xd78L\x90h\x9d\xbc\xad\xec\x00\xd6dN\x85)p\x8ap\xa3\xcd\xb8\x12)l\xc0*\xb5\x87\x9aoI\x8aP\xa9R\xac\nq\xab\xa7^L\x12JM\xa0\xcd\xcc\xc1\xd6\x1c\x0eW\x88\x90\x9a\x90\xd8\x87\xa0\x9c\xd5\xcf\x1fH\xa3A\xa0K%\x85\xde\xbb\xe4\x08\x92r\xf3\x07\x89\xbe\x08\xf2\xb9&\x9d(|\n\x1f\x00\xd1L\xd0\xca\'\x89az\x0f\x8b\xab\x01k\x06mc\xbe\x1eU\xad]w\x1dH-\xc6\xd7\xf1\xe2|\x88\xb8\x1b\xecOi\x95\xa8.\xfeI\xd5\xd4\x9a\x8eUQ\x96\x0e\x96QN.\xb1\xed\xbf\xed\x92\xc3\x08\xf9\xec\xa3\xb7\x00\xa4\xd7\xcfxE\xb0\xdb\x8a0\x95\xa6\x91)\xc1Z\xc6)\xbbY!\xda\xfaa\xcdL\xa0>\xd5\xc2\xffZd\x82\xf5\xa1.\x93\x1e!\x90>\x06\xd1n\xb4\xfd?JC\xc8\x95"\xbav\x91\x88$,g\xc4Qn\x84\xc8\xd5\x07;!\x87"wH\x01\x17\xa2\x94\xddWb\xde?\xec\xe2S\x91\x83G\x15T\x8d\xa4\x03/\xb9\xe8\x92y\xc9v\xa1\xdf&\x15D~tQo\x91\xb7$Z\x9f\xb1\xd9\x80R\x84\xf8/+\xc1\xc3\x9c\xfd0\xd3\xd3\x83\x96=6\xc7\x89\xc0\x18H\xff\xfa9\xb6\xf3\x17\x12\x0f\xc7\xfdW\x1c\x07\xac\x0e\x95\x8a\xc9\x81\x064\xe8\xbaE\x14\xc0\xbcYA\xfd/\x91*\x99E\xaf>N\xf4;\xf0t\x1e.\x19T\xad\xdf?\xb8Q\xf0LG\xbf\xe6\xb0i\xf3\xe1\x96C\r(08\x0f\xa3\t\xf7\x148c\xf3\xcf\x8b\xad\xfb\x08\xbb\x1c\x9e\x1c\x9b\\\xec\xf5\xe6\x10\x85\x86\xc5_z\xaf8\xec\x90\xdf3\x07\xda\xa2\xad7v\x96;\xe9\x14s\xf1X`\xae\xad\xb4\x90#\xdc\x0f\x82\x94\xa9N5\xb9Cn\xce\xfa\xb9bC\x80/\x86\xefPP\xd1!\xdd\xef\xad\xaf\xc1\xcc\x82*\xb7\xb2X\xe0\x01\xb24\xd2\x85\xf0\x90\xa4\xd8K\xa0)\x19\xd2\xc5\x81\x0c\xf2 \x1c&h\xda\x95\xeds\x08\x9cfiI\x1a\xcd\x0f\x99\xed;\x0b\xfaRMk\xa2\xd7\xbc\xf1b\x13\x9a\x18\xb6*s\x0bCI/\x19d\x9aj\x83\xc4\x11#\xf7\x10\xff\x00\x83&\x85\xe0\x87\xfe\x8b\xfe\xd999\xc8\x1b\x7fC\xde\xa8\xb6E\xaaQ\x8el\xcb\xcd\x87\x1b_\x9er\xf0A\xc1[\xbe\xc2 9B\xff\x86\xe4\xfez8#\xe4\xa7\\BQ\xf0\xf0\x06\xb4\x10\x8b\x92bb>\xa5\x04\xce\xa4\x96\xe6\x9bK\xa5A\xdaQ\x16j\xed\x9b\nB\x96M\xbf\xbbK{)\xa4\x97\x03\xc5p9\xf9\x8e\\J\xaa2h\x80\x0c\xee\xed\x85\xc6&\xf7\xe6\x11\x96\x7fW\x13\xebTUh\xb7\xf4[uD\xbf3\xbd\x8e\x8fI\x9c\xbf\xe16z\x15\xadE\xf3w\xf3\xb0\xbbT\xd4\x08\xf3k\x98\x0e#\xa7\xc7\x85\x8f \xfe\xdb_\xcb8\xa9\xd7dg\xd3\x87\x0c\xa3\xbeB\xfbp}\xf8Z\x90\xe7\x11\xd7N\xba\xf82:V\xad\xc7\x8b",?D9\x15\xa0!\xb2\xb3\xee\xcbs\x1c\xe1\xaf\x80a\x88LN\xa7,\x025\x8e\x8dz)\x18\xc0\x9e\xc26(A\xa2U\\#\x12\xec\x07\xa1\x98g\x1c\x89x\xb3\x9a\x93$\xe4"\x1d\x02-\x12@\x97tx\x89\x9a0\xff\xfc\x1b\x8a\xe5\x0e\xf9.\x8e\x96\tr\xe5\xa56\x82`)\xa4\x80\xa8\x12|\x83\xa3\xdeR\xb9\xc2y \xd8\xb8\xcf\xf6\x08S\x8d?=\x03\x06%\xd2\xea)P7\xc6U\x0b8\x9e\'\xe5"dp\xa6\x98\xb8\xe7\x9cj-\x9a\xc6\x8a\x85\x0c\xd1\xc5\x9bu8\x83;&\x8bj\xcc\xd3o\xa2\x08g\xca#JQ\x8c\x18T\x11\xe9\xa4\x01\xa8\xdf[]\xf016}|\xdb\x905\x88\xe1\x83\x0f\x9aMF"\x89\x87a\x08\xbdJ\x06G\xaba\x0cXl/\x92\x8e4pA\xcf\xc2\x92%*S\xcai@m\xed\x92\xe3,HD\\\xf5\xfd\xa7\x86\x1a\'T\xe3T\xc1\xb6\xfe\xbd4\xb0s\xa8\xf0\x99\xbc\x01\xba\x98\xa7\xa9\xb6\xc2X\x91\xe9\xf1\x1d\x1c\xc2\xd1\xd5\x9c\xa5\xc5]\x08\xfe\xc1\xebK\x1ap\xcc[\xc2\x91P\x13=\n,\'"R\x15\x95\xa4k\xeb\xd5\x00\xef\xd0\xa0?\xd4e\xe7\x9a\x9c \xca\xe5\xcf/\xf1\xde2z\xc5\x8b\'06\xe1\x05Z\xe7\x8bh\x82\x156\xad\x85\x96@J\xd4\xa7-\xb5\xc4\xb8\xff\x9e\x9eP\x00\x14%\xc9O\x1d3\xc9\xebw\xa4K\xe3\xb3\xdd!\x01h\xdb}\xea`u\\`\x1c\x16!\x06\xe6\xdbj\xa3W\x83\xe3\x0em\xbf\x1f\xaa\x9a\xa4\x9b\xc7r\xef\xb9&\xde\t7\xddU8Z\x91\xa2\xd6#\xc73R\xcd\xab\xe0\x9b Q&\x9d\x9fz\xf0\x9dT9\xc4{I?\x1f\xe2x\x99\xdb=z,\xb4WJ\x07\xef\xe4|\x00T\xfbx\xbbM\xf3\x95c\x96M\xbcU)L\xfb\xc1\xa5(\x195\xf1\xf4\x7f\xb3X\xc6\x02\x93]\x81[\x84Wtf\x9f\xc2x\xcb\xc3+\x85\xee\xea!\xf10\xc9W\xb7y\'I\xd0c\xdb\xec0\x01l\xe0TR\xa2\x07s\x0fz\x1eH\xbe\xa7\xa4\xfeMG\x91\xaf\x07A=(jg\\Ri\xc3K\x9f\xf8\xc2\x05\x83\xbd8\xa5Q\x06\x91F\xe7\xc8\x07M\xbe\xc7\x1d\x14\x13\xd53\r\x8e\'\xe6\x05\xcd[\x1aNS\xac\xa3A+\xd5/\x0f\x8a\xda\xc8/-\t\xe0\xe5u\xfa\xe4{\xb9v\xdd\xa7\xaa\x1f\x9f\xa8%\xe0hqP\xe1\xb8V\xb9S\xb2\x9e\xb0\xc8\x98f\x9a\x15-\x83\x19\x10b\xe0T[\\\x00\x93\xb3\x0b}\x8eh\xdba\xfaD\xbf\xcb\'\xd3\x18\xd4R)\xc7j\xd4s;\xcf8]+d\x0b/\xd6\xbf\xbe\xc07\xe6\xd1s\x12n\xbf\x12<]5\xbb\x80\xc1\\\xa3\x91%>\xfe\xfc\x93\x83\x10\x8d\'h\x0e\x9b\xbd\xa0\x1f\x04w\xa9\xf2b\xd3\xfb{\x82\xa1\xd1#\x05\xad\x1c\x18\x18W\x85\x0f\xdf\xc9\xe4\xd0)&{\x99\xb9WK\xcc\xda\xac\x7f\xce-\xc1\x0e&J\x99ZH\xe1\xec\x16\xde\xaf$\xe6\xaaW\xb5\r\xd2\x1a\xf9\x8e\x02\xf3mS3\xb3p\x81\xbb^\xd3\xaf\xe5+S\xbc\xa66\xf17\xf2\xd1d\xfd=\x8a\x858\xf2\x8a\xb1Ja\x04W\xa1\xf12\xd1\xdexi\x98\xcf\xd5j\x81\x16\xc5\xd4j\xaf\'=\x18[\x04\xa6\xa6E\xe8\x8b(\xd2\xf9\xe3U\xfa\x8b\xd3\x0e\xc6V\x13+\xe98\x95\x8e\xcf%`jhZ|#C~9D\xf7\x8fh\x9f\t\x95\x99\xdd\xb8|M\x0f\x16p\xce\xe1\x14\x16G&\x9dt\n\xff\xa4\x13\x82m\x07\x95\'139\x90"mT\xa8\xaa\xa5O\x1c\xdd\xc8d\x97\x9f\x19(\xa2\xaa\xdc\xf2\xd5<UO\x95\xf0\x8f\xff\xa2\xb3W\xc9$\xc8\xd7:I\x0f\xed\x1b9\xaa\x99h\xfb\xa4\x94:\n\xa6m\x88\x19\x02\xd2\xfd\x13b\xfe\xfa\xe8\xe4+>\xb7\x9b\xe3K\x9b\xcc\xea\x96\xaa\x0er\xb8\xeb\x1dL=y\x8a\x03\x839\xc0\xd9\xdd\x1d0\x9d\xf3\xed\xe7\x87\xea\x9f\xcd,\xaa\xc6\xf6\xedj\xef_\xb1B\xcf\x9eX{O\x85\xae\xd6\x88\x1b\xb2\xac\x9f0\x83\xaff*\xc7&*\x08WJ\x17\x14\xf8\x84_\xa6\x8fZzl\x83\xc3\x05-:\x99\xadV\t:n\x83\xb3\xda\r\x92G\xf9n*L,\x80\xa1\xe5ot\xf3c=\xbaH\xdf\xb6\xc9\xca\xe8\xd01jR6\xa0\xcfM\xce"\x01+\xec;|C\x11\xbe\x15\xa8\xdfH$\xcd_\xfe\xb5\x86lk\xae\x97T\xf3R\xaek\x93\x8d\xe7D\x1d\x93o\xf7\xb40\xb6p\xac\xca\xb0\x14\x1a\x97\xfby\xed\x99\x06Y\'\x16\x0f\x0c\xeb\x8cQ\x1a)?\x92\x9c\x19\xedH\xab[\xa8\\\xfd\xef\x160\xd2\xbe&\xfd\xc0\xc0\t[.\xd9\xbe\xc1\xbeV\xcc*\xe5v#s\x87t$\xe3\xff\xdbR\xa1"\xed\x9d\xefJ\xe2\'Iu\xef\\\xf8\xd9\x01\xa1Q\x8e\x0b:\xb2\xde\'\xc7\x05yQ\x04=\xb1zXX\x0e\xeb\xeaNP\xfc\xde\x93\x88\xbe\xfd\x13^\xc7\x86\x04\xf1\x07\xf8\xbc3\x8f\xc6\xb7\x10;\xc4\xb6\xf1\xb5\x0f\xad\xca\x12\xde\xad\xbd\x1f\xe8\x9dB\xfa\x90\x03#qx\xfd\x8aN\xecU[\xf2\x113n^\rj(\x15\ro\x8b\xf9\x9e\x1c\x12BsZ\x9d\x8e^aL\xe7_\xe9\n\xd1!&!#\xc3eu\x81\xa6\xa8\xfa\xf6\x8c4Q\xe6\x02\x88HA2J\x88\x17\xc5\t\x9dB\x0e\xa7\xa7{\xaf\xe9D\xc22\x04\xe6_\x8e\x1e\xf7\x8b\x8bX\x9db\xfa\'\x01\xc0Ct\x14\x7f\xcbi\xb1\xa1u\x97\x9f/oi}\xfd\x9e\x99>\xf9\x06B\xd6\xc5!c\x84\xcdO\xd6\x1bn\x92|{I\x14\xa1\xf1\xc7\x7f*e\xa8\x18a\xd4#\x9bF\xa5Jm\xa1\x92/$\xcbz\xbd)\xe6(\xb5\xbd&\x1a\xc1YL\xf9\xfe}U\xaaD\x07\x8fi-\xfa#\xccu_*\xb8G\xeb\x90\x9c\x94\x10\x0e\xfc@\xf1\xa5\x94C\x8a\x80\x87t\x1b\xe7\n\xca7\x8a\xf4\xd5\x17\x8aj<F\x165\x7f\x0b\x1eY\x08\xbeg\xcb\xd6\xf8\xd2\xbd\xec%\x97\xd6Fa\xaa\xe2}C+\x8c\t\xd2*S^\xe8`1\xb7\xf8\xa7\xee\xe9wb,\x7f>\x99\xa1\x85wq\xfd+\xa5%g\xce\xc9\x10\xa4MD\xd2\xb8!\x89\r\xe0\xd7\x06%\xaejy\x1a\x9az\x90"\xd7\x04CF\xedp4\x0e.b\xf3\xdf\xbb\xaa;F\xc6I!\xbc^\xd1HJ\xfe\x18K\x94\x12\xd57\x95\x95\x81\xcafd\xbc\xf9~rvp\xdc\x8e\x8d\xfd\x1f\x1b\xb6:\x0e)\x12\xda\x03foo\xda\x03bar\xda\x03sys\xda\nsubprocess\xda\x02osr(\x00\x00\x00r)\x00\x00\x00Z\tlibraries\xda\x0ccheck_output\xda\x07environ\xda\x03get\xda\nexecutabler\'\x00\x00\x00Z\x13installed_librariesZ\x07library\xda\ncheck_call\xda\x04exec\xda\x07compiler,\x00\x00\x00r,\x00\x00\x00r,\x00\x00\x00r-\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s2\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x01\x08\x01\x08\x04J\x02\x04\x01F\xff\x04\x01\x0e\xff\x04\x01\x0c\xff\x04\x02\x06\x01\x02\xff\x06\x03\x08\x01\x08\x01\x02\x01\x04\x01H\xff\x08\x02\x06\x01\x08\x02)\x0f\xda\x03foo\xda\x03bar\xda\x03sys\xda\x05bytes\xda\x06decode\xda\x04join\xda\x07version\xda\x05splitZ\x0ePYTHON_VERSION\xda\x05print\xda\x07replace\xda\x04exit\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r)\x00\x00\x00r)\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x12\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x03B\x01\x14\x01>\x01\x08\x02\x08\x01)\x0f\xda\x03foo\xda\x03bar\xda\x03sys\xda\x05bytes\xda\x06decode\xda\x04join\xda\x07version\xda\x05splitZ\x0ePYTHON_VERSION\xda\x05print\xda\x07replace\xda\x04exit\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r)\x00\x00\x00r)\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x12\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x03B\x01\x14\x01>\x01\x08\x02\x08\x01'))