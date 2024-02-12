const Game =({gameData})=>{
    console.log("props")
    console.log(gameData);
    return(
        <div className="">
            <h1>Genre: {gameData.genre}</h1>
            <p>Title: {gameData.title}</p>
            <h5>Platform: {gameData.platform}</h5>
            <button>Price: {gameData.price}</button>
            
        </div>


    );

}

export default Game;