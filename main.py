from db_setup import initialize_database
from authentication import initialize_users, authenticate_user
from access_control import query_data, update_data
from confidentiality import encrypt_data, decrypt_data
from integrity import generate_hash, verify_data_integrity

def main():
    # Initialize database and users
    initialize_database()
    initialize_users()

    print("Welcome to Secure Health System")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    # Authenticate user and get their group
    user_group = authenticate_user(username, password)

    if user_group:
        print("Authentication successful. User Group:", user_group)

        while True:
            print("\nMenu Options:")
            print("1. View Records")
            if user_group == 'H':  # Only Group H users can update records
                print("2. Update Records")
            print("3. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                # Query data based on user group
                data = query_data(user_group)
                if data:
                    print("\nRetrieved Records:")
                    for record in data:
                        print(record)
                    
                    # Generate and verify data hash for integrity
                    data_hash = generate_hash(str(data))
                    print("\nData Hash Generated:", data_hash)
                    if verify_data_integrity(str(data), data_hash):
                        print("Data integrity verified.")
                    else:
                        print("Data integrity check failed.")
                    
                    # Encrypt and decrypt sample sensitive data
                    encryption_key = "Sixteen byte key"  # 16-byte AES key
                    sensitive_data = f"Sample sensitive field: {data[0][3]}"  # Example field: age
                    nonce, ciphertext, tag = encrypt_data(sensitive_data, encryption_key)
                    print("\nEncrypted Data:", ciphertext)
                    decrypted_data = decrypt_data(nonce, ciphertext, tag, encryption_key)
                    print("Decrypted Data:", decrypted_data)
                else:
                    print("No records found.")

            elif choice == "2" and user_group == 'H':
                # Handle record updates for Group H users
                record_id = int(input("Enter Record ID to update: ").strip())
                column = input("Enter the column to update (e.g., health_history): ").strip()
                new_value = input(f"Enter new value for {column}: ").strip()
                updates = {column: new_value}
                success = update_data(user_group, record_id, updates)
                if success:
                    print("Record updated successfully.")
                else:
                    print("Failed to update the record. Please check the inputs.")
            
            elif choice == "3":
                print("Exiting Secure Health System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed. Exiting program.")

if __name__ == "__main__":
    main()
