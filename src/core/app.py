def start():
    while True:
        print("\n==== Python API Playground ====")
        print("1. REST API (Weather)")
        print("2. GraphQL API")
        print("3. WebSocket API")
        print("4. SOAP API")
        print("5. gRPC API")
        print("6. MQTT API")
        print("0. Exit")
        print("-------------------------------")

        choice = input("Choose an option: ")

        if choice == "1":
            from src.rest_api import rest_api_client
            rest_api_client.run()

        elif choice == "2":
            print("GraphQL module not yet implemented.")

        elif choice == "3":
            print("WebSocket module not yet implemented.")

        elif choice == "4":
            print("SOAP module not yet implemented.")

        elif choice == "5":
            print("gRPC module not yet implemented.")

        elif choice == "6":
            print("MQTT module not yet implemented.")

        elif choice == "0":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")