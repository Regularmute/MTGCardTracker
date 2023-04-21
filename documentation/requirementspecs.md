# MTG Card Tracker

The application helps manage MTG cards and organize them into collections (e.g. "cubes") and decks. Users can update the amount of times a card has won or lost to help the owner of the cube to see how the cards and colors are performing. Cards in a collection also have a name and a color.

The application has following features:

Features for any user:
* A user can log in, log out and create an account. (Done)
* A user can browse collections, including decks and cards within the collections. (Done)
  * The user can search, filter and sort the displays by Name, Color or Win rate.
* A user can create a new empty collection of cards. (Done)

Features for the creator of a collection, referred to as its 'owner':
  * The owner can add cards to the collection. Each card is assigned a name, a color (including 'colorless'), victories and losses. (NOTE: Worth considering if more properties should be included from the start, in case adding new fields to the database may turn out difficult later.) (Partially Done)
  * The owner can adjust the properties of cards in their collection. (Partiall)
  * The owner can remove cards from their collection. (Done)
  * The owner can delete the collection. (Done)
  * The owner can invite other users to use the collection. (Done)

Features for users invited to use a collection (Including the owner):
* An invited user can create a deck from the cards in the collection. (Done)
* An invited user can update the amount of times cards in their deck have won or lost.(Done)
  * Possible implementation is to let the user select multiple cards in their deck with checkboxes and simultaenously increment their Victories or Losses by one. This will prevent cards that weren't drawn in a game from having their win rate affected.

I am planning to keep track of following databases with various values:
* Users
  * Username
  * Password hash
* Collections
  * Creator (Refers to Users.id)
  * Invited users (Refers to Users.id)
* Decks 
  * Collection (Refers to Collection.id)
  * Creator (Refers to Users.id)
* Cards
  * Collection (Refers to Collection.id, IMPORTANT to distinguish different instances of the same card in different collections. This makes it possible for the same card to have different amount of victories and losses in different collections.)
  * Name
  * Color(s)
  * Victories
  * Losses
  * Win rate, calculated with [Victories / (Victories+Losses)]
* Colors
  * Collection (Refers to Collection.id for similar reasons as in the Cards table. Enables displaying the performance of a color in each collection.)
  * Name (White, Blue, Black, Red, Green or Colorless)
  * Win rate, calculated with [Total Victories of all Cards in the same Collection with the listed Color divided by the sum of those cards' Victories and Losses]