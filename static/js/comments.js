document.addEventListener("DOMContentLoaded", () => {
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("comment-form");
  const submitButton = document.getElementById("submit-button");

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
});
