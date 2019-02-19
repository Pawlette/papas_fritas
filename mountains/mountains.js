function fire(mountains) {
    const reducerHighest = (accumulator, currentValue) => currentValue > accumulator ? currentValue : accumulator

    console.log('fire to: ', mountains.reduce(reducerHighest)) // The index of the mountain to fire on.
}

function fireMountain() {
    let mountains = [3,4,7,1,6,2,0]
    /*for (let i = 0; i < 8; i++) {
        const mountainH = parseInt(readline()) // represents the height of one mountain.
        mountains.push(mountainH)
    }*/
    console.log('Mountains: ', mountains)
    fire(mountains)
}

fireMountain()
