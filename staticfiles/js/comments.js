document.addEventListener("DOMContentLoaded", () => {
  // Set up variables
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("comment-form");
  const submitButton = document.getElementById("submit-button");

  const deleteModal = new bootstrap.Modal(
    document.getElementById("deleteModal"),
  );
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteForm = document.getElementById("deleteForm");

  // Iterate over edit buttons to attach event listener and add edit functionality
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let commentContent = document
        .getElementById(`comment-${commentId}`)
        .querySelector("#comment-text");
      commentText.value = commentContent.innerText;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }

  // Iterate over delete buttons to attach event listener and add delete functionality
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteForm.setAttribute("action", `delete_comment/${commentId}`);
      deleteModal.show();
    });
  }
});
