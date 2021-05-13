const express = require('express');
const app = express();
const port = 3000;

app.get('/fibonacci/v1/sequence/:number', (req, res) => {
    const number = parseInt(req.params.number);
    const f = [0, 1];
    for (let i = 2, l = number; i <= l; i++) {
        f.push(f[i - 1] + f[i - 2]);
    }
    res.json({ data: { value: f[number] } })
})

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`)
})
