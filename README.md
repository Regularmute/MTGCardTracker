# MTG Card Tracker

<h2>Link to the application: <a href="https://card-tracker.fly.dev/"> Card Tracker </a> </h2>

The application helps manage trading cards and organize them into collections (e.g. "cubes") and decks. Users can update the amount of times a card has won or lost to help the owner of the cube to see how the cards are performing.

<h2>Current features</h2>
The application currently has the following features:

  * The user can log in, log out and create an account.
  * The user can create a new empty collection of cards.
  * The user can delete their collections.
  * The user can add cards to their collection.
    * Each card has a name, amount of wins, losses and a win rate percentage.
    * Wins and losses can be incremented and decremented.
  * The user can delete cards from their collection.
  * A user can browse their collections and cards within the collections.

<h2>Test ideas</h2>
Some bugs may occur when testing, they are usually solved either by refreshing the page or by returning to an earlier page and trying the operation again. These will be fixed in the future.

Some ways to test the current features:

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

<h3>Collections</h3>

  * The collection page should be accessible from the front page if and only if the user is logged in.
  * Writing a name to the collection form and submitting should correctly create a new collection.
    * The collection must have a name
  * The collection page should display all of the user's collections.
    * The collections should display a button to delete them, and deletion should remove the collection and the cards inside without affecting the other collections or their contents.
  * The user can click a collection's name to access their unique page

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


<h2>Planned features</h2>
Possible ideas to expand the application:

  * The creator of a collection can add other users as "players" to view the collection.
  * The user can view any collections they've been invited to as players.
  * The user can search for a card in a collection or deck by name or other property.
  * The user can create a deck from the cards in a collection they have access to
  * The user can sort cards by name, wins, losses, winrate and time added.
  * The user can add multiple cards at once.
  * The user can update multiple cards' wins or losses at once.
  * The user can edit cards' names.
  * More properties for the cards, such as mana cost, color or other attributes.
  * Admin role functionality with more rights than a regular user (ability to see all users).

<h2>Thank you very much for taking the time to inspect my application!</h2>
