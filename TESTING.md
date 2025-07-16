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
   i. When landing on the homepage of the site, users are immediately met with a
   large video hero banner that contains books in.
   ii. Also when landing on the homepage, the hero banner contains large heading
   one text that hints at reading-based content, and is supported with additional
   text for more context, along with two prominent buttons acting as calls-to-action.
   iii. When landing on any other page, the header at the top of the page contains
   the logo, navigation menu text, and button text that help to provide context
   to the user that this is a book club site.
2. As a first-time visitor, I want to be able to see what is currently being
   read by the book club.
   i. The homepage hero contains a button link to 'view all books', where the
   books that are currently being read are displayed as the first books shown
   beneath the hero.
   ii. The section under the homepage banner displays books that are currently
   being read, so that they are easy to find and visible high up the page.
   iii. A link to the 'books' page is also present in the navigation menu,
   so that the books that are currently being ready can be accessed from any
   page.
3. As a first-time visitor, I want to be able to create an account and sign
   up to the site/club.
   i. The homepage hero contains a button link as a call-to-action for non-logged
   in users to 'sign up now'.
   ii. The navigation menu also contains a link to 'register' that can be accessed
   from anywhere on the site.
   iii. The foote call-to-action also conditionally displays a button link to
   'sign up now' for users that are not logged in.
4. As a first-time visitor, I want to be able to view the reading progress
   of the books.
   i. The reading progress of the books that are currently being read are displayed
   where they are listed throughout the website (on the homepage and books page).
   ii. The reading progress can also be seen on all book detail pages.

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
