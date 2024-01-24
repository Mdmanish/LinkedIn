function openComment(id) {
    const css= document.querySelector(".comment-section"+id);
    css.classList.remove("comment-section_1")

    const css2= document.querySelector(".all-comments"+id);
    console.log(css2)
    css2.classList.remove("all-comments_1")
}

function closeComment(id) {
    const css= document.querySelector(".comment-section"+id);
    css.classList.add("comment-section_1")
    console.log(css)

    const css2= document.querySelector(".all-comments"+id);
    css2.classList.add("all-comments_1")
}
