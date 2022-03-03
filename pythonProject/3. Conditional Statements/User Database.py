# Short program that shows if a user has been added to a database.

# Create variables that track if a user has been added to the database.
added_user = True
user = "Michael"

# if statement to verify the given user has been added.
if added_user == False:
    print(f"Adding {user} to database.")
    added_user = True
print(f"Database has added user: {user}")

# Same example but False.
added_user = False
user = "Michael"

if added_user == False:
    print(f"Adding {user} to database.")
    added_user = True
print(f"Database has added user: {user}")