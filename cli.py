def cli_homepage():
    print("Please Select an Option:\n")
    print("\t1. Generate threat_feed.csv Only")
    print("\t2. Generate CSV With Report")
    print("\t3. Generate Report Only")
    print("\t4. Exit\n")
    user_input = input(">> ").strip()

    if user_input == "1":
        generate_csv()
        print("Threat Feed CSV Generation Complete")
    elif user_input == "2":
        generate_csv()
        generate_report()
        print("Report and CSV Generation Complete")
    elif user_input == "3":
        generate_report()
        print("Report Generation Complete")
    elif user_input == "4":
        print("Exiting...")
    else:
        print("Invalid Input")
        cli_homepage()

if __name__ == '__main__':
    cli_homepage()