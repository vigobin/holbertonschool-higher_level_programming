#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;
  else {
    const info = JSON.parse(body);
    const taskDict = {};
    for (let i = 0; i < info.length; i++) {
      const userId = info[i].userId;
      if (info[i].completed === true) {
        if (userId in taskDict) {
          taskDict[userId]++;
        } else {
          taskDict[userId] = 1;
        }
      }
    }
    console.log(taskDict);
  }
});
