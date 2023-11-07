const sections = $("section");
sections.hide();

function displayCorrecSection(){
    console.log(window.location.hash)
    let currentSection = window.location.hash.slice(1);
    if (!currentSection || currentSection==="section1") $(sections[0]).show()
}