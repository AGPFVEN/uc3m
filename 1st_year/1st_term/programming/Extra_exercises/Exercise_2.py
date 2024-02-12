class Dates_exercise():
    def init(self, format):
        #Initializing dictionary with months and days for each one
        self.months = {
            "January": 31,
            "February": 28,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August": 31,
            "September": 30,
            "October": 31,
            "November": 30,
            "December": 31}

        self.formats = ["dd/mm/yyyy", "mm/dd/yyyy", "yyyy/mm/dd", "text"]
        self.chosen_format = self.formats[format - 1]