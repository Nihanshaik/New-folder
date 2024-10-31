import java.util.*;

class Account {
    private int accountNumber;
    private double balance;

    public Account(int accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0.0;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + amount);
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else {
            System.out.println("Invalid withdrawal amount or insufficient funds.");
        }
    }
}

public class BankingSystem {
    private HashMap<Integer, Account> accounts;
    private static int accountCounter = 1001;

    public BankingSystem() {
        accounts = new HashMap<>();
    }

    public Account openAccount() {
        int accountNumber = accountCounter++;
        Account newAccount = new Account(accountNumber);
        accounts.put(accountNumber, newAccount);
        System.out.println("New account opened. Account Number: " + accountNumber);
        return newAccount;
    }

    public Account getAccount(int accountNumber) {
        return accounts.get(accountNumber);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankingSystem bank = new BankingSystem();

        while (true) {
            System.out.println("\nBanking System");
            System.out.println("1. Open Account");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. View Balance");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 : bank.openAccount();
                case 2 : {
                    System.out.print("Enter account number: ");
                    int accountNumber = scanner.nextInt();
                    Account account = bank.getAccount(accountNumber);
                    if (account != null) {
                        System.out.print("Enter deposit amount: ");
                        double amount = scanner.nextDouble();
                        account.deposit(amount);
                    } else {
                        System.out.println("Account not found.");
                    }
                }
                case 3 :{
                    System.out.print("Enter account number: ");
                    int accountNumber = scanner.nextInt();
                    Account account = bank.getAccount(accountNumber);
                    if (account != null) {
                        System.out.print("Enter withdrawal amount: ");
                        double amount = scanner.nextDouble();
                        account.withdraw(amount);
                    } else {
                        System.out.println("Account not found.");
                    }
                }
                case 4 : {
                    System.out.print("Enter account number: ");
                    int accountNumber = scanner.nextInt();
                    Account account = bank.getAccount(accountNumber);
                    if (account != null) {
                        System.out.println("Balance: $" + account.getBalance());
                    } else {
                        System.out.println("Account not found.");
                    }
                }
                case 5 :{
                    System.out.println("Exiting Banking System.");
                    scanner.close();
                    return;
                }
                default : System.out.println("Invalid option. Try again.");
            }
        }
    }
}
