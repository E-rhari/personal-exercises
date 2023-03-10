const pokemonName = document.querySelector("#name");
const pokemonNumber = document.querySelector("#number");
const pokemonImage = document.querySelector("#pokemon_img");

const form = document.querySelector("#form");
const input = document.querySelector("#input");

buttonPrev = document.querySelector("#btn_prev");
buttonNext = document.querySelector("#btn_next");

let currentPokeNumber


const fetchPokemon = async (pokemon) => {
    const APIResponse = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);

    if (APIResponse.status === 200)
    {
        const data = await APIResponse.json();
        return data;
    }   
}


const renderPokemon = async (pokemon) => {

    pokemonName.innerHTML = "Loading";
    pokemonNumber.innerHTML = 0;
    
    const data = await fetchPokemon(pokemon);

    if(data)
    {
        pokemonName.innerHTML = data.name;
        pokemonNumber.innerHTML = data.id;
        currentPokeNumber = data.id;
        pokemonImage.src = data['sprites']['versions']['generation-v']
        ['black-white']['animated']['front_default'];
    }

    else
    {
        pokemonName.innerHTML = "Missing No.";
        pokemonNumber.innerHTML = 'E404';
        pokemonImage.src = "../images/Missingno.webp"
    }
    input.value = ""
}


form.addEventListener("submit", (event) => {
    event.preventDefault();

    renderPokemon(input.value.toLowerCase());
})


buttonNext.addEventListener("click", () =>{
    currentPokeNumber += 1;
    renderPokemon(currentPokeNumber)
})


buttonPrev.addEventListener("click", () =>{
    if (currentPokeNumber !== 1)
    {
        currentPokeNumber -= 1;
        renderPokemon(currentPokeNumber)
    }
})


renderPokemon(1)