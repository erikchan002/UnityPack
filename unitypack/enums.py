from enum import IntEnum


class CompressionType(IntEnum):
	NONE = 0
	LZMA = 1
	LZ4 = 2
	LZ4HC = 3
	LZHAM = 4


class NodeFlags(IntEnum):
	Default = 0
	Directory = 1
	Deleted = 2
	SerializedFile = 3


class RuntimePlatform(IntEnum):
	StandaloneOSXUniversal = 2
	StandaloneOSXIntel = 4
	StandaloneWindows = 5
	WebPlayer = 6
	WebPlayerStreamed = 7
	iOS = 9
	PS3 = 10
	XBOX360 = 11
	Android = 13
	StandaloneLinux = 17
	StandaloneWindows64 = 19
	WebGL = 20
	WSAPlayer = 21
	StandaloneLinux64 = 24
	StandaloneLinuxUniversal = 25
	WP8Player = 26
	StandaloneOSXIntel64 = 27
	BlackBerry = 28
	Tizen = 29
	PSP2 = 30
	PS4 = 31
	PSM = 32
	XboxOne = 33
	SamsungTV = 34
	N3DS = 35
	WiiU = 36
	tvOS = 37
	Switch = 38
