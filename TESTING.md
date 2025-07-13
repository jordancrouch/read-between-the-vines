# Read Between the Vines - Testing Documentation

The main README documentation can be found under [README.md](https://github.com/jordancrouch/read-between-the-vines/blob/main/README.md)

[View the website on Heroku](https://read-between-the-vines-24a3e4f3dbe6.herokuapp.com/).

## Table of Contents

1. [User Story Testing](#user-story-testing)
2. [Feature Testing](#feature-testing)
3. [Cross-browser Testing](#cross-browser-testing)
4. [Automated Testing](#automated-testing)
5. [Significant Bugs](#significant-bugs)

### User Story Testing

#### First-time Visitor Goals

1. As a first-time visitor, I want to be able to easily determine and understand
   the main purpose of the website.
   i.
   ii.
   iii.
2. As a first-time visitor, I want to be able to see what is currently being
   read by the book club.
   i.
   ii.
   iii.
3. As a first-time visitor, I want to be able to create an account and sign
   up to the site/club.
   i.
   ii.
   iii.
4. As a first-time visitor, I want to be able to view the reading progress
   of the books.
   i.
   ii.
   iii.

#### Returning Visitor Goals

1. As a returning visitor, I want to be able to see what books are on the reading
   list, so I have an idea of the next books to read.
   i.
   ii.
   iii.
2. As a returning visitor, I want to be able to view all books that have been finished.
   i.
   ii.
   iii.
3. As a returning visitor, I want to be able to log back in to the site.
   i.
   ii.
   iii.
4. As a returning visitor, I want to be able to add/update my reading progress to
   compare it to the average of the club.
   i.
   ii.
   iii.

#### Frequent User Goals

1. As a frequent user, I want to be able to comment on books to join the conversation.
   i.
   ii.
   iii.
2. As a frequent user, I also want to be able to edit any comments I have made.
   i.
   ii.
   iii.
3. As a frequent user, I want to create/read/add/update my reading progress,
   so I can keep track and compare it to the rest of the club.
   i.
   ii.
   iii.
4. As a frequent user, I want to be able to be able to submit a contact form,
   in order to leave feadback or future book suggestions for the club.
   i.
   ii.
   iii.

### Feature Testing

The following feature testing was conducted manually, as outlined below:

#### Book Club Features

<!-- TODO: add manual testing for the features below -->

- Book Listing
  - Books are categorised into: Currently Reading, To Be Read, and Finished Reading
  - The average reading progress is displayed per book
- Book Detail View
  - Club-wide and user-specific reading progress shown
  - Share buttons
  - Comments section
    - Approval system
    - Comment editing and deletion by comment author
  - Conditional sidebar for:
    - Logged-out users (sign up encouragement)
    - Logged-in users (contact call-to-action)
- Reading Progress Tracking
  - Logged-in users can update their progress per-book
  - Only one progress record per user, per book
  - Progress automatically moves a book into "Finished Reading" if average hits 90%

##### Comment System

<!-- TODO: add manual testing for the features below -->

- Logged-in users can submit, edit, or delete their comments
- Comments await admin approval before being shown publicly
- User-specific moderation (faded styling whilst pending)

##### Navigation & UX Enhancements

<!-- TODO: add manual testing for the features below -->

- GSAP hover tilt effects on book covers
- Accessible modals for confirming actions
- Footer CTA with conditional behaviour:
  - Signup prompt for guests
  - Contact prompt for logged-in users
- Custom 404 page handling

### Cross-browser Testing

Cross-browser testing was conducted manually on the browsers and operating systems
outlined below, ensuring that the site works well responsively and that
there are no isseus with any of the intended functionality of the site.

#### Windows 11

- Firefox
- Chrome
- Edge

#### Android

- Firefox
- Chrome
- Edge

#### macOS

- Safari
- Firefox
- Chrome

#### iOS

- Safari
- Firefox
- Chrome

### Automated Testing

#### Integration Tests

### Significant Bugs
