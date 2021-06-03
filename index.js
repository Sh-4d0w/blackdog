const express = require('express');
const ip2loc = require("ip2location-nodejs");
const fs = require('fs');
require('express-group-routes');

const myipaddress = {
	server: express(),
	port: process.env.PORT || 3000
}

const app = myipaddress.server;

app.use(express.json());
app.use(express.urlencoded({ extended: true }))

app.get('/', (req, res) => {
	res.json({
		timestamps: new Date().getTime()
	})
})

app.group("/ip2location", (router) => {
	router.get('/ip/:ip', (req, res) => {
		const { ip } = req.params
		let databases = [];
		fs.readdirSync(__dirname+"/databases").forEach(file => {
			databases.push(__dirname + "/databases/" + file);
		})
		console.log(databases);
		let result = []
		databases.forEach(database => {
			ip2loc.IP2Location_init(database)
			result.push(ip2loc.IP2Location_get_all(ip))
			ip2loc.IP2Location_close();
		})
		res.json(result);
	})
})
app.listen(myipaddress.port, () => {
	console.log('AI Started, Listening on port: http://localhost:'+myipaddress.port);
});