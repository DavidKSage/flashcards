import { useState } from 'react'
import axios from 'axios'

function GetNoun() {

    const [nouns, setNouns] = useState([]);
    // let nounList;
    axios.get(`http://localhost:8000/api/noun`)
    .then(res => {
        // nounList = res.data;
        setNouns(res.data);
    })

    return(
          <ul>{nouns.map(noun => <li key={noun.id}> {noun.nom_sing} </li>)}</ul>
    )
}

export default GetNoun