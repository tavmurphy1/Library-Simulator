# Author: Tavner Murphy
# GitHub username: tavmurphy1
# Date: 10/14/23
# Description: Creates a complete library checkout/return system using classes, inheritance, and polymorphism
# complete with overdue item tracking/fine system, members, w/ 3 different types of media

class LibraryItem:
    """Represents a library item that can be a Book, Movie, or Album with a unique id and a title"""
    def __init__(self, library_item_id, title):
        """Creates a library item with a unique ID and title, includes values for
         location, current borrower, current requester, and date checked out"""
        self._library_item_id = library_item_id
        self._title = title # Cannot be assumed to be unique
        self._location = "ON_SHELF" # can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
        self._checked_out_by = None # Can only be checked out by one person at a time
        self._requested_by = None # Can only be requested by one Patron at a time
        self._date_checked_out = None

    def get_library_item_id(self):
        """Returns unique library item id"""
        return self._library_item_id

    def get_location(self):
        """Returns location of library item:
        on shelf, on hold, or on hold shelf"""
        return self._location

    def get_title(self):
        """Returns title of library item"""
        return self._title
    def get_checked_out_by(self):
        """Returns which patron checked out library item"""
        return self._checked_out_by
    def get_requested_by(self):
        """Returns which patron requested library item"""
        return self._requested_by
    def get_date_checked_out(self):
        """Returns date library item was checked out"""
        return self._date_checked_out

class Book(LibraryItem):
    """A type of library item that has an author, unique ID, and title"""
    def __init__(self, library_item_id, title, author):
        """Initializes Book object with unique ID, title, and author"""
        super().__init__(library_item_id, title)
        self._check_out_length = 21
        self._author = author

    def get_check_out_length(self):
        """Returns check out length of 21"""
        return self._check_out_length

    def get_author(self):
        """Returns book's author"""
        return self._author

class Album(LibraryItem):
    """A type of library item that has an artist, unique ID, and title"""
    def __init__(self, library_item_id, title, artist):
        """Initializes Album with unique ID, title, and artist"""
        super().__init__(library_item_id, title)
        self._check_out_length = 14
        self._artist = artist

    def get_check_out_length(self):
        """Returns check out length of 14"""
        return self._check_out_length

    def get_artist(self):
        """Returns album's artist"""
        return self._artist

class Movie(LibraryItem):
    """A type of library item that has a director, unique id, and title"""
    def __init__(self, library_item_id, title, director):
        """Initializes movie object with unique ID, title, and director"""
        super().__init__(library_item_id, title)
        self._check_out_length = 7
        self._director = director

    def get_check_out_length(self):
        """Returns check out length of 7"""
        return self._check_out_length

    def get_director(self):
        """Returns movie's director"""
        return self._director

class Patron:
    """A member of the library with a unique ID and name,
    has a list of checked out items and a current fine amount,
    as well as methods to amend fine and checked out items list"""
    def __init__(self, patron_id, name):
        """Initializes Patron with unique ID, name,
         empty list of checked out items, and total fines incurred to 0"""
        self._patron_id = patron_id
        self._name = name # Cannot be assumed to be unique
        self._checked_out_items = []
        self._fine_amount = 0 # Allowed to go negative

    def get_name(self):
        """Returns patron's name"""
        return self._name

    def get_patron_id(self):
        """Returns patron's unique ID"""
        return self._patron_id

    def get_checked_out_items(self):
        """Returns list of patron's currently checked out items"""
        return self._checked_out_items

    def get_fine_amount(self):
        """Returns total fines incurred by Patron"""
        return self._fine_amount

    def add_library_item(self, library_item):
        """Adds a library item to the Patron's list of checked out items"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes a library item from the Patron's list of checked out items"""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount): # Fine is allowed to go negative
        """Amends the Patron's total fine amount"""
        self._fine_amount += amount

