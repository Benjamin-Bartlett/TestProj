class Time:
    __hours = None
    __minutes = None
    __seconds = None
    # instance vars (private):
    def __init__(self, h, m, s):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def getHours(self):
        return self.__hours
    def getMinutes(self):
        return self.__minutes
    def getSeconds(self):
        return self.__seconds

    def toString(self):
        return str(self.__hours) + ":" + str(self.__minutes) + ":" + str(self.__seconds)

    def timeInSeconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    def changeTime(self, h, m, s):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def twelveHourClock(self):
        return str(self.__hours % 12 if self.__hours != 12 else 12) + ":" + str(self.__minutes) + ":" + str(self.__seconds) + " " + ("pm" if self.timeInSeconds() > 3600*12 else "am")

    def whatTimeIsIt(self):
        return "morning" if 6*3600 <= self.timeInSeconds() < 12*3600 else ("afternoon" if 12*3600 <= self.timeInSeconds() < 17*3600 else ("evening" if 17*3600 <= self.timeInSeconds() < 22*3600 else "nighttime"))

    def compareTo(self, t):
        return (abs(self.timeInSeconds() - t.timeInSeconds()) / (self.timeInSeconds() - t.timeInSeconds())) if self.timeInSeconds() != t.timeInSeconds() else 0

    def timeTill(self, t):
        return Time((t.timeInSeconds()-self.timeInSeconds()) // 3600, ((t.timeInSeconds()-self.timeInSeconds()) % 3600) // 60, (t.timeInSeconds()-self.timeInSeconds()) % 60)

