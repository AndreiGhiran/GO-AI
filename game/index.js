const deadstones = require('@sabaki/deadstones');
const influence = require('@sabaki/influence');
const http = require('http');
const fs = require('fs')
const Board = require('@sabaki/go-board')


fs.readFile("D:\\FSWD\\L7\\da.txt", 'utf8', async (err,data)=>{
	data = JSON.parse(data);
	
	let board = new Board(data)
	
	//console.log(getEmpty(board))
	console.log(bestMove(board,-1,0))
	// let resp = bestMove(board,1,0,-Infinity,Infinity)
	// resp.then(number =>{
	// 	return number
	// })
	// console.log(await resp.then(resp=>{return resp}))
});

var globalPass = 0

function getEmpty(board){
	let emptyPositions = []
	let x = 0
	let y = 0
	board.signMap.forEach(line =>{
		line.forEach(point =>{
			if(point == 0)
			{
				emptyPositions.push([x,y])
			}
			y = (y + 1)%9
		});
		x = (x + 1)%9
	});

	return emptyPositions
}

function isFinished(board){
	if(getEmpty(board).length == 0)
	{
		return true;
	}
	if(globalPass >= 2)
	{
		return true;
	}

	return false;
}


function score(board,player){
	let score = 0;
	let table = board.signMap

	// let dead = deadstones.guess(table);
	
	// (await dead).forEach(deadStone =>{
	// 	table[deadStone[0]][deadStone[1]] = 0;
	// });

	board = new Board(table)

	let influenceMap = influence.map(board.signMap)
	// console.log(influenceMap)
	// console.log("\n\n")
	influenceMap.forEach(line =>{
		line.forEach(point =>{
			if((point < 0 &&  player < 0 ) || (point > 0 &&  player > 0 ) )
			{
				score = score + 1;
			}
		});
	});
	return score	

}

function bestMove(board,player,depth) {
	if(player == 1)
	{
		best = [-1,-1,-Infinity]
	}
	else
	{
		best = [-1,-1,Infinity]
	}
	
	
	let empty = getEmpty(board);

	if(globalPass == 2 || isFinished(board) == true)
	{
		return [-1,-1,score(board,player)]
	}
	empty.forEach(position =>{
		
		let x = position[0];
		let y = position[1];

		let boardClone = board.clone(); 
		
		board = board.makeMove(player,[x,y]);

		let scor = bestMove(board,-player,depth+1)
		board = boardClone;

		scor[0]=x
		scor[1]=y
		if(player == 1)
		{
			if(best[2]<scor[2])
			{
				best = scor
			}
		}
		else
		{
			if(best[2]>scor[2])
			{
				best = scor
			}
		}


	});
	
	return best;

}