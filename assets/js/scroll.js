if (
  "IntersectionObserver" in window &&
  "IntersectionObserverEntry" in window &&
  "intersectionRatio" in window.IntersectionObserverEntry.prototype
) {
  let observer = new IntersectionObserver(entries => {
    console.log(entries[0].boundingClientRect.y)
    if (entries[0].boundingClientRect.y < 0) {
      document.body.classList.add("nav-not-visible");
    } else {
      document.body.classList.remove("nav-not-visible");
    }
  });
  observer.observe(document.querySelector("#hack-pixel-top"));
}
