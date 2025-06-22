document.addEventListener("DOMContentLoaded", () => {
  // Set up variables
  const deleteButtons = document.getElementsByClassName("btn-delete-progress");
  const deleteForm = document.getElementById("deleteProgressForm");

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      const progressId = e.target.getAttribute("data-progress-id");
      const bookSlug = e.target.getAttribute("data-book-slug");

      deleteForm.action = `delete_progress/${progressId}`;

      const deleteModal = new bootstrap.Modal(
        document.getElementById("deleteProgressModal"),
      );
    });
  }
});
