
import java.util.*;
class Room {
    int roomNumber;
    String type;
    double price;
    boolean isBooked;
    String bookedBy;

    public Room(int roomNumber, String type, double price) {
        this.roomNumber = roomNumber;
        this.type = type;
        this.price = price;
        this.isBooked = false;
        this.bookedBy = null;
    }
}

public class HotelBookingSystem {
    private ArrayList<Room> rooms;

    public HotelBookingSystem() {
        rooms = new ArrayList<>();
        rooms.add(new Room(101, "Single", 50.0));
        rooms.add(new Room(102, "Single", 50.0));
        rooms.add(new Room(201, "Double", 75.0));
        rooms.add(new Room(202, "Double", 75.0));
        rooms.add(new Room(301, "Suite", 150.0));
        rooms.add(new Room(302, "Suite", 150.0));
    }

    public void viewAvailableRooms() {
        System.out.println("\nAvailable Rooms:");
        boolean foundAvailable = false;
        for (Room room : rooms) {
            if (!room.isBooked) {
                System.out.println("Room " + room.roomNumber + " (" + room.type + ") - $" + room.price + " per night");
                foundAvailable = true;
            }
        }
        if (!foundAvailable) {
            System.out.println("No rooms are available at the moment.");
        }
    }

    public void bookRoom(int roomNumber, String customerName) {
        Room room = getRoomByNumber(roomNumber);
        if (room != null && !room.isBooked) {
            room.isBooked = true;
            room.bookedBy = customerName;
            System.out.println("Room " + roomNumber + " has been successfully booked by " + customerName + " for $" + room.price + " per night.");
        } else {
            System.out.println("Room " + roomNumber + " is either unavailable or already booked.");
        }
    }

    public void checkoutRoom(int roomNumber) {
        Room room = getRoomByNumber(roomNumber);
        if (room != null && room.isBooked) {
            System.out.println("Room " + roomNumber + " checked out by " + room.bookedBy + ". Total charges: $" + room.price);
            room.isBooked = false;
            room.bookedBy = null;
        } else {
            System.out.println("Room " + roomNumber + " is not currently booked.");
        }
    }

    private Room getRoomByNumber(int roomNumber) {
        for (Room room : rooms) {
            if (room.roomNumber == roomNumber) {
                return room;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HotelBookingSystem hotel = new HotelBookingSystem();

        System.out.println("Welcome to the Interactive Hotel Booking System!");
        while (true) {
            System.out.println("\nPlease choose an option:");
            System.out.println("1. View Available Rooms");
            System.out.println("2. Book a Room");
            System.out.println("3. Checkout from Room");
            System.out.println("4. Exit");
            System.out.print("Your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    hotel.viewAvailableRooms();
                    break;
                case 2:
                    System.out.print("Enter your name: ");
                    String customerName = scanner.nextLine();
                    System.out.print("Enter room number to book: ");
                    int roomNumberToBook = scanner.nextInt();
                    hotel.bookRoom(roomNumberToBook, customerName);
                    break;
                case 3:
                    System.out.print("Enter room number to checkout: ");
                    int roomNumberToCheckout = scanner.nextInt();
                    hotel.checkoutRoom(roomNumberToCheckout);
                    break;
                case 4:
                    System.out.println("Thank you for using the Hotel Booking System. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        }
    }
}
