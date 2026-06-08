#The Movie class models a single film and owns its seat data.
class Movie:
    def __init__(self, title, showtime, available_seats, booked_seats):
        self.title = title
        self.showtime = showtime
        self.available_seats = available_seats
        self.booked_seats = booked_seats

    def book_seat(self):
        if self.available_seats:
            print("Booking seat for  movie:", self.title , "at", self.showtime, "Which seat would you like to book? Available seats:", self.available_seats)
            booked_seat = input("Enter the seat number you want to book: ")
            if booked_seat in self.available_seats:
                self.booked_seats.append(booked_seat)
                self.available_seats.remove(booked_seat)
                return True
            else:
                print("Invalid seat selection.")
                return False
        else:
            return False

    def cancel_booking(self):
        if self.booked_seats:
            canceled_seat = self.booked_seats.pop()
            self.available_seats.append(canceled_seat)
            return True
        else:
            return False

    def get_available_seats(self):
        return self.available_seats

    def __str__(self):
        return f"{self.title} at {self.showtime} - Available Seats: {self.available_seats}"

# The BookingSystem class manages multiple movies and handles user interactions.
class BookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        for idx, movie in enumerate(self.movies):
            print(f"{idx + 1}. {movie}")

    def book_seat_for_movie(self, movie_index):
        if 0 <= movie_index < len(self.movies):
            if self.movies[movie_index].book_seat():
                print("Seat booked successfully!")
            else:
                print("Sorry, no seats available.")
        else:
            print("Invalid movie selection.")

    def cancel_booking_for_movie(self, movie_index):
        if 0 <= movie_index < len(self.movies):
            if self.movies[movie_index].cancel_booking():
                print("Booking cancelled successfully!")
            else:
                print("No bookings to cancel.")
        else:
            print("Invalid movie selection.")

#Menu-driven interface for the booking system.
def main():
    system = BookingSystem()
    system.add_movie(Movie("Leo", "7:00 PM", ["A1", "A2", "A3", "A4", "A5"],[]))
    system.add_movie(Movie("Jailer", "8:00 PM", ["B1", "B2", "B3", "B4", "B5"],[]))
    system.add_movie(Movie("Avengers", "9:00 PM", ["C1", "C2", "C3", "C4", "C5"],[]))

    while True:
        print("\nMovie Booking System")
        print("1. Display Movies")
        print("2. Book a Seat")
        print("3. Cancel a Booking")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.display_movies()
        elif choice == '2':
            movie_index = int(input("Enter movie number to book a seat: ")) - 1
            system.book_seat_for_movie(movie_index)
        elif choice == '3':
            movie_index = int(input("Enter movie number to cancel a booking: ")) - 1
            system.cancel_booking_for_movie(movie_index)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":    main()

 