class Library:
    """Represents a library object with lists of LibraryItem and Patron objects
     as well as a date counter and methods for checking out, returning, and requesting LibraryItems"""
    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, library_item):
        """Adds a book, album, or movie object to holdings list"""
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """Adds a patron object to members list"""
        self._members.append(patron)

    def get_holdings(self):
        """Returns list of holdings"""
        return self._holdings

    def get_members(self):
        """Returns list of members"""
        return self._members

    def get_current_date(self):
        """Returns current date"""
        return self._current_date

    def lookup_library_item_from_id(self, library_item_id):
        """Looks up book, album, or movie in holdings from unique ID
        or returns 'None' if item not in holdings"""
        # Returns the LibraryItem object corresponding to the ID parameter, or
        # None if no such LibraryItem is in the holdings
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """Looks up patron object from unique ID
        or returns 'None' if not in member list"""
        for member in self._members:
            if member.get_patron_id() == patron_id:
                return member
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Adds a library item to a patron's checked out items and
        updates that albums status and new location"""
        # if the specified Patron is not in the Library's members
        if self.lookup_patron_from_id(patron_id) == None:
            return "patron not found"
        # if the specified LibraryItem is not in the Library's holdings,
        elif self.lookup_library_item_from_id(library_item_id) == None:
            return "item not found"
        #if the specified LibraryItem is already checked out
        elif self.lookup_library_item_from_id(library_item_id).get_location() == "CHECKED_OUT":
            return "item already checked out"
        #if the specified LibraryItem is on hold by another Patron
        elif self.lookup_library_item_from_id(library_item_id).get_location() == "ON_HOLD_SHELF":
            return "item on hold by other patron"
        else:
            # Otherwise update the LibraryItem's checked_out_by, date_checked_out and location
            self.lookup_library_item_from_id(library_item_id)._checked_out_by = self.lookup_patron_from_id(patron_id)
            self.lookup_library_item_from_id(library_item_id)._date_checked_out = self._current_date
            self.lookup_library_item_from_id(library_item_id)._location = "CHECKED_OUT"

            # if the LibraryItem was on hold for this Patron, update requested_by
            if self.lookup_library_item_from_id(library_item_id).get_requested_by() == self.lookup_patron_from_id(patron_id):
                self.lookup_patron_from_id(patron_id)._requested_by = None

            # update the Patron's checked_out_items and return 'checkout successful'
            self.lookup_patron_from_id(patron_id).add_library_item(self.lookup_library_item_from_id(library_item_id))
            return "check out successful"

    def return_library_item(self, library_item_id):
        """Adds a Libary Item back to the the library's holdings
        and updates its location from patron to library's shelf or hold shelf"""
        # if the specified LibraryItem is not in the Library's holdings:
        if self.lookup_library_item_from_id(library_item_id) == None:
            return "item not found"
        # if the LibraryItem is not checked out:
        elif self.lookup_library_item_from_id(library_item_id).get_location() != "CHECKED_OUT":
            return "item already in library"
        else:
            # Update the Patron's checked out items (ie remove the library item)
            self.lookup_library_item_from_id(library_item_id).get_checked_out_by().get_checked_out_items().remove(self.lookup_library_item_from_id(library_item_id))

            # Update the LibraryItem's location depending on whether another Patron has requested it (if so, it should go on the hold shelf)
            if self.lookup_library_item_from_id(library_item_id).get_requested_by() != None:
                self.lookup_library_item_from_id(library_item_id)._location = "ON_HOLD_SHELF"
            else:
                self.lookup_library_item_from_id(library_item_id)._location = "ON_SHELF"

            #Update the library item's checked_out_by to none and return 'return successful'
            self.lookup_library_item_from_id(library_item_id)._checked_out_by = None
            return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """Updates a libary item's location to hold shelf if not requested by another patron"""
        # If the specified Patron is not in the Library's members, return "patron not found"
        if self.lookup_patron_from_id(patron_id) == None:
            return "patron not found"
        # If the specified LibraryItem is not in the Library's holdings, return "item not found"
        elif self.lookup_library_item_from_id(library_item_id) == None:
            return "item not found"
        # If the specified LibraryItem is already requested, return "item already on hold"
        elif self.lookup_library_item_from_id(library_item_id).get_requested_by() != None:
            return "item already on hold"
        else:
            # Update the item's requested by
            self.lookup_library_item_from_id(library_item_id)._requested_by = self.lookup_patron_from_id(patron_id)
            # If the item is on the shelf update its location to on hold
            if self.lookup_library_item_from_id(library_item_id).get_location() == "ON_SHELF":
                self.lookup_library_item_from_id(library_item_id)._location = "ON_HOLD_SHELF"
            return "request successful"

    def pay_fine(self, patron_id, amount):
        """Pay's off a patron's fine by some amount"""
        # If the specified Patron is not in the Library's members
        if self.lookup_patron_from_id(patron_id) == None:
                return "patron not found"
        else:
            # use amend_fine to update the Patron's fine and return 'payment successful'
            if amount >= 0:
                self.lookup_patron_from_id(patron_id).amend_fine(-abs(amount))
            else:
                return "ERROR: Cannot pay negative fine amount"
            return "payment successful"

    def increment_current_date(self):
        """Increments the current date and the fines incurred for all overdue items"""
        self._current_date += 1

        #increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (by calling amend_fine)
        for member in self._members: #for each patron
            for item in member.get_checked_out_items(): #for each item checked out
                # if (current date - date checked out) > item's check out length
                if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length():
                    # amend fine amount = .10 cents per day
                    member.amend_fine(0.10)
