# MTG Card Tracker

<h2>Visit the app here: (https://card-tracker-morning-butterfly-2890.fly.dev) </h2>

The application helps manage trading cards and organize them into collections (e.g. "cubes") and decks. Users can update the amount of times a card has won or lost to help the owner of the cube to see how the cards are performing.

<h2>Current features</h2>
The application currently has the following features:

  * The user can log in, log out and create an account.
  * The user can create a new empty collection of cards.
  * The owner of a collection can invite other users to the collection.
    * The owner can uninvite users from their collection.
  * The user can delete their collections.
  * The user can add cards to their collection.
    * Each card has a name, amount of wins, losses and a win rate percentage.
    * Wins and losses can be incremented and decremented.
  * The user can delete cards from their collection.
  * The owner or an invited user can add decks to their collection.
  * The creator of a deck or the owner of the collection can add and remove cards to the deck.
  * Decks can be deleted.
  * A user can browse their collections and cards within the collections.

<h2>Test ideas</h2>
Some ways to test the current features:

<h3>Navigation</h3>

  * The navigation bar and its links work correctly.
  * The navigation bar's links depend on whether or not the user is logged in.

<h3>Registration</h3>

  * The front page has a link to the registration page.
    * Registering an account requires an username consisting of 1-60 english letters or numbers and a password of at least 6 characters
    * After registering an account, the page should redirect back to the front page with the login form

<h3>Logging in and out</h3>

  * The front page should display the logged user's username, or the registration link for an unlogged user.
  * The login form should work correctly and redirect the user to the front page after a successful operation.
  * A logged user should be able to log out by clicking the link on the front page.
    * After a successful logout operation the user should be redirected to the front page.

<h3>Errors</h3>

  * Error page should have a link to the front page and display an explanation of what caused the error.

  * No unrecognized errors (i.e. Internal Server Error 500) are thrown
  * Errors are thrown for:
    * Registering with an existing username
    * Registering with an invalid username
      * Username can only contain letters a-z and numbers 0-9
      * Username can have between 1 and 60 characters
    * Passwords don't match when registering
    * Logging in with incorrect credentials
    * Adding a collection without a name or a name with over 60 characters
    * Viewing a collection as an uninvited user directly through the url
    * Inviting a user without entering a name
    * Inviting a nonexistent user
    * Inviting an already invited user
    * Uninviting an empty choice
    * Adding a card without a name
    * Adding a card with a name longer than 150 characters
    * Adding a deck without a name
    * Adding a deck with a name longer than 150 characters
    * Adding a nonexistent card to a nonexistent deck
    * Removing a nonexistent card from the deck

<h3>Collections</h3>

  * The collection page should be accessible from the front page if and only if the user is logged in.
  * Writing a name to the collection form and submitting should correctly create a new collection.
    * The collection must have a name
  * The collection page should display all of the user's collections.
    * The collections should display a button to delete them, and deletion should remove the collection and the cards inside without affecting the other collections or their contents.
  * The user can click a collection's name to access their unique page.
  * Deleting a collection asks for confirmation before performing the operation.
  * Users can be invited and uninvited only by the collection's owner
  * Invited users' rights work correctly - they can:
    * View collections they've been invited to
    * Create decks in that collection
    * Add, remove and update the winrate of cards to their decks from the collection
    * See other users' decks
    * Cannot manipulate other users' decks
  * Inviting users works correctly (the username field is case sensitive!)
  * Uninviting users works correctly
  * Uninviting users requires confirmation
  * The user can alternate between viewing cards and viewing decks

<h3>Cards</h3>

  * A collection's page should display the form to add a card and a list of cards added to it.
    * For a new collection, no cards should be visible.
  * A card is added by typing its name into the form and submitting it.
    * Trying to submit an empty form should return an error page.
  * Each card should display their name, wins, losses and a win-rate percentage (rounded to two decimal places). The win-rate is 0% when the cards have no wins or losses marked.
    * Currently there is a bug where wins and losses can go down into the negatives.
  * Each card should display the following buttons (no button should affect the other cards in the collection):
    * delete card: should remove the card from the collection.
    * add win: should increment the card's wins and update its win rate.
    * add loss: should increment the card's losses and update its win rate.
    * remove win: should decrement the card's wins and update its win rate.
    * remove loss: should decrement the card's losses and update its win rate.
  * Deleting a card asks for confirmation before performing the operation.

<h3>Decks</h3>

  * Empty decks can be created
  * Cards from the collection can be added to a deck
    * Multiple copies of a card can be added to a deck
  * Win and loss adjustments made to cards in a deck carry over to the collection
  * Individual cards can be deleted without affecting duplicate copies of it in the deck.
  * Deleting a deck asks for confirmation before performing the operation.


<h2>Planned features</h2>
Possible ideas to expand the application:

  * Inviting the user requires a confirmation by the client to avoid misclicks.
  * The user can search for a card in a collection or deck by name or other property.
  * The user can sort cards by name, wins, losses, winrate and time added.
  * The user can add multiple cards at once.
  * The user can update multiple cards' wins or losses at once.
  * The user can edit cards' names.
  * More properties for the cards, such as mana cost, color or other attributes.
  * Admin role functionality with more rights than a regular user (ability to see all users).

<h2>Thank you very much for taking the time to inspect my application!</h2>
