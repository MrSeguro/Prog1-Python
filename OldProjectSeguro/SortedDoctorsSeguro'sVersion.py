class SortedDoctors:
    def __init__(self, name: str, category: int, last_birth_time: int, accumulated_minutes: int, accumulated_hours: int):
        self.name = name
        self.category = category
        self.last_birth_time = last_birth_time
        self.accumulated_minutes = accumulated_minutes
        self.accumulated_hours = accumulated_hours

    def update_time(self, assistance_duration):
        """
        
        """
        self.accumulated_minutes += assistance_duration
        if self.accumulated_minutes >= 240:
            self.accumulated_hours += 1
            self.accumulated_minutes -= 240

    def update_weekly_time(self, assistance_duration):
        """
        
        """
        self.accumulated_hours += assistance_duration // 60
        self.accumulated_minutes += assistance_duration % 60

        if self.accumulated_hours >= 40: 
            self.accumulated_hours = 40
            self.accumulated_minutes = 15  
            self.weekly_live = 'weekly leave'

    def __str__(self):
        """
        Return a string representation of the doctor.
        
        """
        return "{}, {}, {}, {}, {}".format(self.name, self.category, self.last_birth_time, self.accumulated_minutes, \
                                            self.accumulated_hours)

    def __lt__(self, otherDoctor):
        """
        
        """
        if self.category != otherDoctor.category:
            return self.category > otherDoctor.category
        if self.last_birth_time != otherDoctor.last_birth_time:
            return self.last_birth_time > otherDoctor.last_birth_time
        if self.accumulated_minutes != otherDoctor.accumulated_minutes:
            return self.accumulated_minutes < otherDoctor.accumulated_minutes
        if self.accumulated_hours != otherDoctor.accumulated_hours:
            return self.accumulated_hours < otherDoctor.accumulated_hours

    def sort_doctors(doctors):
        """
        sorts the doctors based on priority of each atribute

        Requires: doctors is a lst of ints and strs
        Ensures: An organized and well prioritized list of doctors
        """
        return sorted(doctors, key=lambda doctor: 
                                        (doctor.category, 
                                        doctor.last_birth_time, 
                                        -doctor.accumulated_minutes, 
                                        -doctor.accumulated_hours, doctor.name))

    # Getters and Setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_category(self):
        return self.category

    def set_weekly_live(self, weekly_live):
        self.weekly_live = weekly_live

    def get_last_birth_time(self):
        return self.last_birth_time

    def set_last_birth_time(self, last_birth_time):
        self.last_birth_time = last_birth_time

    def get_accumulated_minutes(self):
        return self.accumulated_minutes

    def set_accumulated_minutes(self, accumulated_minutes):
        self.accumulated_minutes = accumulated_minutes

    def get_accumulated_hours(self):
        return self.accumulated_hours

    def set_accumulated_hours(self, accumulated_hours):
        self.accumulated_hours = accumulated_hours





