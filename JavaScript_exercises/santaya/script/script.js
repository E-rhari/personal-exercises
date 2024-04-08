const spinner    = document.querySelector("#spinner");
const img        = document.querySelector("#image");
const spinometer = document.querySelector("#spin-o-meter")

const fileInput = document.getElementById("input");

let spinSpeed     = 0;
let imageRotation = 0;


spinner.addEventListener("click", () => {
    spinSpeed+=1/2;
    let spinsPerSecond = spinSpeed*60;
    spinometer.innerHTML = `${spinsPerSecond} graus por segundo!!!`
});

setInterval(() => {
    imageRotation += spinSpeed;
    img.style.transform = `rotate(${imageRotation}deg)`;
}, 1)


fileInput.addEventListener("change", () => {console.log(fileInput)
    let file = fileInput.files[0];
    // img.classList.add("obj");
    img.file = file;

    const reader = new FileReader();
    reader.onload = (e) => {
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
});