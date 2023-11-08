myQuotes = [
    'A volte sono le persone che nessuno immagina che possano fare 
    certe cose quelle che fanno cose che nessuno può immaginare.',
    'La fantasia è più importante del sapere, perché il sapere è limitato.',
    'Chi dice che è impossibile non dovrebbe disturbare chi ce la sta facendo.',
    'C\'è una forza motrice più forte del vapore, 
      dell’elettricità e dell’energia atomica: la volontà.',
    'La misura dell\'intelligenza è data dalla capacità di cambiare 
        quando è necessario.',
    'La logica ti porta da A a B, l’immaginazione ti porta ovunque.',
    'Gli occhi sono lo specchio dell’anima… cela i tuoi se non vuoi che 
       ne scopra i segreti.',
    'Imparerai a tue spese che nel lungo tragitto della vita incontrerai 
        tante maschere e pochi volti.',
    'Ma guardi signora è facilissimo, le insegno io ad esser pazza. 
     Basta gridare la verità in faccia a tutti, loro non ci crederanno 
       e ti prenderanno per pazza.'
];

const buttonQuote = document.getElementById('new-quote');

buttonQuote.addEventListener('click',generate);

function generate(){
    randomQuote = randomNumber(myQuotes);

    const quote =  document.getElementById('quote');
    quote.innerHTML = myQuotes[randomQuote];
}

function randomNumber(array) {
    const num = Math.round(Math.random() * (array.length - 1));
    return num;
}