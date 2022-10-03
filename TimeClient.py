from Lab5 import Time

class TimeClient:
    def main(self):
        t1 = Time(12, 30, 15)
        t2 = Time(0, 1, 15)
        t3 = Time(20, 0, 0)
        t4 = Time(6, 0, 0)
        t5 = Time(2, 1, 15)

        print(t1.toString())
        print(t2.timeInSeconds())
        t2.changeTime(1, 1, 15)
        print(t2.toString())
        print(t1.twelveHourClock())
        print(t2.twelveHourClock())
        print(t3.twelveHourClock())

        print(t1.whatTimeIsIt())
        print(t2.whatTimeIsIt())
        print(t3.whatTimeIsIt())
        print(t4.whatTimeIsIt())

        print(t2.compareTo(t1))
        print(t2.compareTo(t2))


        print(t2.timeTill(t5).toString())
        print(t4.timeTill(t1).toString())


timeClientObj = TimeClient()
timeClientObj.main()


