class ServerMessageTypes(object):
	TEST = 0
	CREATETANK = 1
	DESPAWNTANK = 2
	FIRE = 3
	TOGGLEFORWARD = 4
	TOGGLEREVERSE = 5
	TOGGLELEFT = 6
	TOGGLERIGHT = 7
	TOGGLETURRETLEFT = 8
	TOGGLETURRETRIGHT = 9
	TURNTURRETTOHEADING = 10
	TURNTOHEADING = 11
	MOVEFORWARDDISTANCE = 12
	MOVEBACKWARSDISTANCE = 13
	STOPALL = 14
	STOPTURN = 15
	STOPMOVE = 16
	STOPTURRET = 17
	OBJECTUPDATE = 18
	HEALTHPICKUP = 19
	AMMOPICKUP = 20
	SNITCHPICKUP = 21
	DESTROYED = 22
	ENTEREDGOAL = 23
	KILL = 24
	SNITCHAPPEARED = 25
	GAMETIMEUPDATE = 26
	HITDETECTED = 27
	SUCCESSFULLHIT = 28

	strings = {
		TEST: "TEST",
		CREATETANK: "CREATETANK",
		DESPAWNTANK: "DESPAWNTANK",
		FIRE: "FIRE",
		TOGGLEFORWARD: "TOGGLEFORWARD",
		TOGGLEREVERSE: "TOGGLEREVERSE",
		TOGGLELEFT: "TOGGLELEFT",
		TOGGLERIGHT: "TOGGLERIGHT",
		TOGGLETURRETLEFT: "TOGGLETURRETLEFT",
		TOGGLETURRETRIGHT: "TOGGLETURRENTRIGHT",
		TURNTURRETTOHEADING: "TURNTURRETTOHEADING",
		TURNTOHEADING: "TURNTOHEADING",
		MOVEFORWARDDISTANCE: "MOVEFORWARDDISTANCE",
		MOVEBACKWARSDISTANCE: "MOVEBACKWARDSDISTANCE",
		STOPALL: "STOPALL",
		STOPTURN: "STOPTURN",
		STOPMOVE: "STOPMOVE",
		STOPTURRET: "STOPTURRET",
		OBJECTUPDATE: "OBJECTUPDATE",
		HEALTHPICKUP: "HEALTHPICKUP",
		AMMOPICKUP: "AMMOPICKUP",
		SNITCHPICKUP: "SNITCHPICKUP",
		DESTROYED: "DESTROYED",
		ENTEREDGOAL: "ENTEREDGOAL",
		KILL: "KILL",
		SNITCHAPPEARED: "SNITCHAPPEARED",
		GAMETIMEUPDATE: "GAMETIMEUPDATE",
		HITDETECTED: "HITDETECTED",
		SUCCESSFULLHIT: "SUCCESSFULLHIT"
	}

	def toString(self, id):
		if id in self.strings.keys():
			return self.strings[id]
		else:
			return "??UNKNOWN??"
