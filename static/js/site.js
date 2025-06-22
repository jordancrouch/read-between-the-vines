document.addEventListener("DOMContentLoaded", () => {
  const bookCovers = document.querySelectorAll(".book-cover");

  const titleEffect = (e) => {
    const book = e.currentTarget;
    const rect = book.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    const mouseX = e.clientX;
    const mouseY = e.clientY;

    const deltaX = (mouseX - centerX) / rect.width;
    const deltaY = (mouseY - centerY) / rect.height;

    const tiltStrength = 20;

    gsap.to(book.querySelector("img"), {
      rotationX: -deltaY * tiltStrength,
      rotationY: deltaX * tiltStrength,
      ease: "power2.out",
      duration: 0.3,
    });
  };

  bookCovers.forEach((book) => {
    book.addEventListener("mousemove", titleEffect);

    book.addEventListener("mouseleave", () => {
      gsap.to(book.querySelector("img"), {
        rotationX: 0,
        rotationY: 0,
        ease: "power2.out",
        duration: 0.3,
      });
    });
  });
});
