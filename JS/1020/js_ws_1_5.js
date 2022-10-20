const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]
// participantsNums 에서 배열 하나씩 
for (participants of participantNums){
  for (participant of participants){
    const pair = participants.filter(piece => piece ===participant)
    //console.log(pair);
    if (pair.length === 1){
      console.log(participant);
    }
  }
    
}



// 3
// 100
// 62