import { useState, useEffect } from 'react'
import axios from 'axios'

function GetNoun() {

    const [nouns, setNouns] = useState([]);

    useEffect(() => {
    axios.get('/noun/')
    .then(res => setNouns(res.data))
    .catch(error => {
        console.log(error)
    })  
    }, []);

    return(
          <ul>{nouns.map(noun => <li key={noun.id}> {noun.nom_sing} </li>)}</ul>
    )
}

export default GetNoun